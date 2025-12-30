from calendar import firstweekday


def get_formatted_name(first_name, last_name):
    """Return full name of person, neatly formatted name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(Enter 'q' to quit)")
    f_name = input("First Name: ")
    if f_name == 'q':
        break

    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name} ")