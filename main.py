from user import User
from admin import Admin
from agent import Agent
from customer import Customer
from property import Property
from enquiry import Enquiry


def admin_menu(user):
    admin = Admin.from_dict(user)
    while True:
        print("\n========== ADMIN MENU ==========")
        print("1. Add Agent")
        print("2. View Agents")
        print("3. View Customers")
        print("4. Add Property")
        print("5. View All Properties")
        print("6. Approve Property")
        print("7. Reject/Delete Property")
        print("8. View All Enquiries")
        print("9. View Enquiries By Property")
        print("10. View Booking Requests")
        print("11. Approve Booking")
        print("12. Reject Booking")
        print("13. Logout")
        choice = input("Enter choice: ").strip()
        try:
            if choice == '1':
                admin.add_agent(input('Agent name: ').strip(), input('Agent email: ').strip(), input('Agent password: ').strip())
            elif choice == '2':
                admin.view_agents()
            elif choice == '3':
                admin.view_customers()
            elif choice == '4':
                admin.add_property_interactive()
            elif choice == '5':
                Property.view_all()
            elif choice == '6':
                Property.update_status(int(input('Property ID: ')), 'Approved')
            elif choice == '7':
                Property.delete_property(int(input('Property ID: ')))
            elif choice == '8':
                Enquiry.view_all_detailed()
            elif choice == '9':
                Enquiry.view_for_property(int(input('Property ID: ')))
            elif choice == '10':
                admin.view_bookings_detailed()
            elif choice == '11':
                admin.update_booking(int(input('Booking ID: ')), 'Approved')
            elif choice == '12':
                admin.update_booking(int(input('Booking ID: ')), 'Rejected')
            elif choice == '13':
                break
            else:
                print('Invalid choice.')
        except ValueError:
            print('Please enter a valid number.')
        except Exception as error:
            print('Error:', error)


def agent_menu(user):
    agent = Agent.from_dict(user)
    while True:
        print("\n========== AGENT MENU ==========")
        print("1. Add Property")
        print("2. View My Properties")
        print("3. Search Approved Properties")
        print("4. Update My Property")
        print("5. Delete My Property")
        print("6. Update Property Availability")
        print("7. View Customer Enquiries")
        print("8. View Enquiries For Property")
        print("9. View Booking Requests")
        print("10. Logout")
        choice = input('Enter choice: ').strip()
        try:
            if choice == '1':
                agent.add_property_interactive()
            elif choice == '2':
                agent.view_my_properties()
            elif choice == '3':
                Customer.search_properties_interactive(approved_only=True)
            elif choice == '4':
                agent.update_my_property(int(input('Property ID: ')))
            elif choice == '5':
                agent.delete_my_property(int(input('Property ID: ')))
            elif choice == '6':
                agent.update_my_property_status(int(input('Property ID: ')))
            elif choice == '7':
                Enquiry.view_for_agent(agent.user_id)
            elif choice == '8':
                Enquiry.view_for_property(int(input('Property ID: ')), agent.user_id)
            elif choice == '9':
                agent.view_bookings()
            elif choice == '10':
                break
            else:
                print('Invalid choice.')
        except ValueError:
            print('Please enter a valid number.')
        except Exception as error:
            print('Error:', error)


def customer_menu(user):
    customer = Customer.from_dict(user)
    while True:
        print("\n========== CUSTOMER MENU ==========")
        print("1. Search Properties")
        print("2. View All Approved Properties")
        print("3. View Property Details")
        print("4. Send Enquiry")
        print("5. View My Enquiries")
        print("6. Booking Request")
        print("7. View My Bookings")
        print("8. Logout")
        choice = input('Enter choice: ').strip()
        try:
            if choice == '1':
                Customer.search_properties_interactive()
            elif choice == '2':
                Property.view_approved()
            elif choice == '3':
                Property.view_details(int(input('Property ID: ')))
            elif choice == '4':
                customer.send_enquiry(int(input('Property ID: ')), input('Message: ').strip())
            elif choice == '5':
                Enquiry.view_for_customer(customer.user_id)
            elif choice == '6':
                customer.booking_request(int(input('Property ID: ')))
            elif choice == '7':
                customer.view_bookings()
            elif choice == '8':
                break
            else:
                print('Invalid choice.')
        except ValueError:
            print('Please enter valid input.')
        except Exception as error:
            print('Error:', error)


def main():
    Admin.create_default_accounts()
    while True:
        print("\n==============================================")
        print(" REAL ESTATE PROPERTY MANAGEMENT SYSTEM")
        print("==============================================")
        print("1. Admin Login")
        print("2. Agent Login")
        print("3. Customer Registration")
        print("4. Customer Login")
        print("5. View Approved Properties")
        print("6. Exit")
        choice = input('Enter choice: ').strip()
        try:
            if choice in ('1', '2', '4'):
                user = User.login(input('Email: ').strip(), input('Password: ').strip())
                if user:
                    if user['role'] == 'admin':
                        admin_menu(user)
                    elif user['role'] == 'agent':
                        agent_menu(user)
                    elif user['role'] == 'customer':
                        customer_menu(user)
            elif choice == '3':
                User.register(input('Name: ').strip(), input('Email: ').strip(), input('Password: ').strip())
            elif choice == '5':
                Property.view_approved()
            elif choice == '6':
                print('Thank you for using the system!')
                break
            else:
                print('Invalid choice.')
        except Exception as error:
            print('Error:', error)


if __name__ == '__main__':
    main()
