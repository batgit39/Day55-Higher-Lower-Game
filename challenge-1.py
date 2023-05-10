from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wraper_function():
        return f"<b>{function()}</b>"
    return wraper_function

def make_emphasis(function):
    def wraper_function():
        return f"<em>{function()}</em>"
    return wraper_function

def make_underlined(function):
    def wraper_function():
        return f"<u>{function()}</u>"
    return wraper_function

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run(debug = True)
