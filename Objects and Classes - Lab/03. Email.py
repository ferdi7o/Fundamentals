class Email():

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

informacion = []
data = input()

while data != "Stop":
    senders, receiver, content = data.split()
    email = Email(senders, receiver, content)
    informacion.append(email)

    data = input()

indexes = [int(el) for el in input().split(", ")]

for index, email in enumerate(informacion):
    if index in indexes:
        informacion[index].send()
    print(f'{email.sender} says to {email.receiver}: {email.content}. Sent: {email.is_sent}')