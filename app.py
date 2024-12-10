from flask import Flask, render_template, request
from HealthScheduleCalculate import calculate_hours

app = Flask(__name__)

@app.route('/')
def question_page():
    return render_template('questionPage.html')  


@app.route('/HealthScheduleCalculate', methods=['POST'])
def health_schedule_calculate():
    try:
        exercise = request.form.get('exercise')
        days = int(request.form.get('duration'))
        weight_loss_kg = float(request.form.get('weight'))

        
        hours_per_day, error = calculate_hours(exercise, days, weight_loss_kg)

        if error:
            return render_template('resultPage.html', error=error) 

        
        message = f"If you want to lose {weight_loss_kg}kg in {days} days by {exercise}, you have to do it for {hours_per_day} hours a day."
        return render_template('resultPage.html', message=message)  

    except Exception as e:
        return render_template('resultPage.html', error=str(e))  

if __name__ == "__main__":
    app.run(debug=True)