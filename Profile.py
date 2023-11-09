"""
Displays a menu for profile editing with the following options:

=== Profile Editing ===

1. Edit Bio
2. Change Username
3. Save Changes
4. Cancel

Prompts the user to choose an option (1-4).
"""


# main program

# Sample user profile data
user_profile = {
    "username": "example_user",
    "bio": "This is my bio. I love coding!",
}

# Display the menu
print("=== Profile Editing ===")
print("1. Edit Bio")
print("2. Change Username")
print("3. Save Changes")
print("4. Cancel")

# Prompt the user to choose an option
choice = input("Choose an option (1-4): ")


# Check if the user entered a valid option
if choice.isdigit() and 1 <= int(choice) <= 4:
    # If the user entered a valid option, perform the corresponding action
    if choice == "1":
        # If the user chose to edit the bio, prompt the user to enter a new bio
        new_bio = input("Enter your new bio: ")
        user_profile["bio"] = new_bio
        print("Bio updated successfully!")

    elif choice == "2":
        # If the user chose to change the username, prompt the user to enter a new username
        new_username = input("Enter your new username: ")
        user_profile["username"] = new_username
        print("Username updated successfully!")

    elif choice == "3":
        # If the user chose to save the changes, save the changes to the user's profile
        print("Changes saved successfully!")

    elif choice == "4":
        # If the user chose to cancel, cancel the changes and exit the menu
        print("Profile editing canceled.")

else:
    # If the user entered an invalid option, display an error message
    print("Invalid option. Please choose a valid option (1-4).")


