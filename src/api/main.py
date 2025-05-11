from fastapi import FastAPI
from uvicorn import run

from api import routers

app = FastAPI()
app.include_router(routers.main_router)


if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
