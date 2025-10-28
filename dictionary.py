# Initial data: names and their scores
scores = {'Alice': 88, 'Bob': 92, 'Charlie': 79, 'David': 95, 'Eve': 84}

# Create a new dictionary containing only passing scores (>= 85)
# and convert the names to uppercase.
passing_students = {
    name.upper(): score
    for name, score in scores.items()
    if score >= 85
}

print("Original Scores:", scores)
print("Passing Students (filtered and transformed):")
for name, score in passing_students.items():
    print(f"{name}: {score}")
