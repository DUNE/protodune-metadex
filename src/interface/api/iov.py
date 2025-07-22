from fastapi import APIRouter

router = APIRouter()


@router.get("/iovs/", tags=["iovs"])
async def read_iovs():
    return [{}]
