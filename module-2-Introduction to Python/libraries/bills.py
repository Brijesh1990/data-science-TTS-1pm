menu = {
    "PANEER TIKKA MASALA": 350,
    "PANEER BHURJEE": 290,
    "MASALA DHOSA": 110,
    "CHEECE CHILLI MASALA DHOSA": 150,
    "CHINESE BHEL": 90,
    "MANCHURIYAN DRY": 110,
    "GUJARATI THALI FIXED": 250,
    "UTTAPAM": 100,
    "PANI PURI": 30,
    "SHAHI AALOO": 80
}

# Display menu
print("--------- MENU ---------")
for key, price in menu.items():
    print(f"{key} : ₹{price}")
print("------------------------")

total = 0

while True:
    choice = input("\nENTER ITEM NAME (OR DONE TO CANCEL ANYTIME): ").upper()

    if choice == "DONE":
        break

    elif choice in menu:
        qty = int(input("ENTER THE QUANTITY YOU WANT TO EAT: "))
        
        price = menu[choice]
        subtotal = price * qty
        total += subtotal

        print("\nITEM ADDED SUCCESSFULLY 😍")
        print(f"Item      : {choice}")
        print(f"Price     : ₹{price}")
        print(f"Quantity  : {qty}")
        print(f"Subtotal  : ₹{subtotal}")
        print(f"Total Bill: ₹{total}")

    else:
        print("ITEM UNAVAILABLE 😒")

print("\nTHANK YOU FOR YOUR VISIT 🙏")
print("PLEASE VISIT AGAIN ❤️")
print(f"FINAL AMOUNT TO PAY: ₹{total}")
