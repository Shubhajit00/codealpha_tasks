# Simple stock portfolio calculator

# Hardcoded stock prices (simulating a real-world portfolio)
prices = {
    "AAPL": 180,
    "TSLA": 250,
    "AMZN": 120,
    "GOOGL": 135,
    "MSFT": 300
}

print("\nWelcome to the Stock Portfolio Tracker!")
print("Available stocks:", ', '.join(prices.keys()))
print("Type 'done' when you're finished.\n")

portfolio = {}
total = 0

# Collect user input
while True:
    stock = input("Enter stock name (e.g., AAPL) : ").upper()
    if stock == "DONE":
        break
    if stock not in prices:
        print("Stock not recognized. Try again.")
        continue

    try:
        qty = int(input(f"How many shares of {stock} do you own? "))
        value = prices[stock] * qty
        portfolio[stock] = (qty, value)
        total += value
    except ValueError:
        print("Please enter a valid number.")

# Show results
print("\nYour Portfolio Summary:")
for symbol, (qty, val) in portfolio.items():
    print(f"{symbol}: {qty} shares × ${prices[symbol]} = ${val}")
print(f"\nTotal Investment: ${total}")

# Save to file (optional)
save = input("\nWould you like to save this to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter file name (e.g., portfolio.txt or portfolio.csv): ")
    try:
        with open(filename, "w") as f:
            f.write("Stock,Quantity,Price,Value\n")
            for symbol, (qty, val) in portfolio.items():
                f.write(f"{symbol},{qty},{prices[symbol]},{val}\n")
            f.write(f"\nTotal Investment,,,{total}")
        print(f"Saved successfully as '{filename}'.")
    except:
        print("Something went wrong while saving the file.")
