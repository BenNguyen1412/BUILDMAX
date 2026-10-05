from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from database import AsyncSessionLocal

app = FastAPI(title="BUILDMAX Booking API")

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@app.get("/")
async def root():
    return {"message": "Hệ thống Backend BUILDMAX đã sẵn sàng!"}

@app.get("/test-db")
async def test_connection(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "Thành công!", "message": "Đã kết nối hoàn hảo với PostgreSQL (BUILDMAX_db)."}
    except Exception as e:
        return {"status": "Lỗi kết nối", "chi_tiet": str(e)}