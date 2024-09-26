import openai



client = openai.OpenAI(api_key="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")
openai.api_key = "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"


# function that takes in string argument as parameter
def comp(PROMPT, MaxToken=50, outputs=3):
    # using OpenAI's Completion module that helps execute 
    # any tasks involving text 
    response = openai.Completion.create(
        # model name used here is text-davinci-003
        # there are many other models available under the 
        # umbrella of GPT-3
        model="text-davinci-002",
        # passing the user input 
        prompt=PROMPT,
        # generated output can have "max_tokens" number of tokens 
        max_tokens=MaxToken,
        # number of outputs generated in one call
        n=outputs
    )
    # creating a list to store all the outputs
    output = list()
    for k in response['choices']:
        output.append(k['text'].strip())
    return output


def inputtingChat():
    userInput = input()
    response = comp(userInput)
    print(response)
    with open("save.txt", "a") as saveFile:
        saveFile.write(f"User: {userInput}\nResponse: {response}")
    inputtingChat()
    

with open("save.txt", "r") as saveFile:
    if saveFile.read() == False:
        print("Hi! What\'s your name?")
    else:
        print("Welcome back!")
    inputtingChat()