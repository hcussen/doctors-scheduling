from case import Case

class Doctor:
    def __init__(self) -> None:
        self.name = ""
        self.loves_family = False #can change this to a continuous value for a "loves-family" scale
        self.compensation = 0 #money made from working case
        self.case_sched = [] #list of cases they are doing
        self.availability = [True] * 24 #personal availaiblity from hour 0 to hour 23
        self.hospital_trips = 0 #trips to the hospital: trip to and then from hospital is ONE
        self.breaks = 0 #number of breaks AT the hospital
    
    def get_name(self) -> str:
        return self.name
    
    def get_loves_family(self) -> bool:
        return self.loves_family
    
    def available_at(self, start: int, end: int) -> bool: 
        for x in range(start,end):
            if not self.availability[x]:
                return False
        return True
    
    def can_work(self, case: Case) -> bool: 
        return self.available_at(case.get_start, case.get_end)

    def get_case_utility(self, case: Case) -> int:
        utility = case.get_comp
        if self.loves_family:
            if case.get_end > 15:
                temp = case.get_end - 15
                utility = utility - ((utility / (2 * case.get_length)) * temp)
        return utility 

    def update_trips_and_breaks(self, case: Case) -> None:
        pass

    def goes_home(self, end: int, start_next: int) -> bool:
        #does the calculations to see if the doctors has time to go home, then updates hospital trips and breaks accordingly
        pass

    def take_case(self, case: Case) -> None:
        self.case_sched.append(case)
        for x in range(case.get_start,case.get_end):
            self.availability[x] = False
        update_trips_and_breaks(case)