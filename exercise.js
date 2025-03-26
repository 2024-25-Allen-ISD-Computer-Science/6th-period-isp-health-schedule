function generateWorkout() {
    // assigning variables
    const level = document.getElementById("fitnessLevel").value;
    const goal = document.getElementById("goal").value;
    const time = document.getElementById("time").value;
    
    // assigns proper wording to the camel-cased placeholders
    let goalText = "";
    if (goal === "weightLoss") goalText = "Weight Loss";
    else if (goal === "muscleGain") goalText = "Muscle Gain";
    else if (goal === "endurance") goalText = "Endurance";
    let workout = "";
    
    // determining the exercises to assign based on time given
    
    if (goal === "weightLoss") {
        if (time == 15) {
            workout = "Jump Rope, Squats, Push-ups";
        } else {
            workout = "Jump Rope, Lunges, Burpees, Plank";
        }
    } else if (goal === "muscleGain") {
        if (time == 15) {
            workout = "Dumbbell Squats, Push-ups";
        } else {
            workout = "Deadlifts, Pull-ups, Bench Press";
        }
    } else {
        if (time == 15) {
            workout = "Jogging, Jump Squats";
        } else {
            workout = "Running, Cycling, Plank Holds";
        }
    }
    
    // retreiving the elements and outputting the result
    document.getElementById("workoutPlan").innerHTML = `<h3>Your Workout Plan:</h3>
    <p>Level: ${level.charAt(0).toUpperCase() + level.slice(1)}</p>
    <p>Goal: ${goalText}</p>
    <p>Exercises: ${workout}</p>`;}