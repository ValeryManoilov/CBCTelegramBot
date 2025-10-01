from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):

    __tablename__ = "user"

    id = Column(
        Integer,
        unique=True,
        primary_key=True,
        autoincrement=True,
        nullable=False 
    )

    telegram_id = Column(
        String,
        unique=True
    )

    name = Column(String)

    surname = Column(String)

    patronymic = Column(String)

    def __str__(self):
        return f"{self.id} - {self.telegram_id} - {self.surname} - {self.name} - {self.patronymic}"