cost_price, selling_price = map(float, input("Enter cost price and selling price: ").split())

if selling_price > cost_price:
    print("Profit:", selling_price - cost_price)
elif selling_price < cost_price:
    print("Loss:", cost_price - selling_price)
else:
    print("No profit no loss")
