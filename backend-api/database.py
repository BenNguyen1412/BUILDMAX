from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

# Chuỗi kết nối đúng với cấu hình Docker của bạn (User: Ben, Pass: 1412, DB: BUILDMAX_db)
DATABASE_URL = "postgresql+asyncpg://Ben:1412@localhost:5432/BUILDMAX_db"

engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()