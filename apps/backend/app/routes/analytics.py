from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Analytics overview")
async def analytics_overview():
    return {"message": "Analytics overview"} 