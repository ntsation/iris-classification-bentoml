FROM python:3.12-slim

WORKDIR /app

COPY ./config/requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

COPY ./src/ ./src/
COPY ./bentoml/bentofile.yaml .

RUN python src/main.py

EXPOSE 3000

CMD ["bentoml", "serve", "src.services.iris_service:IrisClassifierService", "--production"]

