# Jared West
# Mr. Chou - CS500 
# Homework Ch4 - Loops

# This program aims to help calculate the increasing tuition costs of a school
# via excerciseres in loops. It does this in the following steps :
# 1. Prompt the user for the initial tuition amount.
# 2. Prompt the user for the annual percentage increase.
# 3. Prompt the user for the number of years for the increase.
# 4. Use a loop to calculate and display the tuition for each year.

# Function to calculate and display the projected tuition
def calculate_projected_tuition(initial_tuition, annual_increase, years):
    # Loop through each year and calculate the tuition
    for year in range(1, years + 1):
        # Calculate the tuition for the current year
        current_tuition = initial_tuition * (1 + annual_increase / 100) ** year
        # Display the projected tuition for the current year
        print(f"Year {year}: Projected Tuition = ${current_tuition:.2f}")

# Main program
def main():
    # Get user input
    initial_tuition = float(input("Enter the initial tuition amount: "))
    annual_increase = float(input("Enter the annual percentage increase: "))
    years = int(input("Enter the number of years for the increase: "))

    # Calculate and display the projected tuition
    calculate_projected_tuition(initial_tuition, annual_increase, years)

# Call the main function
if __name__ == "__main__":
    main()
