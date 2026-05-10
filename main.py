from shop import Shop

def test(shop):

    # Create sample customers
    c1 = shop.add_customer("Smith", "555-1010")
    c2 = shop.add_customer("Jones", "555-2020")
    c3 = shop.add_customer("Brown", "555-3030")

    # Rentals
    r1 = shop.new_rental(c1, 3, 1, 4)
    r2 = shop.new_rental(c2, 5, 0, 2)
    r3 = shop.new_rental(c3, 2, 2, 5)

    # Display rentals
    shop.find_rental(r1).display()
    shop.find_rental(r2).display()
    shop.find_rental(r3).display()

    # Complete a rental
    charge = shop.complete_rental(r2)
    print(f"Rental {r2} completed. Charge: ${charge}")

    # Check remaining inventory
    shop.display_inventory()



def main():
    shop = Shop()
    shop.setup_inventory(300, 300)

    while True:
        print("\n------ MAIN MENU ------")
        print("1. Add new customer")
        print("2. Display a customer")
        print("3. Display all rentals for a customer")
        print("4. Display all OPEN rentals")
        print("5. Make new rental")
        print("6. Return a rental")
        print("7. Display inventory")
        print("8. Show statistics")
        print("9. Run test")
        print("0. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            last = input("Last name: ")
            phone = input("Phone number: ")
            cid = shop.add_customer(last, phone)
            print(f"Customer added! ID = {cid}")

        elif choice == "2":
            cid = int(input("Customer ID: "))
            c = shop.find_customer(cid)
            if c: c.display()
            else: print("Customer not found")

        elif choice == "3":
            cid = int(input("Customer ID: "))
            rentals = shop.find_rentals_for_customer(cid)
            if rentals:
                for i in rentals: i.display()
            else:
                print("No rentals for this customer")

        elif choice == "4":
            shop.display_open_rentals()

        elif choice == "5":
            cid = int(input("Customer ID: "))
            if shop.find_customer(cid) is None:
                print("Customer does not exist, please add them first")
                continue

            skis = int(input("Skis to rent: "))
            snow = int(input("Snowboards to rent: "))
            hours = int(input("Hours: "))
            rid = shop.new_rental(cid, skis, snow, hours)
            if rid is None:
                print("Not enough inventory!")
            else:
                print(f"Rental created! Rental ID = {rid}")

        elif choice == "6":
            rid = int(input("Rental ID: "))
            result = shop.complete_rental(rid)
            if result == "already_closed":
                print("This rental is already completed.")
            elif result is None:
                print("Rental not found.")
            else:
                print(f"Rental complete. Total charge: ${result}")

        elif choice == "7":
            shop.display_inventory()

        elif choice == "8":
            print("---- STATISTICS ----")
            print(f"Total Income: ${shop.total_income}")
            print(f"Total Customers: {len(shop.customers)}")
            print(f"Total Rentals: {len(shop.rentals)}")

        elif choice == "9":
            test(shop)

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print("Invalid input. Try again.")


if __name__ == "__main__":
    main()
