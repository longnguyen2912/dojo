from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/index1', methods=['POST'])
def index1():
    yourName = request.form["yourName"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    return render_template("index2.html", yourName=yourName, location=location, language=language, comment=comment)
@app.route('/index2')
def index2():
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
