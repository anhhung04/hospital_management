from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
async def index():
    return {"message": "Hello, World!"}

@router.get("/demo")
async def demo():
    demo = "This is a demo route!"
    return {"demo": "This is a demo route!"}