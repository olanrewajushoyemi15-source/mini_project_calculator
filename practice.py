
r = 0
while True:
    i = int(input("Enter number to add(o to stop): "))
    if i == 0:
        break
    r += 1
    print(f"the total number now is {r}")
    print(f"final total is {r}")

# Loop in Python 1 to 10

for i in range(1, 11):
    print(i)

# for loop that print even number of 1 to 20
for i in range(1, 20):
    if i % 2 == 0:
        print(i)

# printing each character in python
program = "Python"
for text in program:
    print(text)

# from 10 to 1
for i in range(10, 0, -1):
    print(i)


# sum of numbers from 1 to 10

sum_of_numbers = 0
for i in range(1, 11):
    sum_of_numbers += i
    print(sum_of_numbers)

# multiplication table of 5
for i in range(1, 13):
    print("5 *", i, "=", 5 * i)

# count how many numbers between 1 and 50 are divisible by 3
count = 0
for i in range(1, 51):
    if i % 3 == 0:
        count += 1
        print(count)

# finding largest number between in a list [3,7,2,9,5]

numbers = [3, 7, 2, 9, 5]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num
print(max_num)

# write a for loop to print a square pattern of stars(*) of size 5
size = 5
for i in range(size):
    print('*' * size)

# write a for loop to reverse a string without using built-in reverse functions
s = "hello"
reversed_s = ""

for char in s:
    reversed_s = char + reversed_s
print(reversed_s)


# While loop

i = 6
while True:
    if i >= 0:
        print(i)
        break
