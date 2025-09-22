from flask import Flask, request, render_template
import gpt
import prompts

# TODO: add an "assume no previous knowledge of {concepts}" to prompt
# TODO: brevity dropdown
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/question/', methods=['POST'])
def question():

    if request.method == 'POST':

        # Message is valid length, get data and request gpt response
        data = request.get_json()
        message = data["text"]
        gpt_response = gpt.ask(message, conversation=True,example_response=False)

        print("Conversation has %d tokens" % (prompts.token_usage / 4))
        return gpt_response

    # Reject non-POST requests (flask should handle this regardless)
    return "Invalid request type", 400


@app.route('/reset/', methods=['GET'])
def reset():
    prompts.resetConversation()
    prompts.token_usage = 0
    return "", 200

if __name__ == '__main__':
    app.run(port=8070, debug=True)
