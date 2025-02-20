text = input()

while text != "End":
    if text != "SoftUni":
        double_text = ""
        for charecter in text:
            double_text += (charecter * 2)
        print(double_text)
    text = input()