from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",title="Home")

@app.route("/meal",methods = ["GET","POST"])
def meal():
    if request.method == "POST":
        try:
            food_charge = float(request.form["food_charge"])
            tip = food_charge * 0.18
            sales_tax = food_charge * 0.07
            total_amount = food_charge + tip + sales_tax
        except ValueError:
            food_charge=tip=sales_tax=total_amount=None
    else:
        food_charge=tip=sales_tax=total_amount=None
    return render_template("meal.html",food_charge = food_charge,tip=tip,sales_tax=sales_tax,total_amount=total_amount,title="Meal")

@app.route("/alarm",methods = ["GET","POST"])
def alarm():
    if request.method == "POST":
        current_time = int(request.form["current_time"])
        hours_to_wait = int(request.form["hours_to_wait"])
        alarm_time = (current_time + hours_to_wait) % 24
        period = 'AM' if 0<=alarm_time < 12 else 'PM'
        return render_template("alarm.html",current_time=current_time,hours_to_wait=hours_to_wait,alarm_time=alarm_time,title="Alarm",period=period)
    return render_template("alarm.html",alarm_time = None,title="Alarm")

if __name__=="__main__":
    app.run(debug=True)

