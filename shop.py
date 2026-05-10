SKI_RATE = 15
SNOWBOARD_RATE = 10


class Customer:
    """
    Represents a customer of the ski and snowboard rental shop
    A customer stores their last name, phone number, and an automatically assigned unique ID
    """

    newID = 1  # class variable so no two customers share the same ID

    def __init__(self, last_name, phone_number):
        """
        Creates a new customer
        ID is automatically assigned from Customer.newID
        """
        self.last_name = last_name
        self.phone_number = phone_number
        self.customer_id = Customer.newID
        Customer.newID += 1

    def display(self):
        """Print customer information"""
        print("CUSTOMER INFORMATION:")
        print(f"Customer Name: {self.last_name}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Phone Number: {self.phone_number}")


class Rental:
    """
    Represents a rental transaction
    Stores rental ID, customer ID, equipment, hours, and whether it is closed
    """

    newRentalID = 1

    def __init__(self, customer_id, skis_rented, snowboards_rented, hours):
        """
        Creates a rental record
        RentalID is automatically assigned
        """
        self.rental_id = Rental.newRentalID
        Rental.newRentalID += 1

        self.customer_id = customer_id
        self.skis_rented = skis_rented
        self.snowboards_rented = snowboards_rented
        self.hours = hours
        self.isClosed = False

    def display(self):
        """Print all rental details"""
        print("RENTAL INFO:")
        print(f"Rental ID: {self.rental_id}")
        print(f"Customer ID: {self.customer_id}")
        print(f"Skis Rented: {self.skis_rented}")
        print(f"Snowboards Rented: {self.snowboards_rented}")
        print(f"Hours Rented: {self.hours}")
        print(f"Closed: {self.isClosed}")


class Shop:
    """
    Represents the rental shop
    Stores inventory, customer list, rentals list, total income
    """

    def __init__(self):
        """Creates a shop with empty lists and no income"""
        self.ski_inventory = 0
        self.snowboard_inventory = 0
        self.customers = []
        self.rentals = []
        self.total_income = 0.0

    def setup_inventory(self, skis, snowboards):
        """Sets the inventory for skis and snowboards"""
        self.ski_inventory = skis
        self.snowboard_inventory = snowboards

    def add_customer(self, last_name, phone_number):
        """Create a new customer and stores them in the list"""
        new_customer = Customer(last_name, phone_number)
        self.customers.append(new_customer)
        return new_customer.customer_id

    def find_customer(self, customer_id):
        """Returns the customer object with the matching ID or none"""
        for i in self.customers:
            if i.customer_id == customer_id:
                return i
        return None

    def find_rental(self, rental_id):
        """Returns the rental object with the matching ID or None"""
        for i in self.rentals:
            if i.rental_id == rental_id:
                return i
        return None

    def find_rentals_for_customer(self, customer_id):
        """Returns a list of all rentals belonging to a customer"""
        rental_list = []

        for rental in self.rentals:
            if rental.customer_id == customer_id:
                rental_list.append(rental)

        return rental_list

    def new_rental(self, customer_id, skis, snowboards, hours):
        """
        Creates a new rental if the shop has enough inventory
        Returns the new rental ID, or None if inventory is insufficient
        """
        if skis > self.ski_inventory or snowboards > self.snowboard_inventory:
            return None  # not enough equipment

        rent_obj = Rental(customer_id, skis, snowboards, hours)
        self.rentals.append(rent_obj)

        # remove equipment from inventory
        self.ski_inventory -= skis
        self.snowboard_inventory -= snowboards

        return rent_obj.rental_id

    def complete_rental(self, rental_id):
        """
        Completes the rental, returns equipment, calculates charge, and adds income
        """
        rental = self.find_rental(rental_id)

        if rental is None:
            return None

        if rental.isClosed:
            return "already_closed"

        rental.isClosed = True

        ski_cost = rental.skis_rented * SKI_RATE
        snowboard_cost = rental.snowboards_rented * SNOWBOARD_RATE

        charge = (ski_cost + snowboard_cost) * rental.hours

        self.total_income += charge

        # put equipment back
        self.ski_inventory += rental.skis_rented
        self.snowboard_inventory += rental.snowboards_rented

        return charge

    def display_open_rentals(self):
        """Print all rentals that are NOT completed"""
        for i in self.rentals:
            if not i.isClosed:
                i.display()

    def display_inventory(self):
        """Print current available equipment"""
        print("CURRENT INVENTORY:")
        print(f"Skis Available: {self.ski_inventory}")
        print(f"Snowboards Available: {self.snowboard_inventory}")
