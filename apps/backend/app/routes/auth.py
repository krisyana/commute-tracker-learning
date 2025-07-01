from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Auth endpoint")
async def auth_root():
    return {"message": "Auth endpoint"} 