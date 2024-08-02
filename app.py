from flask import Flask,render_template,request
from datetime import datetime, timedelta

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
        current_hours = int(request.form["current_hours"])
        current_minutes = int(request.form["current_minutes"])
        hours_to_wait = int(request.form["hours_to_wait"])
        minutes_to_wait = int(request.form["minutes_to_wait"])
    
       # Create a datetime object with current hours and minutes
        now = datetime.now().replace(hour = current_hours,minute=current_minutes, second=0, microsecond=0)
        wait_time = timedelta(hours=hours_to_wait ,minutes=minutes_to_wait)

        # Calculate the alarm time
        alarm_time = now + wait_time
    
        # Format the alarm time in 24-hour format
        alarm_time_str = alarm_time.strftime("%H : %M")

        
        return render_template("alarm.html",current_hours=current_hours,current_minutes=current_minutes,hours_to_wait=hours_to_wait,minutes_to_wait= minutes_to_wait,
                               alarm_time = alarm_time_str,title="Alarm")
    
    return render_template("alarm.html",alarm_time = None,title="Alarm")

if __name__=="__main__":
    app.run(debug=True)

