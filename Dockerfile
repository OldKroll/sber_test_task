FROM python:3.12
COPY app/ /proj/app/
COPY requirements.txt /proj/app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /proj/app/requirements.txt
WORKDIR /proj
CMD gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
