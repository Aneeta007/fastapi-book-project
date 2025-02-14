from fastapi import APIRouter

router = APIRouter()

@router.get("/stage2")
async def stage2():
    return {"message": "Stage 2 endpoint is available!"}
