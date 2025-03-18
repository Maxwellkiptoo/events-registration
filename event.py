# ============== SELWYN EVENT TICKETING SYSTEM ==============
# Student Name: 
# Student ID : 
# ================================================================

from datetime import datetime, timedelta
from set_data_alternative import customers, events, unique_id, display_formatted_row


# This section of code will list all the customers details 
def list_all_customers():
    """  Lists customer details."""
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <20}" 
    display_formatted_row(["ID", "First Name", "Family Name", "Birth Date", "e-Mail"], format_str)   
    
    for customer in customers:
        id = customer[0]
        fname = customer[1]
        famname = customer[2]
        birthdate = customer[3].strftime("%d %b %Y")
        email = customer[4]

        display_formatted_row([id, fname, famname, birthdate, email], format_str)

    input("\nPress Enter to continue.")

# This section of code will sow the customers details and tickets they have has purchased
def list_customers_and_tickets():
    """Lists customers and the events they have purchased tickets for, sorted alphabetically by event name."""
    format_str = "{: <5} {: <15} {: <15} {: <14} {: <25} {: <30}"
    display_formatted_row(["ID", "First Name", "Family Name", "Birth Date", "e-Mail", "Events & Tickets"], format_str)
    for customer in customers:
        id = customer[0]
        fname = customer[1]
        famname = customer[2]
        birthdate = customer[3].strftime("%d %b %Y")
        email = customer[4]
       
# This code will help to get events this customer has purchased tickets for
        events_list = []
        for event, details in events.items():
            for buyer in details["customers"]:
                if buyer[0] == id:
                    events_list.append(f"{event} ({buyer[1]})")

        events_str = ", ".join(events_list) if events_list else "No Tickets Purchased"
        display_formatted_row([id, fname, famname, birthdate, email, events_str], format_str)
    input("\nPress Enter to continue.")

# This code will help to know the events listed
def list_event_details():
    """Lists all event details except customer data, sorted alphabetically by event name."""
    format_str = "{: <20} {: <10} {: <12} {: <10} {: <15}"
    display_formatted_row(["Event Name", "Age Limit", "Event Date", "Capacity", "Tickets Sold"], format_str)
    for event in sorted(events):
        details = events[event]
        event_name = event
        age_limit = details["age_restriction"]
        event_date = details["event_date"].strftime("%d %b %Y")
        capacity = details["capacity"]
        tickets_sold = details["tickets_sold"]
        display_formatted_row([event_name, age_limit, event_date, capacity, tickets_sold], format_str)
    input("\nPress Enter to continue.")

# This sections will will promt the customers details when buying the tickets
def buy_tickets():
    """Allows customers to buy tickets if they meet the age and availability criteria."""
    try:
        cust_id = int(input("Enter Customer ID: "))
        customer = next((c for c in customers if c[0] == cust_id), None)
        if not customer:
            print("Customer not found.")
            return
        fname = customer[1]
        famname = customer[2]
        birthdate = customer[3].strftime("%d %b %Y")
        age = (datetime.today().date() - customer[3]).days // 365
        print(f"\nCustomer: {fname} {famname} (Born: {birthdate}, Age: {age})")
        available_events = sorted(
            [event for event, details in events.items() if details["event_date"] > datetime.today().date() and details["tickets_sold"] < details["capacity"]]
        )
        if not available_events:
            print("No available events.")
            return

        print("\nAvailable Events:")
        format_str = "{: <20} {: <12} {: <10}"
        display_formatted_row(["Event Name", "Event Date", "Age Limit"], format_str)
        for event in available_events:
            details = events[event]
            display_formatted_row([event, details["event_date"].strftime("%d %b %Y"), details["age_restriction"]], format_str)

        event_name = input("\nEnter event name: ")
        if event_name not in events:
            print("Invalid event name.")
            return
        
        event = events[event_name]
        if age < event["age_restriction"]:
            print("You do not meet the age requirement for this event.")
            return

        tickets = int(input("How many tickets? "))
        if tickets <= 0:
            print("Invalid ticket quantity.")
            return

        if tickets + event["tickets_sold"] > event["capacity"]:
            print("Not enough tickets available.")
            return

        event["tickets_sold"] += tickets
        event["customers"].append((cust_id, tickets))
        print(f"Successfully purchased {tickets} ticket(s) for {event_name}!")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

    input("\nPress Enter to continue.")

# This section will promt the new customers to enter their details such as their name and email
def add_new_customer():
    """Adds new customers continuously until the user exits."""
    while True:
        print("\n=== Add New Customer ===")
        new_id = unique_id()
        fname = input("Enter First Name (or 'X' to exit): ").strip()
        if fname.upper() == "X":
            break

        famname = input("Enter Family Name: ").strip()
        birthdate_str = input("Enter Birth Date (DD/MM/YYYY): ").strip()
        email = input("Enter Email: ").strip()

        try:
            birthdate = datetime.strptime(birthdate_str, "%d/%m/%Y").date()

            today = datetime.today().date()
            min_birthdate = today.replace(year=today.year - 110)

            if birthdate > today or birthdate < min_birthdate:
                print("Invalid birth date.")
                continue
            
            customers.append([new_id, fname, famname, birthdate, email])
            print(f"Customer {fname} {famname} added successfully!")

        except ValueError:
            print("Invalid date format. Please enter the date as DD/MM/YYYY.")

    input("\nPress Enter to continue.")

# This section will list all the future events or upcoming events and ommitte the one which have passed 
def list_future_available_events():
    """Lists all future events that have tickets available, sorted by date."""
    format_str = "{: <20} {: <12} {: <10}"
    display_formatted_row(["Event Name", "Event Date", "Available"], format_str)
    future_events = sorted(
        [event for event in events if events[event]["event_date"] > datetime.today().date() and events[event]["tickets_sold"] < events[event]["capacity"]],
        key=lambda e: events[e]["event_date"]
    )
    for event in future_events:
        details = events[event]
        available = details["capacity"] - details["tickets_sold"]
        display_formatted_row([event, details["event_date"].strftime("%d/%m/%Y"), available], format_str)
    input("\nPress Enter to continue.")

# This is the menu section where the customer will chose from
def disp_menu():
    """Displays the menu and current date."""
    print("==== WELCOME TO SELWYN EVENT TICKETING SYSTEM ===")
    print(" 1 - List Customers")
    print(" 2 - List Customers and their Events")
    print(" 3 - List Event Details")
    print(" 4 - Buy Tickets")
    print(" 5 - Future Events with tickets")
    print(" 6 - Add New Customer")
    print(" X - eXit (stops the program)")

# This section consist of what the customer should insert while choosing 
response = ""
while response.upper() != "X":
    disp_menu()
    response = input("Please enter menu choice: ").upper()
    if response == "1":
        list_all_customers()
    elif response == "2":
        list_customers_and_tickets()
    elif response == "3":
        list_event_details()
    elif response == "4":
        buy_tickets()
    elif response == "5":
        list_future_available_events()
    elif response == "6":
        add_new_customer()
    elif response != "X":
        print("\n*** You have choosen wrong response, please try again (enter any chose from 1-6 or X)")
    print("")

print("\n=== Thank you for using the SELWYN EVENT TICKET SYSTEM! ===\n")
