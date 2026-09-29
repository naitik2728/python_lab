

contacts = {}

while True:
    print("\n========== PHONEBOOK ==========")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Display Names")
    print("7. Display Phone Numbers")
    print("8. Search by City")
    print("9. Exit")

    choice = input("Enter your choice: ")

    # Add contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        city = input("Enter city: ")

        contacts[name] = {
            "phone": phone,
            "email": email,
            "city": city
        }

        print("Contact added successfully.")

    # Search contact
    elif choice == "2":
        name = input("Enter name to search: ")

        if name in contacts:
            print("\nContact Found:")
            print("Name :", name)
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
            print("City :", contacts[name]["city"])
        else:
            print("Contact not found.")

    # Update contact
    elif choice == "3":
        name = input("Enter name to update: ")

        if name in contacts:
            print("\n1. Update Phone")
            print("2. Update Email")
            print("3. Update City")

            field = input("Enter field: ")

            if field == "1":
                contacts[name]["phone"] = input("Enter new phone: ")
                print("Phone updated.")

            elif field == "2":
                contacts[name]["email"] = input("Enter new email: ")
                print("Email updated.")

            elif field == "3":
                contacts[name]["city"] = input("Enter new city: ")
                print("City updated.")

            else:
                print("Invalid field.")

        else:
            print("Contact not found.")

    # Delete contact
    elif choice == "4":
        name = input("Enter name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    # Display all contacts
    elif choice == "5":
        if not contacts:
            print("Phonebook is empty.")
        else:
            print("\nAll Contacts:")

            for name, details in contacts.items():
                print("\nName :", name)
                print("Phone:", details["phone"])
                print("Email:", details["email"])
                print("City :", details["city"])

    # Display names using keys()
    elif choice == "6":
        print("\nContact Names:")

        for name in contacts.keys():
            print(name)

    # Display phone numbers using values()
    elif choice == "7":
        print("\nPhone Numbers:")

        for details in contacts.values():
            print(details["phone"])

    # Search contacts by city using list comprehension
    elif choice == "8":
        city = input("Enter city: ")

        result = [
            name
            for name, details in contacts.items()
            if details["city"].lower() == city.lower()
        ]

        if result:
            print("\nContacts from", city + ":")
            for name in result:
                print(name)
        else:
            print("No contacts found.")

    # Exit
    elif choice == "9":
        print("Exiting Phonebook...")
        break

    else:
        print("Invalid choice.")