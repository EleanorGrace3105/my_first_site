from flask import Flask

app = Flask ("MyApp")

@app.route("/")
def hello():
	return "Hello Eleanor!"


@app.route("/idontexist")
def idontexist():
	return "I do exist now!"


app.run (debug = True)

