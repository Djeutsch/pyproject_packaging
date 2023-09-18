from datetime import datetime

class AgeCalculator:
    """
    This program calculates a person's age based on their date of birth and return the day of the week they were born. 
    """
    def __init__(self, date_of_birth):
        self.date_of_birth = date_of_birth

    def calculate_age(self):
        # Get the current date
        current_date = datetime.now()
        
        # Calculate the age
        age = current_date.year - self.date_of_birth.year - ((current_date.month, current_date.day) < (self.date_of_birth.month, self.date_of_birth.day))
        
        return age

    def day_of_week(self):
        # Get the day of the week as an integer (0 = Monday, 6 = Sunday)
        day_index = self.date_of_birth.weekday()

        # Define a list of days of the week
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Get the day of the week as a string
        day_name = days_of_week[day_index]

        return day_name

if __name__ == "__main__":
    # Input date of birth in the format 'YYYY-MM-DD'
    date_of_birth_str = input("Enter your date of birth (YYYY-MM-DD): ")

    try:
        # Convert the input string to a datetime object
        date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d')

        # Create an instance of the AgeCalculator class
        calculator = AgeCalculator(date_of_birth)

        # Calculate age and day of the week
        age = calculator.calculate_age()
        day_name = calculator.day_of_week()

        print(f"You are {age} years old.")
        print(f"You were born on a {day_name}.")
    except ValueError:
        print("Invalid date of birth format. Please use 'YYYY-MM-DD'.")

