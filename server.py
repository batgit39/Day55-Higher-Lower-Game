import random
from flask import Flask

random_number = random.randint(0,9)
print(random_number)

app = Flask(__name__)

def make_header(function):
    def wraper_function():
        return f"<h1>{function()}</h1>"
    return wraper_function

@app.route('/')
def hello_world():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"

@app.route("/<int:users_guess>")
def guess_the_number(users_guess):
    if users_guess > random_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
                "<img src='https://media.giphy.com/media/3og0IuWMpDm2PdTL8s/giphy.gif'/>"

    elif users_guess < random_number:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
                "<img src='https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
                "<img src='https://media.giphy.com/media/QyK8gRzGW2fV6qo8Hm/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug = True)
