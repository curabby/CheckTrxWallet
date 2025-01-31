from fastapi import FastAPI, HTTPException, Depends
from schemas import CheckWalletResponse, ListRequestsResponse
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from db import get_db
from models import CheckTrxWallet
import httpx
from typing import List
from fastapi import Query

app = FastAPI()


@app.post("/check-wallet", response_model=CheckWalletResponse)
async def CheckWalletAPI(address: str, db: AsyncSession = Depends(get_db)) -> List[CheckWalletResponse]:
    """
       Запись запросов пользователей и направление ответа о проверке кошелька
    """
    tron_api = "https://api.trongrid.io/wallet/getaccount"
    json_data = await get_data_method(tron_api, address)
    if not json_data:
        raise HTTPException(status_code=404, detail="Wallet data not found")
    # Формируем ответ
    data = {
        "address": address,
        "balance": json_data.get("balance", 0) / 1e6,
        "bandwidth": json_data.get("net_window_size", 0),
        "energy": json_data.get("account_resource", {}).get("energy_window_size", 0)
    }
    # Сохраненяем данные о запросе в БД
    new_check = CheckTrxWallet(address=address)
    db.add(new_check)
    await db.commit()
    return data


@app.get("/wallets-requests", response_model=List[ListRequestsResponse])
async def get_wallets(
    db: AsyncSession = Depends(get_db),
    limit: int = Query(25, ge=1, le=100),  # Ограничение количества записей (1-100)
    offset: int = Query(0, ge=0)  # Смещение записей
) -> List[ListRequestsResponse]:
    """
    Получение списка кошельков с пагинацией
    """
    stmt = select(CheckTrxWallet).offset(offset).limit(limit)
    result = await db.execute(stmt)
    wallets_requests = result.scalars().all()
    return wallets_requests


async def get_data_method(url: str, address: str) -> dict:
    """
    Подключение к сети ТРОН по API и получение данных о кошельке
    """
    try:
        payload = {"address": address, "visible": True}
        headers = {
            "accept": "application/json",
            "content-type": "application/json"
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            json_data = response.json()
            return json_data
        else:
            raise HTTPException(status_code=response.status_code, detail="API request failed")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
