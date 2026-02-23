# Exercise 1 : Call History
# Instructions

#     Create a class called Phone. This class takes a parameter called phone_number. When instantiating an object create an attribute called call_history which value is an empty list.
class Phone:

    def __init__(self, phone_number):
        self.number = phone_number
        self.call_history = []
        self.messages = []
#     Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. The method should print a string stating who called who, and add this string to the phone’s call_history.
   
    def call(self, other_phone):
        call_string = f'{self.number} called {other_phone.number}.'
        print(call_string)
        self.call_history.append(call_string)
        other_phone.call_history.append(call_string) 
#     Add a method called show_call_history. This method should print the call_history.

    def show_call_history(self):
        print(self.call_history)


#     Add another attribute called messages to your __init__() method which value is an empty list.

#     Create a method called send_message which is similar to the call method. Each message should be saved as a dictionary with the following keys:
#         to : the number of another Phone object
#         from : your phone number (also a Phone object)
#         content
    def send_message(self, recipient, content):
        message = {'to': recipient.number, 'from': self.number, 'content': content}
        self.messages.append(message)
        recipient.messages.append(message)
#     Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self)
    def show_outgoing_messages(self):
        for message in self.messages:
            if message['from'] == self.number:
                print(message)
    
    def show_incoming_messages(self):
        for message in self.messages:
            if message['to'] == self.number:
                print(message)
    def show_messages_from(self, number):
        for message in self.messages:
            if message['from'] == number:
                print(message)
        
phone1 = Phone('0506666071')
phone2 = Phone('0589993232')
phone1.call(phone2)
phone2.call(phone1)
phone1.send_message(phone2, 'Hey!')
phone2.send_message(phone1, "Good evening!")
phone1.show_call_history()
phone2.show_call_history()
phone1.show_incoming_messages()
phone2.show_incoming_messages()
#     Test your code !!!