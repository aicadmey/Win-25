def greetings():
    print("\nHi! I am Raymax, apka apna personal healthcare Robot (inspired from Baymax).")
    print("How are you feeling today?\n")
    
    # User input for their mood
    user_response = input("Please tell me: (e.g.yes I am fine, no i am not fine, etc.): ").lower()
    
    if "yes" in user_response:
        print("That's great to hear! I hope you stay healthy and happy.")
    else:
        print("I hope you would be fine soon. Remember, seeking help is always a good option.")
    
    # Ask if the user needs help
    print("-" * 50)
    print("Do you need any assistance from me today?")
    print("Type '1' for Yes or '0' for No.\n")
    help_choice = input("Your choice: ")
    
    if help_choice == "1":
        print("Great! Let's get started. Here's what I can do for you:\n")
        main_menu()  # Proceed to the main menu
    else:
        print("Goodbye! Take care of yourself. Stay safe and healthy!")

# Main menu
def main_menu():
    
        print("Please choose what care u need:\n")
        print("1. BMI Calculator - To know your Body Mass Index and focus on weight loss or gain.")
        print("2. Water Intake Recommendation - To prevent dehydration by knowing daily water needs.")
        print("3. Calorie Needs Estimation - To manage weight by estimating your daily calorie intake.")
        print("4. Basic Symptom Checker - To check for common symptoms and possible suggestions.")
        print("5. Heart Rate Checker - To monitor your heart health.")
        print("6. Exercise Suggestions - To get exercise ideas based on your fitness level.")
        print("7. Sleep Tracker - To analyze your sleep patterns and improve rest quality.")
        print("8. Mental Health Tips - To receive suggestions for mental well-being.")
        print("9. Medicine Suggestion System - To get information about common medicines.")
        print("10. Basic First Aid Guide - To know how to handle minor injuries and emergencies.")
        print("0. Exit - To leave Raymax's assistance.\n")
        
        choice = input("Enter your choice (0-10): ").strip()

        if choice == "0":
            print("Goodbye! Stay healthy!\n")
            
        elif choice == "1":
            bmi_calculator()
        elif choice == "2":
            water_intake_recommendation()
        elif choice == "3":
            calorie_needs_estimation()
        elif choice == "4":
            basic_symptom_checker()
        elif choice == "5":
            heart_rate_checker()
        elif choice == "6":
            exercise_suggestions()
        elif choice == "7":
            sleep_tracker()
        elif choice == "8":
            mental_health_tips()
        elif choice == "9":
            medicine_suggestion_system()
        elif choice == "10":
            first_aid_guide()
        else:
            print("Invalid choice. Please enter a valid number between 0 and 10.\n")
        print("-" * 50)

# 1. BMI Calculator
def bmi_calculator():
    print("\n--- BMI Calculator ---")
    weight = float(input("Please enter your weight in kilograms: "))
    height = float(input("Please enter your height in meters: "))
    
    # Calculate BMI
    bmi = weight / (height ** 2)
    
    # Print result
    print(f"Your BMI is: {bmi:.2f}") # .2f round off krny kai liye use kia hai
    
    # Provide health feedback based on BMI
    if bmi < 18.5:
        print("You are underweight. Consider consulting a nutritionist for advice.")
    elif 18.5 <= bmi < 24.9:
        print("You have a healthy weight. Keep up the good work!")
    elif 25 <= bmi < 29.9:
        print("You are overweight. Consider adopting a healthier diet and exercise routine.")
    else:
        print("You are obese. It's important to consult a healthcare provider for advice.")

# 2. Water Intake Recommendation
def water_intake_recommendation():
    print("\n--- Water Intake Recommendation ---")
    weight = float(input("Please enter your weight in kilograms: "))
    
    # Recommended water intake is around 35ml per kg of body weight
    water_intake = weight * 35  # In milliliters
    
    print(f"Your recommended daily water intake is: {water_intake / 1000:.2f} liters.") 

# 3. Calorie Needs Estimation
def calorie_needs_estimation():
    print("\n--- Calorie Needs Estimation ---")
    
    # Getting user details
    gender = input("Please enter your gender (Male/Female): ").lower()
    age = int(input("Please enter your age in years: "))
    weight = float(input("Please enter your weight in kilograms: "))
    height = float(input("Please enter your height in centimeters: "))
    
    # Calculate BMR using Mifflin-St Jeor equation
    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161
    
    # Estimating total calorie needs based on activity level
    activity_level = input("Enter your activity level (Sedentary, Light, Moderate, Active, Very Active): ").lower()
    
    if activity_level == "sedentary":
        total_calories = bmr * 1.2
    elif activity_level == "light":
        total_calories = bmr * 1.375
    elif activity_level == "moderate":
        total_calories = bmr * 1.55
    elif activity_level == "active":
        total_calories = bmr * 1.725
    elif activity_level == "very active":
        total_calories = bmr * 1.9
    else:
        print("Invalid activity level. Please try again.")
        return
    
    print(f"Your estimated daily calorie needs are: {total_calories:.2f} calories.")

