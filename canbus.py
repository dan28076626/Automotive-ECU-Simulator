from datetime import datetime as dt

class CANBus:
    id_codes={
            "ECU": "0x101",
            "DASHBOARD": "0x102",
            "ABS": "0x103",
            "TCM":"0x104",
            "TPMS": "0x105"
        }

    def __init__(self):
        self.messages=[]
        
    def send_message(self, sender, receiver, message, data):
        can_id=self.id_codes.get(receiver.upper(),"0x000")
        can_message ={
             "id": can_id,
            "timestamp": dt.now().strftime("%d/%m/%Y %H:%M:%S"),   
            "sender": sender,
            "receiver": receiver,
            "command": message,
            "data": data,
            "processed": False

        }
           
               
   


        self.messages.append(can_message)
