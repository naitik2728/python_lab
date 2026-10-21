
# Program 8: Student Grade and Statistics Calculator

def calculate_statistics(*args, **kwargs):
    # Combine all assessment grades
    grades = list(args)

    # Add grades passed through keyword arguments
    grades.extend(kwargs.values())

    if not grades:
        return 0, 0, 0, {}

    # Calculate minimum, maximum, and average
    minimum = min(grades)
    maximum = max(grades)
    average = sum(grades) / len(grades)

    # Calculate letter grade distribution
    distribution = {
        "A": 0, "B": 0, "C": 0, "D": 0, "F": 0
    }

    for grade in grades:
        if grade >= 90:
            distribution["A"] += 1
        elif grade >= 80:
            distribution["B"] += 1
        elif grade >= 70:
            distribution["C"] += 1
        elif grade >= 60:
            distribution["D"] += 1
        else:
            distribution["F"] += 1

    return minimum, maximum, average, distribution


# Calling the function using *args and **kwargs
minimum, maximum, average, distribution = calculate_statistics(
    85, 92, 76, 58,
    quiz=88,
    assignment=95
)

# Display results
print("Minimum Grade:", minimum)
print("Maximum Grade:", maximum)
print("Average Grade:", round(average, 2))
print("Letter Grade Distribution:")

for grade, count in distribution.items():
    print(grade, ":", count)
