### Progressive Over-Acheiving

# A Gym Progress Tracker designed to highlight best achievements in the gym and keep you pushing to break records

# Main App Goals
- Different Tabs
    - Create a Workout
    - Workout History
    - Exercises
    - General Exercise Tips
        - What is Progressive Overloading?
        - Importance of proper form
        - Tips for motivation
        - Etc.
- The biggest feature will include 'Milestones/Records"
    - The highest amount of weight used in a workout
    - Highest amount of weight used in a workout with 6+ reps
- Incentive feature for beating records
    - Stretch Goal - The BigCoin - a fake currency that is gifted to your account everytime you break a previous record. BigCoins can also be rewarded for other random events.

# Tech to Be Used
- Django
- Python
- SQL

# Exercises Model
- Exercises will be the main data used for the app. An exercise will be defined as a gym-movement
- An exercise model will be made up of:
    - Name (str)
    - Sets (int)
    - Reps (int)
    - Weight (int)

# Workout Model
- This will be a broader model for keeping track of a users exercises done on a specific day
- When a user wants to create a workout, they will fill out a form about the exercises done that day
- Upon finishing the workout form, it will be appended to a workout history section
- A workout model will be made up of:
    - Name (str)
    - Date (date, auto-generated to current date but changeable)
    - Exercises (arr, containing any number of exercise models)

# User Authentication
- It is necesary that each user will have their own individual account to keep track of own workouts
- So far, it is unclear how I will do that using Django framworks
- It is also unclear how I will associate a User Model with Workouts

# User Model (Subject to Change)
- A user model will be made up of 
    - Name (str)
    - Gender (str)
    - Age (int)
    - DOB (date)
    - Email/Username ? (str)
    - Password ? (str)

# Stretch -- BigCoin Model/Variable
- This is a useless fake currency that would be attached to a user
- Balance of this fake currency will be able to be seen in the header
- Hopefully users will get dopamine hits when seeing the imaginary currency go up
- A BigCoin model will be made up of:
    - Number of Coins (int)
