from sqlalchemy import func, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime


class Base(DeclarativeBase):
    pass


class CheckTrxWallet(Base):
    __tablename__ = 'check_trx_wallet'
    id: Mapped[int] = mapped_column(primary_key=True)
    address: Mapped[str] = mapped_column(String(128), nullable=False)
    request_from_user: Mapped[int] = mapped_column(Integer, nullable=True)
    requested_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(),
                                                   nullable=False)
