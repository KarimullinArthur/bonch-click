from fastapi import APIRouter, Depends, Response

from api.dependencies.auth import verify_token
from common import database

router = APIRouter(
    tags=["accounts"],
    dependencies=[Depends(verify_token)],
)


@router.post("/accounts", status_code=201)
def create_account(email: str, password: str):
    database.create_account(email, password)


@router.get("/accounts")
def get_account(email: str, response: Response):
    account = database.get_account(email)
    if account:
        return account

    response.status_code = 404


@router.delete("/accounts")
def delete_account(email: str):
    database.delete_account(email)


@router.patch("/accounts", status_code=204)
def update_account(email: str, new_password: str, response: Response):
    result = database.edit_account(email, new_password)
    if result is None:
        response.status_code = 404
