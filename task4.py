from functools import wraps # just for metadata of func

# Decorator
def input_error(func):
    @wraps(func) # To get metadata of inner function in future
    def inner(*args, **kwargs):
        # Handle exception
        try:
            return func(*args, **kwargs) # call the func with arguments
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter user name"
        except KeyError:
            return "Please provide normal key"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Use decorator for func 
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Use decorator for func 
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

# Use decorator for func 
@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f'Name: {name}, phone: {contacts.get(name)}'
    return 'User doesn\'t exist'

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_phone(args, contacts))
        elif command == "all":
            print(contacts)
        else: 
            print("Invalid command.")

if __name__ == "__main__":
    main()