glossary = {
 'string': 'A series of characters.',
    'else': 'A note in a program that the Python interpreter ignores.',
    'variable': 'A collection of items in a particular order.',
    'loops': 'Work through a collection of items, one at a time.',
    'print': "A collection of key-value pairs.",
    }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")