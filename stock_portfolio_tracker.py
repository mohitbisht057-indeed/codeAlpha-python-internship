# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 350
}

print("=== STOCK PORTFOLIO TRACKER ===")
print("Available Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", price)

total = 0

n = int(input("How many stocks do you want to buy? "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stock_prices:
        investment = stock_prices[stock_name] * quantity
        total += investment
    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total)

# Save result to file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value = " + str(total))

print("Result saved in portfolio.txt")