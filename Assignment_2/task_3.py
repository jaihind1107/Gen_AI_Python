# Task 3: User Menu

orders = []

while True:
    print("\nMenu")
    print("1 Add order amount")
    print("2 Show all orders and totals")
    print("q Quit")

    choice = input("Choose an option: ")

    if choice == "q":
        break

    elif choice == "1":
        try:
            amount = int(input("Enter order amount: "))
            orders.append(amount)
        except ValueError:
            print("Invalid amount.")
            continue

    elif choice == "2":
        print("Orders summary:")
        for order in orders:
            if order >= 2000:
                discount_rate = 0.15
            elif order >= 1500:
                discount_rate = 0.10
            elif order >= 1000:
                discount_rate = 0.07
            else:
                discount_rate = 0.0

            final_amount = order - (order * discount_rate)
            print("Order:", order, "Final:", final_amount)

    else:
        print("Invalid option. Try again.")
        continue