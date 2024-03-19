from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/hello")
async def index():
    return {"message": "Hello, World!"}