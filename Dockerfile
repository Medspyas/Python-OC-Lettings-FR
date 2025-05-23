FROM python:3.11-slim


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY . /app/


RUN pip install --no-cache-dir --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt


RUN python manage.py collectstatic --noinput


EXPOSE 8000

CMD ["gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000"]