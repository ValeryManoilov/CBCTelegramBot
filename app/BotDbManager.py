from sqlalchemy import create_engine, text
from .user import User, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import BigInteger

# Base = declarative_base()

# admin_engine = create_engine("postgresql://postgres:batareyka@localhost:5432/postgres")
engine = create_engine("postgresql://postgres:batareyka@localhost:5432/cbcdatabase")

Base.metadata.create_all(engine)

# with admin_engine.connect() as conn:
#     # Завершаем ВСЕ активные соединения с базой данных cbcdatabase
#     conn.execute(text("""
#         SELECT pg_terminate_backend(pg_stat_activity.pid)
#         FROM pg_stat_activity
#         WHERE pg_stat_activity.datname = 'cbcdatabase'
#         AND pid <> pg_backend_pid();
#     """))
    
#     # Теперь удаляем базу данных
#     conn.execute(text("COMMIT"))
#     conn.execute(text("DROP DATABASE IF EXISTS cbcdatabase"))
#     print("База данных cbcdatabase удалена")
    
#     # Создаем заново
#     conn.execute(text("CREATE DATABASE cbcdatabase"))
#     print("База данных cbcdatabase создана")

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