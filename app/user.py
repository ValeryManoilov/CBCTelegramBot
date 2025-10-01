from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, String

Base = declarative_base()

class User(Base):

    __tablename__ = "user"

    telegram_id = Column(
        BigInteger,
        unique=True,
        primary_key=True
    )

    name = Column(String)

    surname = Column(String)

    patronymic = Column(String)

    def __str__(self):
        return f"{self.telegram_id} - {self.surname} - {self.name} - {self.patronymic}"