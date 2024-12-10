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
    return round(hours_per_day, 2), None