number = float(input())

if number == 0:
    print("zero")
elif 1_000_000 > number >= 1:
    print("positive")
elif 1 > number > 0:
    print("small positive")
elif number >= 1_000_000:
    print("large positive")
elif 0 > number >= -1:
    print("small negative")
elif -1 > number > -1_000_000:
    print("negative")
elif number < -1_000_000:
    print("large negative")
