from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# BMR 계산 함수
def calculate_bmr(gender, weight, height, age):
    if gender == "woman":
        return 10 * weight + 6.25 * height - 5 * age - 161
    else:
        return 10 * weight + 6.25 * height - 5 * age + 5

# 운동 시간 계산 함수
def calculate_hours(exercise, days, weight_loss_kg):
    calories_per_hour = {
        "running": 600,
        "cycling": 500,
        "walking": 300,
        "yoga": 200
    }
    calories_to_burn = weight_loss_kg * 7000
    daily_calories_to_burn = calories_to_burn / days

    if exercise not in calories_per_hour:
        return None, f"Error: {exercise} is not a valid exercise option."

    hours_per_day = daily_calories_to_burn / calories_per_hour[exercise]
    return round(hours_per_day, 2), daily_calories_to_burn

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        age = int(request.form.get("age"))
        weight = float(request.form.get("weight"))
        height = float(request.form.get("height"))
        gender = request.form.get("gender")

        bmr = calculate_bmr(gender, weight, height, age)
        return redirect(url_for("plan_form", bmr=bmr))

    return render_template("index.html")

@app.route("/plan_form", methods=["GET", "POST"])
def plan_form():
    bmr = float(request.args.get("bmr"))

    if request.method == "POST":
        exercise = request.form.get("exercise")
        days = int(request.form.get("duration"))
        weight_loss_kg = float(request.form.get("weight"))

        hours_per_day, daily_calories_to_burn = calculate_hours(exercise, days, weight_loss_kg)

        if bmr < daily_calories_to_burn:
            return render_template("confirm_schedule.html", bmr=bmr, daily_calories_to_burn=daily_calories_to_burn, 
                                   exercise=exercise, days=days, weight_loss_kg=weight_loss_kg, hours_per_day=hours_per_day)
        else:
            message = f"If you want to lose {weight_loss_kg}kg in {days} days by {exercise}, you have to do it for {hours_per_day} hours a day."
            return render_template("schedule_result.html", message=message)

    return render_template("plan_form.html", bmr=bmr)

@app.route("/confirm_schedule", methods=["POST"])
def confirm_schedule():
    choice = request.form.get("choice")
    exercise = request.form.get("exercise")
    days = int(request.form.get("days"))
    weight_loss_kg = float(request.form.get("weight_loss_kg"))
    hours_per_day = float(request.form.get("hours_per_day"))

    if choice == "yes":
        message = f"If you want to lose {weight_loss_kg}kg in {days} days by {exercise}, you have to do it for {hours_per_day} hours a day."
        return render_template("schedule_result.html", message=message)
    else:
        return redirect(url_for("plan_form"))

if __name__ == "__main__":
    app.run(debug=True)
