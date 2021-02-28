class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def sent(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

command = input()
while not command == "Stop":
    sender, receiver, content = command.split(" ")
    email = Email(sender, receiver, content)
    emails.append(email)

    command = input()

send_email = [int(index) for index in input().split(", ")]

for i in send_email:
    emails[i].sent()

for mail in emails:
    print(mail.get_info())



