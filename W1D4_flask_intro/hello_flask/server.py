from flask import Flask, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)  # Create a new instance of the Flask class called "app"


@app.route(
    "/"
)  # The "@" decorator associates this route with the function immediately following
def hello_world():
    return "Hello World!"  # Return the string 'Hello World!' as a response

# @app.route("/dashboard")
# def dash():
#     return "<script>alert('Please dont do this ❌')</script>"

@app.route(
    "/about"
)  # The "@" decorator associates this route with the function immediately following
def hello():
    return "This is a simple flask application!"  # Return the string 'Hello World!' as a response


@app.route("/profile/<username>")
def profile(username):
    return f"Welcome {username} to your profile"


@app.route("/profile/<username>/<int:multiply>")
def multiple_times(username, multiply):
    return f"Welcome {username} to your profile"*multiply


# @app.route("/profile/<username>/<multiply>")
# def multiple_times2(username, multiply):
#     return f"Welcome {username} to your profile {multiply}"

@app.route("/hello_template")
def cool():
    return render_template("about.html");


if (
    __name__ == "__main__"
):  # Ensure this file is being run directly and not from a different module
    app.run(debug=True)  # Run the app in debug mode.
