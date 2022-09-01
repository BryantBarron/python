#fxns with outputs

def format_name(first, last):
    if first == "" or last == "":
        return "You didn't provide valid inputs."
    first_name = first.title()
    last_name = last.title()

    #print(f"{first_name} {last_name}")
    return f"{first_name} {last_name}"

# formatted_names = format_name("bryant", "BRYANT")
# print(formatted_names)

print(format_name(input("What is your first name? "), input("What is your last name? ")))