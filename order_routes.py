from fastapi import APIRouter


order_router = APIRouter(prefix="/orders",tags=["orders"])


@order_router.get("/")
async def order():
    return {"order":"here is order page"}