# Jared West
# Mr. Chou - CS500

# This program is an exercise in loops

# Particularly, this program is meant to help calculate the percentage in APR interest in student loans over time

# Projected Tuition Calculator


def main():
    while True:
        # Get user input
        current_tuition = float(input("Enter the current tuition per semester: $"))
        annual_increase = float(input("Enter the annual percentage increase (e.g., 4.5 for 4.5%): "))
        years = int(input("Enter the number of years for the projection: "))

        # Convert percentage to a decimal
        increase_decimal = annual_increase / 100

        # Calculate and display the projected tuition for each year
        print("\nProjected Tuition Over Time:")
        for year in range(1, years + 1):
            new_tuition = current_tuition * (1 + increase_decimal) ** year
            print(f"Year {year}: Projected tuition is ${new_tuition:.2f}")

        # Ask if the user wants to do another calculation
        repeat = input("\nWould you like to calculate another projection? (yes/no): ").strip().lower()
        if repeat not in ("yes", "y"):
            print("Thank you for using the Projected Tuition Calculator!")
            break

if __name__ == "__main__":
    main()
