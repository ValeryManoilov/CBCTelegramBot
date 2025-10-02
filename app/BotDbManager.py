from sqlalchemy import create_engine, text
from .user import User, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import BigInteger

admin_engine = create_engine("postgresql://postgres:batareyka@localhost:5432/postgres")
engine = create_engine("postgresql://postgres:batareyka@localhost:5432/cbcdatabase")


with admin_engine.connect() as conn:
    result = conn.execute(text("""
        SELECT 1 FROM pg_database WHERE datname = 'cbcdatabase'
    """))
    
    if not result.scalar():
        conn.execute(text("COMMIT"))
        conn.execute(text("CREATE DATABASE cbcdatabase"))
        print("База данных cbcdatabase создана")
    else:
        print("База данных cbcdatabase уже существует")

Base.metadata.create_all(engine)


SessionLocal = sessionmaker(bind=engine)

class Manager:
    def add_user(self, new_user: User):
        with SessionLocal() as session:
            session.add(new_user)
            session.commit()
            print(f"Создан пользователь: {new_user}")
    
    def delete_user(self, tg_id: BigInteger):
        with SessionLocal() as session:
            user = session.query(User).filter(User.telegram_id == tg_id).first()
            if user:
                session.delete(user)
                session.commit()
    
    def get_user(self, tg_id: BigInteger):
        with SessionLocal() as session:
            return session.query(User).filter(User.telegram_id == tg_id).first()
        
    def update_user(self, update_user: User):
        with SessionLocal() as session:
            user = session.query(User).filter(User.telegram_id == update_user.telegram_id).first()
            if user:
                user.surname = update_user.surname
                user.name = update_user.name
                user.patronymic = update_user.patronymic
                session.commit()