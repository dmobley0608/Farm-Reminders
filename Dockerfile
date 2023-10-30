FROM python:3.12
#Environment Variables
ENV REQUEST_URL=https://ddcattle.company/api/horses
ENV EMAIL_1=dmobley0608@gmail.com
ENV EMAIL_2=djones@hallcounty.org
ENV GOOGLE_USERNAME=dmobley0608@gmail.com
ENV GOOGLE_KEY='tons bame pkmc vgxq'
#Add Files
ADD classes/* ./classes
ADD main.py .
#Install Third Party
RUN pip install --upgrade pip
RUN pip install requests
RUN pip install python-dateutil
RUN pip install python-dotenv
#Run Program
CMD ["python","-u", "./main.py"]