from datetime import datetime
from dateutil.relativedelta import relativedelta  
class Horse:
    def __init__(self, name, off_prop_rides):
        self.name = name
        self.off_property_rides = off_prop_rides
        self.records = []
        
    def add_record (self, record):
        self.records.append(record)
        
    def check_record(self, property,due, reminder):
        properties = []
        for record in self.records:
           if getattr(record, property):               
                properties.append(record.date)
        properties.sort()
        if len(properties) > 0:
           months =relativedelta(datetime.now(),properties[-1]).months
           years = relativedelta(datetime.now(),properties[-1]).years         
           if months > reminder or years > 0:                             
               return True
        else:           
            return True
        return False
        
        
        