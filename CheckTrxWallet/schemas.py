from pydantic import BaseModel
from datetime import datetime


class CheckWalletRequest(BaseModel):
    """Схема для сохранения запроса в БД"""
    address: str

class CheckWalletResponse(BaseModel):
    """Схема ответа пользователю"""
    address: str
    balance: float
    bandwidth: int
    energy: int


class ListRequestsResponse(BaseModel):
    """Схема ответа о запросах пользователей"""
    id: int
    address: str
    requested_at: datetime
    class Config:
        from_attributes = True