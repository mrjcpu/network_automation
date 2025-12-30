unsent_messages = [
    'hey there mamasita!',
    'well what do you know?',
    'yahoooooo!'
]
sent_messages = []

def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Message sending: {current_message}")
        sent_messages.append(current_message.title())

def show_sent_messages(sent_messages):
    print("\nSent messages:")
    for sent_message in sent_messages:
        print(sent_message)

send_messages(unsent_messages, sent_messages)
show_sent_messages(sent_messages)
