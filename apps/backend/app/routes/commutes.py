from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="List commutes")
async def list_commutes():
    return {"message": "List of commutes"} 