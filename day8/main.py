""" def greet():
    print("Practicing Functions")
    print("Futurama")
    print("Streetlight Manifesto")

greet() """

#function that allows for input
""" def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_name("Bryant") """

""" def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with("Bryant", "Malibu") """

def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")


greet_with(location="Santa Barbara", name="Bryant")
