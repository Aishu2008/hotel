#hotel management

print("="*50)
print("WELCOME TO 5 star HOTEL MANAGEMENT ")
print("="*50)

import pymysql

# Database Connection
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="1234",
    database="hotel_crud"
)

cursor = conn.cursor()

def recepit(name, room_type, days, bill):
    print("\n========== RECEIPT ==========")
    print(f"Customer Name: {name}")
    print(f"Room Type: {room_type}")
    print(f"Number of Days: {days}")
    print(f"Total Bill: {bill}")
    print("="*30)
    
# Add Customer
def Add_customer():
    name = input("Enter Customer Name: ")
    room_type = input("Enter Room Type (AC/Non AC): ")
    days = int(input("Enter Number of Days: "))

    if room_type.lower() == "ac":
        bill = days * 1500
    elif room_type.lower() == "non ac":
        bill = days * 1000
    else:
        print("Invalid Room Type")
        return
    print(f"Total Bill for {days} days in {room_type} room is: {bill}")

    sql = "INSERT INTO hotel(customer_name, room_type, days, bill) VALUES(%s,%s,%s,%s)"

    cursor.execute(sql, (name, room_type, days, bill))
    conn.commit()
    recepit(name, room_type, days, bill)
    print("Customer Added Successfully")

# View Customers
def View_customer():
    cursor.execute("SELECT * FROM hotel")
    rows = cursor.fetchall()

    print("\nRoom No\tCustomer Name\tRoom Type\tDays\tBill")
    print("-" * 60)

    for row in rows:
        print(f"{row[0]}\t{row[1]}\t\t{row[2]}\t\t{row[3]}\t{row[4]}")

# Update Customer
def Update_customer():
    room = int(input("Enter Room Number: "))

    name = input("Enter Customer Name: ")
    room_type = input("Enter Room Type: ")
    days = int(input("Enter Number of Days: "))

    if room_type.lower() == "ac":
        bill = days * 1500
    elif room_type.lower() == "non ac":
        bill = days * 1000
    else:
        print("Invalid Room Type")
        return

    sql = """
    UPDATE hotel
    SET customer_name=%s, room_type=%s, days=%s, bill=%s
    WHERE room_no=%s
    """

    cursor.execute(sql, (name, room_type, days, bill, room))
    conn.commit()
    recepit(name, room_type, days, bill)
    print("Customer Updated Successfully")

# Delete Customer
def Delete_customer():
    room = int(input("Enter Room Number: "))

    sql = "DELETE FROM hotel WHERE room_no=%s"

    cursor.execute(sql, (room,))
    conn.commit()
    print("Customer Deleted Successfully")
    
def hotel_services():
    print("\n========== HOTEL SERVICES ==========")
    print("1. Room Service")
    print("2. Laundry Service")
    print("3. Spa Service")
    print("4. Gym Access")
    print("5. Swimming Pool Access")
    print("6. Exit")

    service_option = input("Enter Your Option: ")

    if service_option == "1":
        print("Room Service Selected")
    elif service_option == "2":
        print("Laundry Service Selected")
    elif service_option == "3":
        print("Spa Service Selected")
    elif service_option == "4":
        print("Gym Access Selected")
    elif service_option == "5":
        print("Swimming Pool Access Selected")
    elif service_option == "6":
        bye()
    else:
        print("Invalid Option")
        
def hotel_rules():
    print("\n========== HOTEL RULES ==========")
    print("1. Check-in time is 2:00 PM")
    print("2. Check-out time is 12:00 PM")
    print("3. No smoking in the rooms")
    print("4. No pets allowed")
    print("5. carry your ID proof at all times")
    print("6. Exit")

    rules_option = input("Enter Your Option: ")

    if rules_option == "1":
        print("Check-in time is 2:00 PM")
    elif rules_option == "2":
        print("Check-out time is 12:00 PM")
    elif rules_option == "3":
        print("No smoking in the rooms")
    elif rules_option == "4":
        print("No pets allowed")
    elif rules_option == "5":
        print("Please carry your ID proof at all times")
    elif rules_option == "6":
        bye()
    else:
        print("Invalid Option")
    
def bye():
    print("Thank You for using the 5 Star Hotel ")
    print("have a great day!")

# Menu
while True:
    print("\n========== HOTEL MANAGEMENT SYSTEM ==========")
    print("1. Add Customer")
    print("2. View Customer")
    print("3. Update Customer")
    print("4. Delete Customer")
    print("5. Exit")

    option = input("Enter Your Option: ")

    if option == "1":
        Add_customer()
    elif option == "2":
        View_customer()
    elif option == "3":
        Update_customer()
    elif option == "4":
        Delete_customer()
    elif option == "5":
        bye()
        break
    else:
        print("Invalid Option")

cursor.close()
conn.close()