from fastapi import APIRouter

from .accounts import router as accounts_router

main_router = APIRouter()
main_router.include_router(accounts_router)
