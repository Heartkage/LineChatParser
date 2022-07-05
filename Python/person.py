import string


class Person:
    name : string
    totalChats : int
    messageCount : int
    totalWordCount : int
    stickerCount : int
    pictureCount : int
    videoCount : int
    voiceCount : int
    linkCount : int

    def __init__(self, name, chats, messages, words, stickers, pictures, videos, voice, links):
        self.name = name
        self.totalChats = chats
        self.messageCount = messages
        self.totalWordCount = words
        self.stickerCount = stickers
        self.pictureCount = pictures
        self.videoCount = videos
        self.voiceCount = voice
        self.linkCount = links