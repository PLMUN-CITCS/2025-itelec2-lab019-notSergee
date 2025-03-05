def get_student_score() -> float:
    """
    Handles user input to obtain the student's score.

    Returns:
        float: The numerical score entered by the user.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Error: Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Please enter a numerical score.")


def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score and grading scale.

    Args:
        score (float): The numerical score of the student.

    Returns:
        str: The corresponding letter grade.
    """
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


def main():
    """
    Main function that executes the program flow.
    """
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"\nYour Grade is: {grade}")

    # Notable Observations
    print("\nNotable Observations:")
    print("1. Function Decomposition: The problem is divided into two distinct functions (get_student_score and calculate_grade), promoting modularity and code reusability.")
    print("2. Data Flow: The get_student_score function handles user input and returns a numerical score, which is then passed as an argument to the calculate_grade function. The calculated grade is returned and used for the final output.")
    print("3. Conditional Logic: The calculate_grade function uses if, elif, and else statements to determine the correct grade based on the provided score and the grading scale.")

    # Python Best Practices
    print("\nPython Best Practices:")
    print("1. Meaningful Function and Variable Names: Use descriptive names that clearly indicate the purpose of functions and variables (e.g., get_student_score, calculate_grade, score).")
    print("2. Docstrings: Included for each function to explain its purpose, parameters, and return value.")
    print("3. Type Hints: Used to indicate expected data types for function parameters and return values.")
    print("4. Input Validation: Ensures the user enters a valid numerical score between 0 and 100.")
    print("5. Testing: The program should be tested with various inputs (including edge cases and invalid input) to ensure it functions correctly.")


if __name__ == "__main__":
    main()
