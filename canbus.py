from datetime import datetime as dt

class CANBus:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, receiver, message):
        can_message = {
            "date":dt.now().strftime("%d/%m/%Y %H:%M:%S"),
            "sender": sender,
            "receiver": receiver,
            "message": message
        }

        self.messages.append(can_message)
        print(f"CAN message sent: {can_message}")
