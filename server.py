from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'aKey'

@app.route('/')
def index():
    if "gold" not in session:
        session["gold"] = 0
    if "log" not in session:
        session["log"] = []

    return render_template("index.html", gold = session['gold'], log = session['log'])

@app.route('/process', methods =["GET", 'POST'])
def result():
    
    if request.form['action'] == "farm":
        pay = random.randint(10,20)
        session['gold'] += pay
        session['log'].append("{} from farm".format(int(pay)))
    elif request.form['action'] == "cave":
        pay = random.randint(5,10)
        session['gold'] += pay
        session['log'].append("{} from cave".format(int(pay)))
    elif request.form['action'] == "house":
        pay = random.randint(2,5)
        session['gold'] += pay
        session['log'].append("{} from house".format(int(pay)))
    elif request.form['action'] == "casino":
        pay = random.randint(-50,50)
        session['gold'] += pay
        session['log'].append("{} from casino".format(int(pay)))
    elif request.form['action'] == "reset":
        session['gold'] = 0
        session['log'] = []

    return redirect('/')

    

app.run(debug=True)