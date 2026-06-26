FROM python:3.9-slim

WORKDIR /NotebookApp
COPY requeriments.txt ./

RUN pip install --no-cach-dir -r

COPY . .

EXPOSE 500

CMD ["python", "app.py"]