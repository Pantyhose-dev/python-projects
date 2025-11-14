# ─────────────────────────────────────────────────────────────
# TacWaffle Company LLC — Budget Calculator
# Tactical ASCII Edition
# EST. 2019
# ─────────────────────────────────────────────────────────────

print('TacWaffle Company LLC  —  EST 2019')
print('===========================================================================\n')

# Tactical ASCII Panel #1
print("  █████████████████             ____________")
print("  █ ▓ ▓ ▓ ▓ ▓ ▓ ▓ █            / ____/ ____/___  ____ ___  ___ ")
print("  █ ▓ ░ ▓ ░ ▓ ░ ▓ █      _____/ / __/ /   / __ \\/ __ `__ \\/ _ \\ ")
print("  █ ▓ ▓ ▓ ▓ ▓ ▓ ▓ █     /_____/ /_/ / /___/ /_/ / / / / / /  __/")
print("  █ ▓ ░ ▓ ░ ▓ ░ ▓ █           \\____/\\____/\\____/_/ /_/ /_/\\___/ ")
print("  █ ▓ ▓ ▓ ▓ ▓ ▓ ▓ █                 |====|==========------>")
print("  █ ▓ ░ ▓ ░ ▓ ░ ▓ █                 |====|")
print("  █ ▓ ▓ ▓ ▓ ▓ ▓ ▓ █                 |====|")
print("  █ ▓ ░ ▓ ░ ▓ ░ ▓ █                 |====|")
print("  █████████████████\n")

print("           Made by TacWaffle Company LLC — All Rights Reserved")
print("===========================================================================\n\n")

# ─────────────────────────────────────────────────────────────
# PAGE BREAK — Section Divider
# ─────────────────────────────────────────────────────────────
print("\n\n")
print("════════════════════════════════════════════════════════════════════════════")
print("       >>> PAGE BREAK — INITIAL INPUT SECTION <<<")
print("════════════════════════════════════════════════════════════════════════════")

# Tactical ASCII Helmet
print(r"""
         ____ 
       .'* *.'
    __/_*_*(_
   / _______ \
 _\_)/ ___ \(_/_
/ _(( /___\ ))_ \
\ \__)     (__/ /
 \___\_____/___/
""")

print("Please input your information below to calculate your initial budget\n")

# Get user inputs
cashier_device_cost = int(input("Enter the cost of the cashier device: "))
shelving_cost = int(input("Enter the cost of shelving units: "))
display_case_cost = int(input("Enter the cost of display cases: "))
rent_amount = int(input("Enter the monthly rent amount: "))
inventory_cost = int(input("Enter the cost of initial inventory: "))

# ─────────────────────────────────────────────────────────────
# PAGE BREAK — Calculation Section
# ─────────────────────────────────────────────────────────────
print("\n\n")
print("════════════════════════════════════════════════════════════════════════════")
print("       >>> PAGE BREAK — BUDGET CALCULATION <<<")
print("════════════════════════════════════════════════════════════════════════════")

# Tactical ASCII Scope
print(r"""
              ___---___
          .--          --.
        ./   ()      .-. \.
       /   o    .   (   )  \
      / .            '-'    \
     | ()    .  O         .  |
     \    .            .     /
      \       .     ()     ./
       `\  .        .    ./`
         `--___    ___--`
               --- 
""")

# Calculate budget
def calculate_total_budget():
    total_budget = (cashier_device_cost +
                    shelving_cost +
                    display_case_cost +
                    rent_amount +
                    inventory_cost)
    return total_budget

# ─────────────────────────────────────────────────────────────
# PAGE BREAK — Final Report
# ─────────────────────────────────────────────────────────────
print("\n\n")
print("════════════════════════════════════════════════════════════════════════════")
print("       >>> PAGE BREAK — FINAL BUDGET REPORT <<<")
print("════════════════════════════════════════════════════════════════════════════")

# Tactical ASCII Shield
print(r"""
        █████████████████████
        ████ ▄▄▄▄▄ █ ▄▄▄▄▄ ████
        ████ █   █ █ █   █ ████
        ████ █▄▄▄█ █ █▄▄▄█ ████
        ████▄▄▄▄▄▄▄█▄▄▄▄▄▄▄████
""")

# Display results
def display_budget_breakdown():
    print(f"Cashier Device Cost:      ${cashier_device_cost}")
    print(f"Shelving Cost:            ${shelving_cost}")
    print(f"Display Case Cost:        ${display_case_cost}")
    print(f"Rent Amount (monthly):    ${rent_amount}")
    print(f"Inventory Cost:           ${inventory_cost}")
    print("------------------------------------------------------------------")
    print(f"TOTAL BUSINESS STARTUP BUDGET:   ${calculate_total_budget()}")
    print("------------------------------------------------------------------")

display_budget_breakdown()

print("\nThank you for using the TacWaffle Tactical Budget Calculator.")
print("Stay Tactical. Stay Prepared.")
