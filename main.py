# We are cooked

with open("save.txt", "r") as saveFile:
    if saveFile.read() == False:
        print("Hi! What\'s your name?")

def inputtingChat():
    userInput = input()
    
    with open("save.txt", "a") as saveFile:
        saveFile.write(f"User: {userInput}")
