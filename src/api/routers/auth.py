from fastapi import APIRouter, HTTPException, status

from api import services
from api.dependencies import AuthDep, create_access_token

router = APIRouter(tags=["auth"])


@router.post("/token")
async def login(form: AuthDep):
    all_creds = services.auth.get_all_creds()

    cred_from_req = {
        "username": form.username,
        "password": form.password,
    }

    if cred_from_req not in all_creds:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверные учетные данные"
        )

    access_token = create_access_token(data={"sub": form.username})
    return {"access_token": access_token, "token_type": "bearer"}
