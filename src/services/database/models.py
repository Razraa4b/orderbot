from sqlalchemy import BigInteger, String, ForeignKey, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


class User(Base):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(64), nullable=False)
    telegram_id: Mapped[int] = mapped_column(BigInteger(), nullable=False)
    bot_settings: Mapped["UserBotSettings"] = relationship(back_populates="user", cascade="all, delete-orphan")

class UserBotSettings(Base):
    __tablename__ = "UserBotSettings"
    id: Mapped[int] = mapped_column(Integer(), primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer(), ForeignKey("Users.id", ondelete="CASCADE"))
    is_enable: Mapped[bool] = mapped_column(Boolean(), default=True)
    mail_interval: Mapped[int] = mapped_column(Integer(), default=60)
    user: Mapped["User"] = relationship(back_populates="bot_settings", single_parent=True)
