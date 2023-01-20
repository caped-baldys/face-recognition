from flask import Flask , render_template

app = Flask(__name__)

print("Give your name")
name = input()

@app.route('/')

def home():
    return render_template("home.html",name1 = name)

app.run(debug=True)
