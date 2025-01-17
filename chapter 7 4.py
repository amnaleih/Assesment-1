def make_shirt(size='large', message='I love Python!'):
    """Summarize the shirt that will be made."""
    print(f"\nI am making a {size} t-shirt.")
    print(f'It will say, "{message}"')

make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programming is hard to learn.')