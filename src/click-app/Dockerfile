FROM python:3.12-slim

# Устанавливаем curl для supercronic
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Ставим supercronic
RUN curl -fsSLo /usr/local/bin/supercronic https://github.com/aptible/supercronic/releases/latest/download/supercronic-linux-amd64 \
    && chmod +x /usr/local/bin/supercronic

# Устанавливаем pip с поддержкой pyproject.toml
RUN pip install --upgrade pip

ENV PYTHONPATH=/app/src

WORKDIR /app

COPY ./pyproject.toml .

# Ставим зависимости через pip
RUN pip install --no-cache-dir .

# Теперь копируем код
COPY . . 
#COPY ./src/common common
#COPY ./src/click-app click-app
#COPY ./src/click-app/cronfile .
#COPY ./.env .

CMD ["/usr/local/bin/supercronic", "src/click-app/cronfile"]
