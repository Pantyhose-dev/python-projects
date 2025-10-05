# Jared West
# CS-500
# Mr. Chou
# Cookout Calculator Program
# This program has been designed to aid in calculating the total cost of a Cookout.

def cookout_calculator():
    # Get user input
    print('Welcome to Cookout Calculator!')
    num_people = int(input("Enter the number of people attending the cookout: "))
    brats_per_person = int(input("Enter the number of brats each person will be given: "))

    # Calculate total brats and buns needed
    total_brats = num_people * brats_per_person
    total_buns = total_brats  # Assuming 1:1 ratio of brats to buns

    # Calculate the number of packages needed
    brats_packages = (total_brats + 11) // 12  # Round up to the nearest package
    buns_packages = (total_buns + 15) // 16    # Round up to the nearest package

    # Calculate leftovers
    brats_leftovers = (brats_packages * 12) - total_brats
    buns_leftovers = (buns_packages * 16) - total_buns

    # Display the results
    print(f"\nMinimum number of packages of 12 brats required: {brats_packages}")
    print(f"Minimum number of packages of 16 buns required: {buns_packages}")
    print(f"Number of brats that will be left over: {brats_leftovers}")
    print(f"Number of buns that will be left over: {buns_leftovers}")
    print('THANK YOU FOR USING THE COOKOUT CALCULATOR!')
# Run the cookout calculator
cookout_calculator()
   
