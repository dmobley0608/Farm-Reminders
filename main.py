import psycopg
from classes.horse import Horse
from classes.record import  Record
from email.message import EmailMessage
import ssl
import smtplib
from datetime import datetime
import time
url = 'db.tgdqkumgqyptsqjmlwkf.supabase.co'



    
                
google_key = 'tons bame pkmc vgxq'
email_sender = 'dmobley0608@gmail.com'
email_reciever = 'tmobley@hallcounty.org'
subject = "DD Cattle"
body = f"""
<img src='https://ddcattle.company/static/media/ddc.b51fd10ab57a812f22d9.png' width='200px'/>
<h1>Vaccination Status and Worming Updates</h1>
<h2>The following horses need to be wormed:</h2>
<ol>
<li>
    {'<li>'.join(worming)}
</ol>
<hr>
<h2>The following horses need Coggins pulled:</h2>
<ol>
<li>
    {'<li>'.join(coggins)}
</ol>
<hr>
<h2>The following horses need rabies shots:</h2>
<ol>
<li>
    {'<li>'.join(rabies)}
</ol>
<hr>
<h2>The following horses need yearly vaccines:</h2>
<ol>
<li>
    {'<li>'.join(vaccines)}
</ol>
<hr>
"""
welcome_message =  f"""
<img src='https://ddcattle.company/static/media/ddc.b51fd10ab57a812f22d9.png' width='200px'/>
<h1>You have been enrolled to recieve DDCATTLE'S Vaccination Status and Worming Updates</h1>
"""
em = EmailMessage()
em['From'] = 'ddcattle company'
em['To'] = email_reciever
em.add_header('Content-Type','text/html')
em['Subject'] = subject
em.set_payload(welcome_message)

context = ssl.create_default_context()
print("Sending Initial Email")
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, google_key)
            smtp.sendmail(email_sender, email_reciever,em.as_string())


while True: 
    count = 0   
    horses = {}
    records = []
    worming = []
    coggins = []
    vaccines = []
    rabies = []
    
    print(f"Checking Records current time is {datetime.now()}")  
    #Fetch Data
    print("Fetching Records")
    with psycopg.connect(f'host={url} user=postgres password=thebigdawgisawesome! port=5432') as conn:
        with conn.cursor() as cur:
            cur.execute('Select name, date, wormed, coggins, rabies, yearly_vaccines, off_property_rides FROM medical_records JOIN horses ON horses.id = medical_records.horse_id')
            response = cur.fetchall()
            for record in response:           
                if not horses.get(record[0]):
                    horses[record[0]] = Horse(record[0], record[6])
                records.append(record)
                count += 1
    print(f"{count} Records")
    #Organize Records By Horse
    for record in records:
        if horses[record[0]].name == record[0]:
            horses[record[0]].add_record(Record(horse=horses.get(record[0]),date=record[1],rabies= record[4],coggins= record[3],wormed= record[2],yearly_vaccines= record[5]))
    #Check Record Dates
    for horse in horses.values():    
        if horse.check_record('coggins',12, 9) and horse.off_property_rides:
            coggins.append(horse.name)
        if horse.check_record('rabies',12, 9):
            rabies.append(horse.name)
        if horse.check_record('wormed',4, 4):
            worming.append(horse.name)
        if horse.check_record('yearly_vaccines',12, 9):
            vaccines.append(horse.name)
            
    #Set Body For Email
    body = f"""
        <img src='https://ddcattle.company/static/media/ddc.b51fd10ab57a812f22d9.png' width='200px'/>
        <h1>Vaccination Status and Worming Updates</h1>
        <h2>The following horses need to be wormed:</h2>
        <ol>
        <li>
            {'<li>'.join(worming)}
        </ol>
        <hr>
        <h2>The following horses need Coggins pulled:</h2>
        <ol>
        <li>
            {'<li>'.join(coggins)}
        </ol>
        <hr>
        <h2>The following horses need rabies shots:</h2>
        <ol>
        <li>
            {'<li>'.join(rabies)}
        </ol>
        <hr>
        <h2>The following horses need yearly vaccines:</h2>
        <ol>
        <li>
            {'<li>'.join(vaccines)}
        </ol>
        <hr>
"""
    em.set_payload(body)
    # Send Email with results
    if len(coggins) > 0 or len(rabies) > 0 or len(worming) > 0 or len(vaccines) > 0:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, google_key)
            smtp.sendmail(email_sender, email_reciever, em.as_string()) 
    # Wait an Hour and Do it again
    time.sleep(3600)        