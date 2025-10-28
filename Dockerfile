FROM python:3.13
WORKDIR /expenses
COPY . .
RUN pip install --upgrade -r requirements.txt
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]