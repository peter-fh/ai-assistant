import json
import os

prompt = open("prompt.txt").read()
token_usage = 0

def resetConversation():
    os.remove("conversation.txt")


def getPrompt(conversation=False):
    global token_usage
    return_prompt = prompt
    if conversation:
        try:
            with open("conversation.txt") as f:
                previous_conversation = f.read()
                token_usage = len(previous_conversation) / 4
                return_prompt = prompt + previous_conversation
        except:
            return return_prompt
    return return_prompt 

