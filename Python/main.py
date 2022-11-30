#coding=utf8
import sys
from chatRoom import ChatRoom
from person import Person
from lineParse import LineParse

if len(sys.argv) != 2:
    print("Please give a txt file as input argument")

fileName = sys.argv[1]
print("Reading file: " + fileName + "\n")

line = LineParse(fileName)

names = line.GetAllNames()
chatRoom = ChatRoom()

totalChat = line.GetTotalChats()
print("-----總共 {} 則訊息-----".format(totalChat))
for name in names:
    person = Person(name, line.GetTotalChatCount(name), line.GetMessageCount(name), line.GetTotalWordCount(name),line.GetSendStickerCount(name), line.GetSendPictureCount(name), line.GetSendVideoCount(name), line.GetSendVoiceCount(name), line.GetSendLinkCount(name), line.GetCallCount(name), line.GetTotalCallSeconds(name))
    chatRoom.AddPerson(person)

for name in names:
    person : Person = chatRoom.GetPerson(name)
    callHours = int(person.callTotalSeconds / 3600)
    callMinutes = int(person.callTotalSeconds / 60)
    CallSeconds = int(person.callTotalSeconds % 60)
    print("{}: {}則({:.0%})".format(name, person.totalChats, chatRoom.GetChatRatio(name)))
    print("    {} 串文字({:.0%}), {} 總字數({:.0%})".format(person.messageCount, chatRoom.GetMessageRatio(name), person.totalWordCount, chatRoom.GetWordRatio(name)))
    print("    {} 貼圖({:.0%}), {} 照片({:.0%}), {} 影片({:.0%}), {} 語音訊息({:.0%}), {} 網址連結({:.0%}), {} 通話次數({:.0%}), {}:{:02d}:{:02d} 總通話時間".format(person.stickerCount, chatRoom.GetStickerRatio(name), person.pictureCount, chatRoom.GetPictureRatio(name), person.videoCount, chatRoom.GetVideoRatio(name), person.voiceCount, chatRoom.GetVoiceRatio(name), person.linkCount, chatRoom.GetLinkRatio(name), person.callCount, chatRoom.GetCallRatio(name), callHours, callMinutes, CallSeconds))
print("")

totalChatDays = line.GetChatTotalDays()
print(f"-----聊天天數: {totalChatDays}天-----")
for i in range(totalChatDays):
    print(f"{line.GetChatDateFromDayIndex(i+1)}(Day {i+1:2d}): 總{line.GetChatsCountFromDay(i+1):3d}則", end=" ")
    for name in names:
        print(f"    {name}: {line.GetChatsCountFromDayAndWho(i+1, name):3d}則", end=" "),
    print("")
print("")

n = 150
print(f"-----Top{n} 最常使用的句子-----")
datas = line.GetTopXMostFrequentLine(n)
sentences = datas["datas"]
sender = datas["sender"]
for i in range(len(sentences)):
    senderString = ""
    for name in names:
        senderString += f", ({name}:{sender[i][name]}次)"
    print(f"No.{i+1}: \"{sentences[i][0]}\" 總{sentences[i][1]}次{senderString}")

print("")