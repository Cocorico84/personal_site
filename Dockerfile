FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN groupadd -g 999 python && \
    useradd -r -u 999 -g python python

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

USER 999

EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
