from agent.agent import Agent


def agent_login():
    print("\n========== AGENT LOGIN ==========")

    email = input("Email: ").strip()
    password = input("Password: ").strip()

    users = Agent.load_users()

    for user in users:
        if (
            user.get("email") == email
            and user.get("password") == password
            and user.get("role") == "agent"
        ):
            agent = Agent.from_dict(user)
            print(f"\nWelcome, {agent.name} (Agent)!")
            agent_menu(agent)
            return

    print("\nInvalid agent email or password.")


def agent_menu(agent):
    while True:
        print("\n========== AGENT MENU ==========")
        print("1. Add Property")
        print("2. View My Properties")
        print("3. Update Property")
        print("4. Delete Property")
        print("5. Update Property Status")
        print("6. View Booking Requests")
        print("7. Logout")

        choice = input("Enter choice: ").strip()

        try:
            if choice == "1":
                agent.add_property_interactive()

            elif choice == "2":
                agent.view_my_properties()

            elif choice == "3":
                property_id = input("Enter Property ID: ").strip()
                agent.update_my_property(property_id)

            elif choice == "4":
                property_id = input("Enter Property ID: ").strip()
                agent.delete_my_property(property_id)

            elif choice == "5":
                property_id = input("Enter Property ID: ").strip()
                agent.update_my_property_status(property_id)

            elif choice == "6":
                agent.view_bookings()

            elif choice == "7":
                print("Agent logged out.")
                break

            else:
                print("Invalid choice. Please enter 1-7.")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    agent_login()