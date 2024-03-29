from email import message
import string
import re
from chatData import ChatData

class LineParse:
    __chatNames = set()
    __chatData = [ChatData]
    def __init__(self, textFile):
        self.__chatData.clear()
        lineData = []
        with open(textFile) as f:
            lineData = f.readlines()
        self.__parseData(lineData)

    def __parseData(self, lineData):
        yyyy : int
        mm : int
        dd : int
        dayInWeek : string
        for data in lineData:
            #match yyyy/mm/dd(DayOfWeek)
            matchDate = re.match(r'(\d{4})/(\d+)/(\d+).(.{2}).*', data)
            #match HH:mm "Name" "Message"
            matchMessage = re.match(r'(\d{2}):(\d{2})\t(.*)\t(.*)', data)
            if(matchDate):
                yyyy = matchDate.group(1)
                mm = matchDate.group(2)
                dd = matchDate.group(3)
                dayInWeek = matchDate.group(4)
                #print(matchDate.groups())
            elif(matchMessage):
                #message match [..] or [....]
                messageDecode = re.match(r'\[(.{2}|.{4})\]', matchMessage.group(4))
                #message match ^https?:.*
                httpDecode = re.search(r'(https?://.*|www\..*)', matchMessage.group(4))
                #message match 通話時間 mm:ss
                callDecode = re.match(r'通話時間 (\d*):(\d{2})', matchMessage.group(4))
                messageType = "None"
                if(messageDecode):
                    messageType = messageDecode.group(1)
                elif(httpDecode):
                    messageType = "WebLink"
                elif(callDecode):
                    messageType = "Call"
                    
                self.__chatNames.add(matchMessage.group(3))
                chat = ChatData(yyyy, mm, dd, dayInWeek, matchMessage.group(1), matchMessage.group(2), matchMessage.group(3), messageType, matchMessage.group(4))
                if(messageType == "Call"):
                    totalSec = int(callDecode.group(1))*60
                    totalSec += int(callDecode.group(2))
                    chat.SetCallDuration(totalSec)
                self.__chatData.append(chat)
                #print(matchMessage.groups())
            else:
                if(len(self.__chatData) > 0):
                    self.__chatData[-1].message += data

    def GetTotalChats(self):
        return len(self.__chatData)

    def GetAllNames(self):
        return self.__chatNames
    
    def GetTotalChatCount(self, name):
        return len([x for x in self.__chatData if x.who == name]) 

    def GetSendStickerCount(self, name):
        return len([x for x in self.__chatData if x.who == name and x.messageType == "貼圖"])

    def GetSendPictureCount(self, name):
        return len([x for x in self.__chatData if x.who == name and x.messageType == "照片"])

    def GetSendVideoCount(self, name):
        return len([x for x in self.__chatData if x.who == name and x.messageType == "影片"])

    def GetSendVoiceCount(self, name):
        return len([x for x in self.__chatData if x.who == name and x.messageType == "語音訊息"])

    def GetSendLinkCount(self, name):
        return len([x for x in self.__chatData if x.who == name and x.messageType == "WebLink"])
    
    def GetCallCount(self, name):
        return len([x for x in self.__chatData if x.who == name and x.messageType == "Call"])

    def GetMessageCount(self, name):
        return len([x for x in self.__chatData if x.who == name and x.messageType == "None"])
    
    def GetTotalWordCount(self, name):
        wordCount = 0
        for data in [x for x in self.__chatData if x.who == name and x.messageType == "None"]:
            wordCount += len(data.message)
        return wordCount

    def GetAllChatDates(self):
        days = set()
        for chat in self.__chatData:
            days.add(chat.date)
        dates = [x for x in days]
        dates.sort()
        return dates

    def GetChatTotalDays(self):
        days = set()
        for chat in self.__chatData:
            days.add(chat.date)
        return len(days)
    
    def GetChatDateFromDayIndex(self, dayIndex):
        dates = self.GetAllChatDates()
        return dates[dayIndex - 1]

    def GetChatsCountFromDay(self, dayIndex):
        dates = self.GetAllChatDates()
        return len([x for x in self.__chatData if x.date == dates[dayIndex-1]])

    def GetChatsCountFromDayAndWho(self, dayIndex, name):
        dates = self.GetAllChatDates()
        return len([x for x in self.__chatData if x.date == dates[dayIndex-1] and x.who == name])

    def GetTotalCallSeconds(self, name):
        totalCallSeconds = 0
        for data in [x for x in self.__chatData if x.who == name and x.messageType == "Call"]:
            totalCallSeconds += data.callDurationInSec
        return totalCallSeconds

    def GetTopXMostFrequentLine(self, n):
        wordSet = {}
        senderCount = {}
        for chat in self.__chatData:
            if chat.messageType != "None":
                continue
            if chat.message in wordSet:
                wordSet[chat.message] += 1
                senderCount[chat.message][chat.who] += 1
            else:
                wordSet[chat.message] = 1
                senderCount[chat.message] = {}
                for person in self.__chatNames:
                    senderCount[chat.message][person] = 0
                senderCount[chat.message][chat.who] = 1

        datas = list(wordSet.items())
        datas.sort(key=lambda x:x[1], reverse=True)
        senderCounter = []
        for i in range(len(datas)):
            senderCounter.append(senderCount[datas[i][0]])
      
        return {"datas" : datas[:n], "sender" : senderCounter[:n]}
        
    

