# Function to determine grade based on score
def get_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Get user input
try:
    score = float(input("Enter your score: "))
    if 0 <= score <= 100:
        grade = get_grade(score)
        print(f"Your Grade is: {grade}")
    else:
        print("Please enter a valid score between 0 and 100.")
except ValueError:
    print("Invalid input! Please enter a numeric value.")
