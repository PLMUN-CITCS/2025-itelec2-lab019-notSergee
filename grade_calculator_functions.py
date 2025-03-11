def get_student_score() -> float:
    """Prompts the user to input their score and returns the score as a float."""
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:  # Score must be between 0 and 100
                return score
            else:
                print("Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_grade(score: float) -> str:
    """Calculates the grade based on the score."""
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def main():
    """Main function to run the grade calculator."""
    score = get_student_score()  # Get the student's score
    grade = calculate_grade(score)  # Calculate the grade
    print(f"Your Grade is: {grade}")  # Output the grade

# Run the main program
if __name__ == "__main__":
    main()
