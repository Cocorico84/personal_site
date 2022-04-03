# FROM python:3

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# RUN mkdir /app 

# COPY /app /app
# COPY pyproject.toml /app 

# WORKDIR /app
# ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

# RUN pip install poetry

# RUN poetry config virtualenvs.create false
# RUN poetry install --no-dev

FROM python:3

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY . /code/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0000:8000"]