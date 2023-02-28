FROM python:3.10-slim
#starting direcory into the container
WORKDIR /code

COPY ./requirements.txt ./
#docker has its own cache
RUN pip install wheel
RUN pip install gunicorn
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "-w","4", "run:app" ]