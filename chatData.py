from datetime import datetime
import string

class ChatData:
    # Date
    dateTime : datetime
    date : string
    year: int
    month: int
    day: int
    # Time
    HH: int
    mm: int
    # Person
    who: string
    # Chat
    messageType: string
    message: string

    def __init__(self, yyyy, MM, dd, HH, mm, w, msgType, msg):
        self.year = yyyy
        self.month = MM
        self.day = dd
        self.HH = HH
        self.mm = mm
        self.who = w
        self.messageType = msgType
        self.message = msg

        self.dateTime = datetime(int(yyyy), int(MM), int(dd), int(HH), int(mm))
        self.date = self.dateTime.strftime("%Y/%m/%d")
