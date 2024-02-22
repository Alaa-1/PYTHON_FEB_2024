from flask import Flask, render_template # import the class Flask

app = Flask(__name__) # create an instance from the class

# Create a Route

@app.route("/")
def index():
    return "You have arrived ! 👏"


@app.route("/home")
def home():
    full_name = "James Bond"
    return render_template("home.html", username = full_name, age=25)

@app.route("/home/<name>/<int:age>/<fav_color>")
def custom_home(name, age,fav_color):
    return render_template("custom_home.html", name = name, age = age, color = fav_color )

@app.route("/list")
def show_list():
    zoo = [
        {"name": "🐱", "number": 3},
        {"name": "🦁", "number": 1},
        {"name": "🦓", "number": 8},
        {"name": "🐘", "number": 2},
    ]

    return render_template("zoo.html", animals = zoo)

if(__name__ == "__main__"):
    app.run(debug=True)

