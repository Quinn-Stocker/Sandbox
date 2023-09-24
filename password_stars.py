min_length = 4
correct_input = False
while correct_input == False:
    password = str(input("Enter Password: "))
    if len(password) >= min_length:
        correct_input = True
hidden_pass = ""
for i in range(0, len(password), 1):
    hidden_pass = hidden_pass + "*"

print(hidden_pass)