# 4. Basic Symptom Checker
def basic_symptom_checker():
    print("\n--- Basic Symptom Checker ---")
    symptom = input("Please describe your symptom (e.g., headache, fever, cough): ").lower()
    
    if "headache" in symptom:
        print("You may have a headache. Try resting, staying hydrated, and avoiding screens.")
    elif "fever" in symptom:
        print("You may have a fever. Rest, stay hydrated, and monitor your temperature. If it persists, see a doctor.")
    elif "cough" in symptom:
        print("You may have a cough. Stay hydrated and consider using cough syrup if needed. Seek medical advice if necessary.")
    else:
        print("Your symptom is not recognized. If you're concerned, please consult a healthcare provider.")

# 5. Heart Rate Checker
def heart_rate_checker():
    print("\n--- Heart Rate Checker ---")
    heart_rate = int(input("Please enter your heart rate (beats per minute): "))
    
    if heart_rate < 60:
        print("Your heart rate is below normal. Please consult a healthcare provider.")
    elif 60 <= heart_rate <= 100:
        print("Your heart rate is within the normal range. Keep up the good health!")
    else:
        print("Your heart rate is above normal, Attack Risks .You may want to consult a doctor.")

# 6. Exercise Suggestions
def exercise_suggestions():
    print("\n--- Exercise Suggestions ---")
    fitness_level = input("Enter your fitness level (Beginner, Intermediate, Advanced): ").lower()
    
    if fitness_level == "beginner":
        print("Suggestions: Start with walking, light jogging, or basic bodyweight exercises.")
    elif fitness_level == "intermediate":
        print("Suggestions: Try moderate running, cycling, or resistance training.")
    elif fitness_level == "advanced":
        print("Suggestions: High-intensity interval training (HIIT), heavy weightlifting, or endurance sports.")
    else:
        print("Invalid fitness level. Please choose from Beginner, Intermediate, or Advanced.")

# 7. Sleep Tracker
def sleep_tracker():
    print("\n--- Sleep Tracker ---")
    sleep_hours = float(input("How many hours did you sleep last night? "))
    
    if sleep_hours < 6:
        print("You are getting less sleep than recommended. Try to get at least 7-9 hours of sleep for better health.")
    elif 6 <= sleep_hours <= 9:
        print("You are getting a healthy amount of sleep. Keep it up!")
    else:
        print("You are getting more sleep than usual. Ensure you're not oversleeping, as it can lead to health issues.")

# 8. Mental Health Tips
def mental_health_tips():
    print("\n--- Mental Health Tips ---")
    mood = input("How are you feeling emotionally today? (e.g., stressed, anxious, happy): ").lower()
    
    if "stressed" in mood:
        print("Try relaxation techniques such as deep breathing or meditation to reduce stress.")
    elif "anxious" in mood:
        print("Consider talking to a counselor, or try mindfulness and relaxation practices.")
    elif "happy" in mood:
        print("Great to hear! Keep up the positive vibes.")
    else:
        print("Remember, it's okay to seek help if you're feeling down.")

# 9. Medicine Suggestion System
def medicine_suggestion_system():
    print("\n--- Medicine Suggestion System ---")
    symptom = input("Please describe your symptoms (e.g., headache, cold, fever): ").lower()
    
    if "headache" in symptom:
        print("You can try over-the-counter pain relievers like paracetamol or ibuprofen or painkiller like Paandol.")
    elif "cold" in symptom:
        print("Consider using decongestants or taking warm fluids to relieve symptoms.")
    elif "fever" in symptom:
        print("Consider using cold towel or taking Acetaminophen and ibuprofen  to relieve symptoms.")
    else:
        print("Please consult a healthcare provider for personalized advice.")

# 10. Basic First Aid Guide
def first_aid_guide():
    print("\n--- Basic First Aid Guide ---")
    injury_type = input("Please describe the injury (e.g., cut, burn, sprain): ").lower()
    
    if "cut" in injury_type:
        print("Clean the wound with water, apply antiseptic, and bandage it. Seek medical help if necessary.")
    elif "burn" in injury_type:
        print("Cool the burn with cold water, cover with a clean cloth, and avoid applying ointments.")
    elif "sprain" in injury_type:
        print("Rest the sprained area, apply ice, and elevate it. If needed, seek medical attention.")
    else:
        print("For more serious injuries, contact emergency services immediately.")

# Starting the program
greetings()
