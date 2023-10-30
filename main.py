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
    records = []
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
        needs_coggins = horse.check_coggins()
        if needs_coggins:        
            coggins.append(needs_coggins)
       
        #Check Rabies Status
        needs_rabies = horse.check_yearly('rabies')
        if needs_rabies:
            rabies.append(needs_rabies)
        
        #Check Wormed Status
        needs_wormed = horse.check_quarterly('wormed')
        if needs_wormed:
            worming.append(needs_wormed)
            
        #Check Yearly Vaccines
        needs_yearly = horse.check_yearly('yearly_vaccines')
        if needs_yearly:
            vaccines.append(needs_yearly) 
  
   
    #Print status
    print(f'{len(coggins)} - Horses Need Coggins')
    print(f'{len(worming)} - Horses Need To Be Wormed')
    print(f'{len(vaccines)} - Horses Need Yearly Vaccines')
    print(f'{len(rabies)} - Horses Need A Rabies Shot')
    # Send Email with results   
    if len(coggins) > 0 or len(rabies) > 0 or len(worming) > 0 or len(vaccines) > 0:
        email = Email("Vaccination/Worming Status")
        email.add_recipient('dmobley0608@gmail.com')
        email.add_recipient('djones@hallcounty.org')
        email.set_body_for_vaccines(coggins, rabies, vaccines, worming)
        email.send_email()
    else:
        print("All records up to date")
    print("Going To Sleep. I will check again tomorrow!")
    print("-"*150)
    # Wait One Day and Do it again
    time.sleep(86400)        