sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef', 'club', 'tuna', ' chicken']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I'm making your " + current_sandwich + " sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made an " + sandwich + " sandwich for you.")