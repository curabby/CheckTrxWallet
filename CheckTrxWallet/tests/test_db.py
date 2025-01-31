import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from models import Base, CheckTrxWallet

# Тестовая БД (SQLite in-memory)
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(TEST_DATABASE_URL, echo=True)

# Создаём сессию
TestingSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

@pytest_asyncio.fixture
async def async_session():
    """Фикстура для тестовой сессии"""
    async with TestingSessionLocal() as session:
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        yield session
        await session.rollback()

@pytest.mark.asyncio
async def test_create_wallet_request(async_session: AsyncSession):
    """
    Юнит-тест: проверяет, что новая запись создаётся в БД.
    """
    new_check_wallet = CheckTrxWallet(address="TGMwc4f8Xksw8mjeBqtwN2f9qpSAfNBLWb")
    async_session.add(new_check_wallet)
    await async_session.commit()
    await async_session.refresh(new_check_wallet)

    assert new_check_wallet.id is not None
    assert new_check_wallet.address == "TGMwc4f8Xksw8mjeBqtwN2f9qpSAfNBLWb"
