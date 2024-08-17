# Author: Nixiris Dartero
# This bot reposts and forwards messages with various options
import json, requests, datetime

apiServer = 'https://api.telegram.org'

class TGMessage:
    def __init__(self):
        self.message_id = 0
        self.is_topic_message = False
    
    @staticmethod
    def test():
        print(22)


class TGUpdateObj:
    def __init__(self):
        update_id = 0
        message = TGMessage()

class TGBot:
    def __init__(self):
        self.token = ''
    
    def sendRequest(self,method):
        headers = {
            'User-Agent': 'Python',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept': 'application/json',
        }
        response = requests.get(url=apiServer + "/" + self.token + "/" + method,headers=headers)
        return response

    def getUpdates(self):
        response = self.sendRequest("getUpdates")
        return json.loads(response.text)



# bot = TGBot()
# updates = bot.getUpdates()
# pass

class MyObject:
    def __init__(self):
        self.__attr = 0
        self.b = 0
    
    def __repr__(self):
        return "Fuck"

    def __str__(self):
        return "Ok"

    @property
    def attr(self):
        return self.__attr
    
    @attr.setter
    def attr(self, val):
        if val < 10:
            self.__attr = val
    @attr.getter
    def attr(self):
        return 0

obj = MyObject()
#print(obj.attr)
obj.attr = 5
print(obj.attr)
obj.attr = 20
print(obj.attr)
obj.attr = 7
print(obj.attr)
obj.b = 5
print(obj.b)
print(obj)