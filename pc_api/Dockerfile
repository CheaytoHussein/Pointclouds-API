FROM python:3.9.12

WORKDIR /app/pc_api

COPY ./requirements.txt .

RUN apt-get update && apt-get install --no-install-recommends -y wget gnupg curl && apt-get install --no-install-recommends -y \
    libgl1 \
    libgomp1 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY ./. .

ENV PYTHONPATH "${PYTHONPATH}:/app/pc_worker"

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

