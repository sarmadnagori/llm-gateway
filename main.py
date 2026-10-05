def add_turn(history, text):
    history.append({"role": "user", "content": text})   # writes ON the board
    return history                                     # hands back the SAME board


# ---- Version 1: the broken "backup" ----
conversation = [{"role": "system", "content": "be brief"}]
backup = conversation                     # second note, same board

print(backup is conversation)             # True  -> same object
print(id(backup) == id(conversation))     # True  -> same address in memory

conversation = add_turn(conversation, "hi")

print(len(conversation))                  # 2
print(len(backup))                        # 2   <- backup changed too
print(backup is conversation)             # True  -> still one board


# ---- Version 2: a real backup ----
conversation = [{"role": "system", "content": "be brief"}]
backup = conversation.copy()              # new board, same contents

print(backup is conversation)             # False -> two objects

conversation = add_turn(conversation, "hi")

print(len(conversation))                  # 2
print(len(backup))                        # 1   <- backup kept the old state