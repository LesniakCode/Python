from calendar import monthrange, calendar
import datetime


class Credit:
    '''
    Base credit object
    Fields  name    overall time    intrests
            str     int     years   %
    Methods get_gen_info




    '''
    def __init__(self, Name, Overall=0, Time=0, Intersts=0):
        self.name = Name
        self.overall = Overall
        self.time = Time
        self.intrests = Intersts
        self.current = Overall

    def get_gen_info(self):
        print("Credit: {} \nOverall: {}\nTime: {}\nIntrests: \
            {}".format(self.name, self.overall, self.time, self.intrests))

    def _firstSchCalc(self):
       pass 

    def _calcMonth(self):
        installment = self.current * self.intrests * self.time / 365
        return installment

    def _getDaysOfMonth(self, month) -> int:
        return monthrange(self._getYear(), month)

    def _getYear(self) -> int:
        today = datetime.date.today()
        return today.year
        
    def _days_in_year(year=datetime.datetime.now().year):
        return 365 + calendar.isleap(year)