import json
from random import randint
from time import sleep



from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer

class WSConsumer(WebsocketConsumer):
    def connect(self):
        rand = randint(1, 100)
        self.accept()
        
        for i in range(1000):
            self.send(json.dump({'message': rand}))
            sleep(2)
    