from fastapi import APIRouter

from common import database

router = APIRouter()


@router.post("/accounts", status_code=201)
def create_account(email: str, password: str):
    database.create_account(email, password)


@router.get("/accounts")
def get_account(email: str):
    database.get_account(email)
