

class Record:
    def __init__(self,horse, date,rabies, coggins, wormed, yearly_vaccines) :
        self.date = date
        self.rabies = rabies
        self.horse = horse
        self.coggins = coggins
        self.wormed = wormed
        self.yearly_vaccines = yearly_vaccines
        
    def __str__(self) -> str:
        return f"Horse: {self.horse.name}, Date: {self.date}, Coggins:{self.coggins}, Wormed:{self.wormed}, Yearly Vaccines: {self.yearly_vaccines}"