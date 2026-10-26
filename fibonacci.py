n = int(input("Enter number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Enter a positive number")
else:
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()
