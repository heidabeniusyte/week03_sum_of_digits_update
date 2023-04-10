def sum_of_digits(n):
    if n < 0 or n > 9999999999:
        raise ValueError("Input number must be positive and have at most 10 digits.")
    return sum(int(digit) for digit in str(n))


import csv

with open('test_numbers.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        number = int(row[0])
        try:
            result = sum_of_digits(number)
            print(f"Input number: {number}, Result: {result}")
        except ValueError as e:
            print(f"Input number {number} is invalid: {e}")