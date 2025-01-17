def describe_city(city, country='mexico'):
    """Describe a city."""
    msg = f"{city.title()} is located in {country.title()}."
    print(msg)

describe_city('acapulo')
describe_city('antigua', 'guatemala')
describe_city('guanajuato')