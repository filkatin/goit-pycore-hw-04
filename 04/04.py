def main():
    contacts = {}

    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        if command == "hello":
            response = "How can I help you?"
        elif command == "add":
            response = add_contact(args, contacts)
        elif command == "change":
            response = change_contact(args, contacts)
        elif command == "phone":
            response = show_phone(args, contacts)
        elif command == "all":
            response = show_all_contacts(contacts)
        else:
            response = "Invalid command."

        print(response)

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: Command 'add' requires exactly 2 arguments (name and phone)."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: Command 'change' requires exactly 2 arguments (name and new phone)."
    name, phone = args
    if name not in contacts:
        return f"Error: Contact '{name}' does not exist."
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: Command 'phone' requires exactly 1 argument (name)."
    name = args[0]
    if name not in contacts:
        return f"Error: Contact '{name}' not found."
    return contacts[name]

def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

if __name__ == "__main__":
    main()
