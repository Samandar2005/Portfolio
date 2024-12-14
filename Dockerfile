# Python asosiy tasviri
FROM python:3.10-slim

# Ishchi katalogni belgilash
WORKDIR /app

# Talablar faylini nusxalash va o'rnatish
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Loyihani nusxalash
COPY . /app/

# Django statik fayllarini yig‘ish
RUN python manage.py collectstatic --noinput

# Portni belgilash
EXPOSE 8000

# Django loyihasini ishga tushirish uchun buyruq
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]