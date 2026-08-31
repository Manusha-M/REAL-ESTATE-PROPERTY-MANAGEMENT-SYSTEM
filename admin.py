from admin.admin import AdminModule
from admin.property_management import PropertyManagement


def admin_menu():
    admin = AdminModule()
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
            if choice == '1': admin.add_agent(input('Agent name: ').strip(), input('Agent email: ').strip(), input('Agent password: ').strip())
            elif choice == '2': admin.view_agents()
            elif choice == '3': admin.view_customers()
            elif choice == '4': admin.add_property_interactive()
            elif choice == '5': admin.view_all_properties()
            elif choice == '6': admin.approve_property(int(input('Property ID: ')))
            elif choice == '7': admin.reject_delete_property(int(input('Property ID: ')))
            elif choice == '8': admin.view_all_enquiries()
            elif choice == '9': admin.view_enquiries_by_property(int(input('Property ID: ')))
            elif choice == '10': admin.view_bookings_detailed()
            elif choice == '11': admin.update_booking(int(input('Booking ID: ')), 'Approved')
            elif choice == '12': admin.update_booking(int(input('Booking ID: ')), 'Rejected')
            elif choice == '13': break
            else: print('Invalid choice.')
        except ValueError: print('Please enter a valid number.')
        except Exception as error: print('Error:', error)

if __name__ == '__main__':
    AdminModule().create_default_accounts()
    admin_menu()
