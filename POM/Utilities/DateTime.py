import datetime
import time
from dateutil import relativedelta
from dateutil.relativedelta import relativedelta
from datetime import date, timedelta


class DateTime(object):

    @staticmethod
    def GetPresentTime():
        CurrentTime = datetime.datetime.now()
        return CurrentTime

    @staticmethod
    def GetTimeDifferenceInMinute(PastTime):
        CurrentTime = DateTime.GetPresentTime()
        TimeDifference = relativedelta.relativedelta(CurrentTime, PastTime)
        return TimeDifference.minutes

    @staticmethod
    def GetTimeDifferenceInSecond(PastTime):
        CurrentTime = DateTime.GetPresentTime()
        TimeDifference = relativedelta.relativedelta(CurrentTime, PastTime)
        return TimeDifference.seconds

    @staticmethod
    def GetTimeStamp(FormatTimeStamp='%Y_%m_%d_%H_%M_%S'):
        return datetime.datetime.fromtimestamp(time.time()).strftime(FormatTimeStamp)

    @staticmethod
    def GetCurrentTime(FormatTime='%H:%M:%S'):
        return datetime.datetime.fromtimestamp(time.time()).strftime(FormatTime)

    @staticmethod
    def GetCurrentDate(FormatTimeStamp='%Y-%m-%d'):
        return datetime.datetime.fromtimestamp(time.time()).strftime(FormatTimeStamp)

    @staticmethod
    def GetCurrentDateTime(FormatTimeStamp='%Y-%m-%d %H:%M:%S'):
        return datetime.datetime.fromtimestamp(time.time()).strftime(FormatTimeStamp)

    @staticmethod
    def AddDays(Day=0, Month=0, Year=0, Hour=0, Minute=0, Second=0, DateTimeFormat='%Y-%m-%d %H:%M:%S'):
        if (Day != 0):
            CurrentDateTime = datetime.datetime.today() + relativedelta(days=Day)
        elif (Month != 0):
            CurrentDateTime = datetime.datetime.today() + relativedelta(months=Month)
        elif (Year != 0):
            CurrentDateTime = datetime.datetime.today() + relativedelta(years=Year)
        elif (Hour != 0):
            CurrentDateTime = datetime.datetime.today() + relativedelta(hours=Hour)
        elif (Minute != 0):
            CurrentDateTime = datetime.datetime.today() + relativedelta(minutes=Minute)
        elif (Second != 0):
            CurrentDateTime = datetime.datetime.today() + relativedelta(seconds=Second)
        else:
            CurrentDateTime = datetime.datetime.now()
        return CurrentDateTime.strftime(DateTimeFormat);

    @staticmethod
    def GetRandomDate():
        pass;
