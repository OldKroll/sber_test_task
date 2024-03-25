from fastapi import APIRouter

from app.schemes.deposit import EntryVector

router = APIRouter()


@router.post("/")
async def calculate_deposit(vector: EntryVector) -> EntryVector:
    return vector
