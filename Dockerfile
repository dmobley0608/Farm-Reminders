FROM python:3.12
ADD classes/* ./classes
ADD main.py .
RUN pip install --upgrade pip
RUN pip install psycopg
RUN pip install python-dateutil
CMD ["python","-u", "./main.py"]