#dockerfile, image, container
FROM python:3.9


ADD main.py .
ADD update.py .
ADD secret.json .
#ADD AL29D.xlsx .
#ADD AL30D.xlsx .
#ADD AL30.xlsx .
#ADD AL41D.xlsx .
#ADD AE38D.xlsx .
#ADD AE38.xlsx .
#ADD GD30D.xlsx .
#ADD AL29.xlsx .
ADD requirements.txt .

RUN pip install openpyxl pandas psycopg2 sqlalchemy wget


CMD ["python", "./main.py", "./update.py"]