
n = int(input("Enter the number you want (1-6): "))

if 1 <= n <= 6:
    probability = 1 / 6
    print("Probability =", probability)
else:
    print("Invalid number!")