import json
import os

prompt = open("prompt.txt").read()

def resetConversation():
    os.remove("conversation.txt")


def getPrompt(conversation=False):
    return_prompt = prompt
    if conversation:
        try:
            with open("conversation.txt") as f:
                return_prompt = prompt + f.read()
        except:
            print("cant find conversation.txt")
            return return_prompt
    return return_prompt 

