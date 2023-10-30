from datetime import datetime
from dateutil.relativedelta import relativedelta  
class Horse:
    def __init__(self, name, records = [], off_prop_rides = False):
        self.name = name
        self.off_property_rides = off_prop_rides
        self.records = records
        
    def add_record (self, record):
        self.records.append(record)       
    
    
    def check_coggins(self):
        records = list(filter(lambda record: (record["coggins"] == True and self.off_property_rides), self.records))
        if len(records) > 0:
            record_date = datetime.strptime(records[0].get("date"), '%Y-%m-%d')
            months = relativedelta(datetime.now(), record_date).months
            years = relativedelta(datetime.now(),record_date).years       
            if months > 10 or years > 0:
                return f'{self.name} - Last Coggins {records[0].get('date')}'   
        elif self.off_property_rides:
            return f'{self.name} - No Coggins On Record'
    
    def check_yearly(self, vaccine):
        records = list(filter(lambda record: (record[vaccine] == True), self.records))
        if len(records) > 0:
            record_date = datetime.strptime(records[0].get("date"), '%Y-%m-%d')
            months = relativedelta(datetime.now(), record_date).months
            years = relativedelta(datetime.now(),record_date).years       
            if months > 10 or years > 0:
               return f'{self.name} - Last {vaccine.capitalize()} {records[0].get('date')}'         
        elif len(records) == 0:
            return f'{self.name} - No {vaccine.capitalize()} on record.'
    
    def check_quarterly(self, vaccine):
        records = list(filter(lambda record: record[vaccine] == True, self.records))  
        if len(records) > 0:
            record_date = datetime.strptime(records[0].get("date"), '%Y-%m-%d')
            months = relativedelta(datetime.now(), record_date).months
            years = relativedelta(datetime.now(),record_date).years       
            if months > 3 or years > 0:
               return f'{self.name} - Last {vaccine.capitalize()} {records[0].get('date')}'         
        elif len(records) == 0:
            return f'{self.name} - No {vaccine.capitalize()} on record.'
        
    
    def __str__(self) -> str:
        return self.name
        
        
      