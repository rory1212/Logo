FROM python:3.12.3-slim
WORKDIR /app
ENV ENV=PROD
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 1313
CMD ["python", "app.py"]
