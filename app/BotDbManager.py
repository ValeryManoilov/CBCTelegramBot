from sqlalchemy import create_engine, text
from .user import User, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Base = declarative_base()

# admin_engine = create_engine("postgresql://postgres:batareyka@localhost:5432/postgres")
engine = create_engine("postgresql://postgres:batareyka@localhost:5432/cbcdatabase")

Base.metadata.create_all(engine)

# with admin_engine.connect() as conn:
#     conn.execute(text("COMMIT"))
#     conn.execute(text("CREATE DATABASE cbcdatabase"))

SessionLocal = sessionmaker(bind=engine)

class Manager:
    def add_user(self, new_user: User):
        with SessionLocal() as session:
            session.add(new_user)
            session.commit()
            print(f"Создан пользователь: {new_user}")
    
    def delete_user(self, tg_id):
        with SessionLocal() as session:
            user = session.query(User).filter(User.telegram_id == tg_id).first()
            if user:
                session.delete(user)
                session.commit()
    
    def get_user(self, tg_id):
        with SessionLocal() as session:
            return session.query(User).filter(User.telegram_id == tg_id).first()