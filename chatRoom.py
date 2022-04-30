from person import Person

class ChatRoom:
    people = [Person]

    def __init__(self):
        self.people.clear()
    
    def AddPerson(self, person : Person):
        self.people.append(person)

    def GetPerson(self, name):
         for p in self.people:
            if(p.name == name):
                return p

    def GetChatRatio(self, name):
        d = sum(p.totalChats for p in self.people)
        for p in self.people:
            if(p.name == name):
                return p.totalChats / d if d else 0
        return 0

    def GetMessageRatio(self, name):
        d = sum(p.messageCount for p in self.people)
        for p in self.people:
            if(p.name == name):
                return p.messageCount / d if d else 0
        return 0
    
    def GetWordRatio(self, name):
        d = sum(p.totalWordCount for p in self.people)
        for p in self.people:
            if(p.name == name):
                return p.totalWordCount / d if d else 0
        return 0
    
    def GetStickerRatio(self, name):
        d = sum(p.stickerCount for p in self.people)
        for p in self.people:
            if(p.name == name):
                return p.stickerCount / d if d else 0
        return 0
    
    def GetPictureRatio(self, name):
        d = sum(p.pictureCount for p in self.people)
        for p in self.people:
            if(p.name == name):
                return p.pictureCount / d if d else 0
        return 0

    def GetVideoRatio(self, name):
        d = sum(p.videoCount for p in self.people)
        for p in self.people:
            if(p.name == name):
                return p.videoCount / d if d else 0
        return 0
    
    def GetVoiceRatio(self, name):
        d = sum(p.voiceCount for p in self.people)
        for p in self.people:
            if(p.name == name):
                return p.voiceCount / d if d else 0
        return 0
    
    def GetLinkRatio(self, name):
        d = sum(p.linkCount for p in self.people)
        for p in self.people:
            if(p.name == name):
                return p.linkCount / d if d else 0
        return 0

        