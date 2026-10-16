# Define the denominations as a constant
DENOMINATIONS = [
    ('One Thousand Peso Bill', 1000.00),
    ('Five Hundred Peso Bill', 500.00),
    ('Two Hundred Peso Bill', 200.00),
    ('One Hundred Peso Bill', 100.00),
    ('Fifty Peso Bill', 50.00),
    ('Twenty Peso Bill', 20.00),
    ('Ten Peso Coin', 10.00),
    ('Five Peso Coin', 5.00),
    ('One Peso Coin', 1.00),
    ('Twenty-Five Centavo Coin', 0.25),
    ('Ten Centavo Coin', 0.10),
    ('Five Centavo Coin', 0.05),
    ('One Centavo Coin', 0.01)
]

def calculate_change(price, amount_paid): 
    """Calculate the change to be returned."""
    # Check if the amount paid is less than the price
    if amount_paid < price:
        raise ValueError("Amount paid is less than the price.")
    # Check if the price or amount paid is negative
    if price < 0 or amount_paid < 0:
        raise ValueError("Price and amount paid must be non-negative.")

    # Calculate the change and round it to 2 decimal places
    return round(amount_paid - price, 2)

def get_denominations(change):
    """Get the denominations of the change in Philippine Pesos."""
    # Create an empty dictionary to store the change distribution
    change_distribution = {}

    # Loop through each denomination and its value
    for denomination, value in DENOMINATIONS:
        # Calculate how many of this denomination can fit into the change
        count = int(change // value)
        # If at least one of this denomination is needed, add it to the distribution
        if count > 0:
            change_distribution[denomination] = count
            # Subtract the total value of this denomination from the change
            change = round(change - count * value, 2)

    # Return the dictionary of change distribution
    return change_distribution

def print_change_distribution(change_distribution):
    """Print the change distribution."""
    print("Change distribution:")
    # Loop through each denomination and its count in the distribution
    for denomination, count in change_distribution.items():
        print(f"{count} x {denomination}")

def main():
    while True:
        try:
            # Get the price and amount paid from the user
            price = float(input("Enter the price: "))
            amount_paid = float(input("Enter the amount paid: "))

            # Calculate the change and get the change distribution
            change = calculate_change(price, amount_paid)
            change_distribution = get_denominations(change)
            # Print the change distribution
            print_change_distribution(change_distribution)

        except ValueError as e:
            # Handle any value errors and print the error message
            print(f"Error: {e}")

        # Ask the user if they want to try again
        try_again = input("Do you want to try again? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
