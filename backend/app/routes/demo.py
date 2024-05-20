from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
async def index():
    return {"message": "Hello, World!"}

@router.get("/demo")
async def demo():
    return {"demo": "This is a demo route!"}