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
for key, price in menu.items():
   print(f"{key} : ₹{price}")
print("------------------------")

total = 0

while True:
    choice = input("ENTER ITEM NAME (OR DONE TO CANCEL ANYTIME): ").upper()

    if choice == "DONE":
        #print("THANK YOU FOR YOUR VISIT")
        break

    elif choice in menu:
        qty = int(input("ENTER THE QUANTITY YOU WANT TO EAT: "))
        cost = menu[choice] * qty
        total =total + cost 
        print("ITEM ADDED SUCCESSFULLY 😍")
    

    else:
        print("ITEM UNAVAILABLE 😒")


print(f"FINAL AMOUNT TO PAY: ₹{total}")
print("\nTHANK YOU FOR YOUR VISIT 🙏")
print("PLEASE VISIT AGAIN ❤️")


