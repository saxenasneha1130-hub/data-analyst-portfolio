stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 380,
    "INFY": 20
}

portfolio = {}
total = 0

print("📈 Stock Portfolio Tracker")
print("-" * 30)

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break
    
    if stock in stocks:
        qty = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = qty
        print(f"✅ Added {qty} shares of {stock} @ ₹{stocks[stock]}")
    else:
        print("❌ Stock not found!")

print("\n📊 Your Portfolio Summary")
print("-" * 30)

for stock, qty in portfolio.items():
    value = stocks[stock] * qty
    total += value
    print(f"{stock}: {qty} shares x ₹{stocks[stock]} = ₹{value}")

print("-" * 30)
print(f"💰 Total Investment: ₹{total}")