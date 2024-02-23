from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'shhh, this is a secret to share with anyone' # set a secret key for security purposes


#* VIEW ROUTE
@app.route("/form")
def display_form():
    
    return render_template("form.html")

#? ACTION ROUTE
@app.route("/process", methods=['POST'])
def process_payment():
    # print("="*60)
    # print(request.form)
    print("="*60)
    # print(request.form["full_name"])
    # print(request.form["card"])
    # print(request.form["amount"])
   
    #? setting up the session
    session["username"] = request.form["full_name"]
    # session["card_number"] = request.form["card"]
    session["amount"] = request.form["amount"]

    # print(f"You just payed {amount} $$$")
    #! NEVER EVER EVER RENDER ON POST REQUEST
    return redirect("/success")

#* VIEW ROUTE
@app.route("/success")
def success():
   
    return render_template("success.html")

#* Clear Session Route
@app.route("/clear")
def clear_session():
    # session.pop("username")
    session.clear()
    return redirect("/success")




if __name__ == "__main__":
    app.run(debug=True)
