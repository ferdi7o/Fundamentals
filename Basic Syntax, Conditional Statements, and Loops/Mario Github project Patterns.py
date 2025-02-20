# 🖼️ Python Pattern Drawing Project

# Step 1: Display a menu to the user
print("🌟 Welcome to the Python Pattern Drawing Program!")
print("Choose a pattern type:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Hollow Square")
print("6. Pyramid")
print("7. Reverse Pyramid")
print("8. Rectangle with Hollow Center")

# Step 2: Get the user's choice
choice = int(input("Enter the number corresponding to your choice: "))

rows = size = 0

# Step 3: Get dimensions based on choice
if choice in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
    rows = int(input("Enter the number of rows: "))
elif choice in [2, 5]:  # Patterns that need size
    size = int(input("Enter the size of the square/rectangle: "))

# Step 4: Generate the selected pattern
if choice == 1:  # Right-angled Triangle
    for i in range(1,rows + 1, 1):
        print(i * "*")

elif choice == 2 or choice == 5:  # Square with Hollow Center
    for i in range(size):
        if i == 0 or i == (size -1):
            print("*" * size)
        else:
            print("*" + (" " * (size - 2)) + "*")

elif choice == 3:  # Diamond
    for k in range(1, rows + 1, 2):
        print(" " * ((rows - k) // 2) + "*" * k)
    for m in range(rows -2, 0, -2):
        print(" " * ((rows - m) // 2) + ( "*" * m ))

elif choice == 4:  # Left-angled Triangle
    for i in range(rows, 0 , -1):
        print(i * "*")

elif choice == 5:  # Hollow Square
    # TODO: Similar to choice 2 but ensure perfect square logic
    pass

elif choice == 6:  # Pyramid
    for i in range(1, rows + 1, 2):
        print(" " * ((rows - i) // 2) + ("*" * i) )

elif choice == 7:  # Reverse Pyramid
    for i in range(rows, 0, -2):
        print(" " * ((rows - i) // 2) + ("*" * i) )

elif choice == 8:  # Rectangle with Hollow Center
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))

    for i in range(height):
        if i == 0 or i == (height - 1):
            print("*" * width)
        else:
            print("*" + (" " * (width - 2)) + "*")

else:
    print("❌ Invalid choice! Please restart the program.")


# Step 5: Optional - Allow the user to restart or exit