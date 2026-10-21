
# Program 7: Functional Data Filtering & Matrix Transformation Suite

# Input matrix
matrix = [
    [4, -2, 7],
    [9, 3, -5],
    [6, -1, 8]
]

print("Original Matrix:")
for row in matrix:
    print(row)

# 1. Filter out negative numbers using filter() and lambda
filtered_matrix = list(
    map(lambda row: list(filter(lambda x: x >= 0, row)), matrix)
)

print("\nMatrix after removing negative numbers:")
for row in filtered_matrix:
    print(row)

# 2. Square each element using map() and lambda
squared_matrix = list(
    map(lambda row: list(map(lambda x: x**2, row)), filtered_matrix)
)

print("\nMatrix after squaring elements:")
for row in squared_matrix:
    print(row)

# 3. Sort each row in ascending order using sorted()
sorted_matrix = list(
    map(lambda row: sorted(row), filtered_matrix)
)

print("\nMatrix after sorting each row:")
for row in sorted_matrix:
    print(row)

# 4. Sort tuples using a custom key
data = [(3, 50), (1, 80), (2, 60), (4, 40)]

sorted_data = sorted(data, key=lambda x: x[1])

print("\nTuples sorted by second element:")
print(sorted_data)
