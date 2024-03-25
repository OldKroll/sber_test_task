import datetime

from dateutil.relativedelta import relativedelta
from fastapi import APIRouter

from app.schemes.deposit import EntryVector

router = APIRouter()


@router.post("/")
async def calculate_deposit(vector: EntryVector) -> dict[str, float]:
    deposit = {}
    amount = vector.amount
    for i in range(vector.periods):
        amount *= 1 + vector.rate / 12 / 100
        date = vector.date + relativedelta(months=i)
        deposit[date.strftime("%d.%m.%Y")] = round(amount, 2)
    return deposit
