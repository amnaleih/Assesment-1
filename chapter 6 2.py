prompt = "How old are you?"
prompt += "\nEnter 'quit' when you have finished already. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You can get in for free !")
    elif age < 13:
        print("  Your ticket's price  is $10.")
    else:
        print("  Your ticket's price  is $15.")