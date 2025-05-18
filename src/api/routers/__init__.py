from fastapi import APIRouter

from .accounts import router as accounts_router
from .auth import router as auth_router

main_router = APIRouter()
main_router.include_router(accounts_router)
main_router.include_router(auth_router)
