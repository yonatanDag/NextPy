from file1 import GreetingCard


class BirthdayCard(GreetingCard):
    def __init__(self, sender_age=0, recipient="Dana Ev", sender="Eyal Ch"):
        super().__init__(recipient, sender)
        self._sender_age = sender_age

    def greeting_msg(self):
        super().greeting_msg()
        print(f"the age of the sender is: {self._sender_age}")