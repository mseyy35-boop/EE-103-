# n = int(input("Enter a number: "))
# factorial = 1

# for i in range(1, n + 1):
#    factorial *= i

# print(f"{n}! = {factorial}")


n = int(input("Enter a number: "))
factorial = 1
i = 1

while i <= n:
    factorial *= i
    i += 1

print(f"{n}! = {factorial}")