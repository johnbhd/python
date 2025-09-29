#num classifier
num = int(input("Enter an integer: "))

if num > 0:
    print(f"The number {num} is positive.")
else:
    print(f"The number {num} is zero or negative.")

#num odd even
num = int(input("Enter an integer: "))

print(f"The number {num} is {'even' if num % 2 == 0 else 'odd'}.")

# age classifier
age = int(input("Enter your age: "))

print(f"You are a{'n Adult' if age >= 18 else ' Kid'}.")

# age vote eligible
age = int(input("Enter your age: "))

print(f"You are {'eligible to vote.' if age >= 18 else 'not eligible to vote yet.'}")

# score pass exam
score = int(input("Enter your exam score: "))

print(f"You {'passed' if score >= 60 else 'did not pass'} the exam.")
