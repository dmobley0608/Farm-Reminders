import requests
from classes.horse import Horse
from classes.record import  Record
from classes.email import Email
from datetime import datetime
import time
url = 'db.tgdqkumgqyptsqjmlwkf.supabase.co'
                




while True: 
    count = 0   
    horses = []    
    worming = []
    coggins = []
    vaccines = []
    rabies = []
    print("-"*150)
    print(f"Checking Records current time is {datetime.now()}")  
    #Fetch Data   
    r = requests.get('https://ddcattle.company/api/horses')
    data = r.json()
    print(f'Record Check Complete')
    for horse in data:
        horses.append(Horse(horse['name'], horse['MedicalRecords'], horse['off_property_rides']))
          
    #Check Record Dates
    for horse in horses: 
        #Check For Coggins
        count += len(horse.records)
        records = horse.check_records()
        coggins.append(records.get('coggins') or  )
        rabies.append(records.get('rabies'))
        vaccines.append(records.get('vaccines'))
        worming.append(records.get('wormed'))
    print(coggins)
  
   
    #Print status
    print(f'Checked {count} Records')
    print(f'{len(coggins)} - Horses Need Coggins')
    print(f'{len(worming)} - Horses Need To Be Wormed')
    print(f'{len(vaccines)} - Horses Need Yearly Vaccines')
    print(f'{len(rabies)} - Horses Need A Rabies Shot')
    # Send Email with results   
    if len(coggins) > 0 or len(rabies) > 0 or len(worming) > 0 or len(vaccines) > 0:
        email = Email("Vaccination/Worming Status")
        email.add_recipient('dmobley0608@gmail.com')
        email.add_recipient('djones@hallcounty.org')
        # email.set_body_for_vaccines(coggins, rabies, vaccines, worming)
        # email.send_email()
        print(email.body)
        
    else:
        print("All records up to date")
    print("Going To Sleep. I will check again tomorrow!")
    print("-"*150)
    # Wait One Day and Do it again
    time.sleep(86400)        