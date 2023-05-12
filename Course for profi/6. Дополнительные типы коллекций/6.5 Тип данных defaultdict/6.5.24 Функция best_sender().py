from collections import defaultdict


def best_sender(messages: list, senders: list) -> str:
    ddict = defaultdict(int)
    for sender, message in zip(senders, messages):
        ddict[sender] += len(message.split())
    return sorted(ddict, key=lambda x: (ddict.get(x), x))[-1]


# messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
# senders = ['Sam Fisher', 'Linda', 'Sam Fisher']
#
# print(best_sender(messages, senders))
