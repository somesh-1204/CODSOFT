# ===============================
#      SMART CONTACT BOOK
# ===============================

contacts = {}

while True:

    print("\n" + "=" * 45)
    print("        📒 SMART CONTACT BOOK")
    print("=" * 45)
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    # -------- ADD CONTACT --------
    if choice == "1":

        phone = input("Phone Number: ")

        if phone in contacts:
            print("⚠ Contact already exists.")
            continue

        contacts[phone] = {
            "Name": input("Name: ").title(),
            "Email": input("Email: "),
            "Address": input("Address: ")
        }

        print("✅ Contact Saved Successfully!")

    # -------- VIEW CONTACTS --------
    elif choice == "2":

        if not contacts:
            print("\nNo Contacts Available.")
        else:
            print("\n" + "-" * 60)
            print("{:<15}{:<20}".format("Phone", "Name"))
            print("-" * 60)

            for phone, details in contacts.items():
                print("{:<15}{:<20}".format(phone, details["Name"]))

    # -------- SEARCH CONTACT --------
    elif choice == "3":

        search = input("Enter Name or Phone: ").lower()

        found = False

        for phone, details in contacts.items():

            if search == phone or search == details["Name"].lower():

                print("\nContact Found")
                print("-" * 25)
                print("Name    :", details["Name"])
                print("Phone   :", phone)
                print("Email   :", details["Email"])
                print("Address :", details["Address"])
                found = True

        if not found:
            print("❌ Contact Not Found.")

    # -------- UPDATE CONTACT --------
    elif choice == "4":

        phone = input("Enter Phone Number: ")

        if phone in contacts:

            print("\nPress Enter to keep old value.")

            name = input(f"New Name ({contacts[phone]['Name']}): ")
            email = input(f"New Email ({contacts[phone]['Email']}): ")
            address = input(f"New Address ({contacts[phone]['Address']}): ")

            if name:
                contacts[phone]["Name"] = name.title()

            if email:
                contacts[phone]["Email"] = email

            if address:
                contacts[phone]["Address"] = address

            print("✅ Contact Updated Successfully!")

        else:
            print("❌ Contact Not Found.")

    # -------- DELETE CONTACT --------
    elif choice == "5":

        phone = input("Enter Phone Number to Delete: ")

        if phone in contacts:
            del contacts[phone]
            print("🗑 Contact Deleted Successfully!")
        else:
            print("❌ Contact Not Found.")

    # -------- EXIT --------
    elif choice == "6":

        print("\nThank you for using Smart Contact Book!")
        break

    else:
        print("❌ Invalid Choice!")