def main():
    try:
        score = float(input("Enter your score: "))
        if 0 <= score <= 100:
            if score >= 90:
                grade = 'A'
            elif score >= 80:
                grade = 'B'  # Corrected 'grede' to 'grade'
            elif score >= 70:
                grade = 'C'
            elif score >= 60:
                grade = 'D'
            else:
                grade = 'F'
            print(f"Your Grade is: {grade}")
        else:
            print("Please enter a valid score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
