"""Simple contact management assistant bot with basic CRUD operations."""

from functools import wraps
from typing import Callable, Dict


def get_error_message (
        errors: Dict[str, Dict[str, str]],
        err: Exception,
        func: Callable,
        default_error: str
    ):
    """Return a user-friendly error message based on the exception type and function name."""
    exception_name = type(err).__name__
    func_name = func.__name__
    message = errors.get(exception_name, {}).get(func_name, "")
    return message if message else default_error

def input_error(func):
    """Decorator that handles common input errors and provides user-friendly messages."""
    @wraps(func)
    def inner(*args, **kwargs):
        errors: Dict[str, Dict[str, str]] = {
            "ValueError": {
                "add_contact": "Give me name and phone please.",
                "change_contact": "Give me name and phone please.",
                "show_phone": "Invalid name format.",
            },
            "IndexError": {
                "add_contact": "Give me name and phone please.",
                "change_contact": "Give me name and phone please.",
                "show_phone": "Enter user name",
            },
            "KeyError": {
                "change_contact": "Contact not found.",
                "show_phone": "Contact not found."
            },
            "TypeError": {
                "add_contact": "Invalid argument types. Name and phone must be text.",
                "change_contact": "Invalid argument types. Name and phone must be text.",
                "show_phone": "Invalid argument type for name."
            }
        }
        default_error = "An error occurred. Please check your input and try again."
        try:
            return func(*args, **kwargs)
        except KeyError as err:
            return get_error_message(errors, err, func, default_error)
        except ValueError as err:
            return get_error_message(errors, err, func, default_error)
        except IndexError as err:
            return get_error_message(errors, err, func, default_error)
        except TypeError as err:
            return get_error_message(errors, err, func, default_error)
    return inner

def parse_input(user_input):
    """Parse user input into command and arguments, converting command to lowercase."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    """Add a new contact to the address book, checking for duplicates."""
    name, phone = args
    if name in contacts:
        return f"A contact with that name \"{name}\" already exists.add"
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    """Update the phone number for an existing contact."""
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    """Display the phone number for a specified contact."""
    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact is not exists."

def show_all(contacts):
    """Format and return a list of all contacts and their phone numbers."""
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    """Run the main bot loop, processing user commands until exit."""
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
            result = add_contact(args, contacts)
            print(result)
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
