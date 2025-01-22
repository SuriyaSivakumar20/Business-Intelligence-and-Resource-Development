from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

class Chatbot:
    def __init__(self):
        self.role = None
        self.score = 0
        self.responses = []
        self.questions_vc = [
            "What industries are you most interested in? 🌟",
            "How many companies have you invested in so far?",
            "What's your biggest success story as a VC? 🚀",
            "Do you prefer seed or growth-stage investments?"
        ]
        self.questions_startup = [
            "What's your startup idea? 💡",
            "How are you preparing your product for launch?",
            "What challenges are you facing as a startup founder? 🤔",
            "How do you plan to scale your business?"
        ]

    def handle_input(self, user_message):
        response = ""

        if self.role is None:
            self.role = user_message.lower()
            if self.role in ["vc", "venture capitalist"]:
                question = random.choice(self.questions_vc)
                response = f"Great! Let's discuss your experience as a VC. {question}"
            elif self.role in ["startup", "startup company head"]:
                question = random.choice(self.questions_startup)
                response = f"Awesome! Let's talk about your startup. {question}"
            else:
                response = "Are you a VC or a Startup company head? 🤷"
                self.role = None
        else:
            self.responses.append(user_message)
            self.score += random.randint(1, 4)  # Random scoring for responses

            if self.role in ["vc", "venture capitalist"]:
                question = random.choice(self.questions_vc)
            else:
                question = random.choice(self.questions_startup)

            if len(self.responses) < 3:  # Limit questions to 3
                response = f"{question}"
            else:
                response = f"Thanks for your responses! Your score is {self.score} out of 10. "
                if self.score > 7:
                    response += "🎉 You're eligible to create a profile on our platform!"
                else:
                    response += "😔 Unfortunately, you didn't meet the eligibility criteria."
                self.reset_chatbot()

        return response

    def reset_chatbot(self):
        self.role = None
        self.score = 0
        self.responses = []

chatbot = Chatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form['message']
    bot_response = chatbot.handle_input(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
