prompt = "\nWhat type toppings would you like to put on your pizza?"
prompt += "\nEnter 'quit' when you have finished already: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break