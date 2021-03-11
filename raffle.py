"""Read customer data from file and run a raffle."""

import random


class Customer(object):
    """A customer at Ubermelon."""

    def __init__(self, name, email, street, city, zipcode):
        self.name = name
        self.email = email
        self.street = street
        self.city = city
        self.zipcode = zipcode


def get_customers_from_file(customer_file_path):
    """Read customer file and return list of customer objects.
    Read file at customer_file_path and create a customer object
    containing customer information.
    """

    customers = []

    with open(customer_file_path) as customer_file:

    # Process a file like:
    #
    #   customer-name | email | street | city | zipcode

        for line in customer_file:
            customer_data = line.strip().split("|")
            name, email, street, city, zipcode = customer_data

            new_customer = Customer(name, email, street, city, zipcode)
            customers.append(new_customer)

    return customers


def pick_winner(customers):
    """Choose a random winner from list of customers."""

    chosen_customer = random.choice(customers)
    
    name = chosen_customer.name
    email = chosen_customer.email

    print(f"Tell {name} at {email} that they've won")
    return chosen_customer

def run_raffle():
    """Run the weekly raffle."""

    customers = get_customers_from_file("customers.txt")
    pick_winner(customers)
