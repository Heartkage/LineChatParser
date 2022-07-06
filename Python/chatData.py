from datetime import datetime
import string
from this import s

class ChatData:
    # Date
    dateTime : datetime
    date : string
    year: int
    month: int
    day: int
    dayInWeek: string
    # Time
    HH: int
    mm: int
    # Person
    who: string
    # Chat
    messageType: string
    message: string
    # Call
    callDurationInSec: int

    def __init__(self, yyyy, MM, dd, day, HH, mm, w, msgType, msg):
        self.year = yyyy
        self.month = MM
        self.day = dd
        self.dayInWeek = day
        self.HH = HH
        self.mm = mm
        self.who = w
        self.messageType = msgType
        self.message = msg
        self.callDurationInSec = 0

        self.dateTime = datetime(int(yyyy), int(MM), int(dd), int(HH), int(mm))
        self.date = self.dateTime.strftime("%Y/%m/%d")

    def SetCallDuration(self, callInSec):
        self.callDurationInSec = callInSec