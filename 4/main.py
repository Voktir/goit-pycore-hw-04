
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:        
        name, phone = args
        name = name.strip().upper()
        contacts[name] = phone
        return "Contact added."
    except:
        return "Wrong data! : add [name] [phone nbr]"
    
def change_username_phone(args, contacts):
    try:        
        name, phone = args
        name = name.strip().upper()
        if name in contacts:
            contacts[name] = phone
            return "Contact changed"
        else:
            return "Wrong contact"
    except:
        return "Wrong data! : change [name] [phone nbr]"
    
def show_phone(args, contacts):
    try:        
        name, = args
        name = name.strip().upper()
        if name in contacts:
            return [int(contacts.get(name))]
        else:
            return "Wrong contact"
    except:
        return "Wrong data! : phone [name]"

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
            print(change_username_phone(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()