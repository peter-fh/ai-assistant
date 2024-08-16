from openai import OpenAI
import os
import prompts

def ask(question, conversation=False, example_response=False):
    if example_response:
        with open("example_response.txt") as f:
            return f.read()

    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


    prompt = prompts.getPrompt(conversation)
    print("Sending the following query:")
    print(prompt)
    print(question)
    completion = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {
                "role": "system", 
                "content": prompt
            },

        {
                "role": "user", 
                "content": question
            }
      ]
    )
    msg = str(completion.choices[0].message.content)

    if conversation:
        with open("conversation.txt", 'a') as f:
            f.write("\nUSER MESSAGE:\n")
            f.write(question)
            f.write("\nAI RESPONSE:\n")
            f.write(msg)


    return msg

if __name__ == "__main__":
    inp = input()
    print(ask(inp))
