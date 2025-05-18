FROM python:3.12-slim

ENV PYTHONPATH=/app/src

WORKDIR /app
#COPY ./src/common .

COPY ./pyproject.toml .

RUN pip install --no-cache-dir .

COPY . .
#COPY ./src/common common
#COPY ./src/api api
#COPY ./.env .

CMD ["python3", "src/api/main.py"]
