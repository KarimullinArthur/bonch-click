FROM python:3.12-slim

WORKDIR /app

COPY migrator/requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH=/app/src

CMD ["alembic", "upgrade", "head"]
