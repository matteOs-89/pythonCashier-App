
def addproducts():
    basket ={}
    stillshopping = True
    while stillshopping:
        ques = input("Please type 'Y' if still shopping or 'Q' to Quit: ").lower()
        if ques == "y":
            product = input("Enter Product: ")
            quantity = int(input("Enter Quantity: "))
            basket.update({product: quantity})
        elif ques == "q":
            stillshopping = False
        else:
            print("please choose the right option")
    return basket



def getPrice(product, quantity):

    priceInfo = {"apple": 3,
                 "orange": 4,
                 "fish": 8,
                 "coke": 2,
                 "bread": 2,
                 "chicken": 5,
                 "egg": 1,
                 "onion": 3,
                 "pear": 2
                 }
    if product not in priceInfo.keys():
        priceInfo.update({product:len(product)})

    subtotal = priceInfo[product] * quantity

    print(f"{product}: £{str(priceInfo[product])} x {str(quantity)} = {str(subtotal)}")

    return subtotal

def memberDiscount(bill, membership):

    discount = 0

    if bill >= 25:
        if membership =="gold":
          bill = bill * 0.8
          discount = 20

        elif membership =="silver":
          bill = bill * 0.90
          discount = 10

        elif membership == "bronze":
          bill = bill * 0.95
          discount = 5

        elif membership == "none":
            bill = bill
            discount = 0

        print(f"{str(discount)} % off, {membership} membership total amount is £{str(bill)}")
    else:
        print("No discount unless bill is over £25 and hold a membership card")
    return bill


def makeBill(basket, membership):
    bill = 0
    for key, value in basket.items():
        bill += getPrice(key, value)
    bill = memberDiscount(bill, membership)
    print(f"Total amount is £{str(bill)}")


basket = addproducts()
membership = input("Enter customer membership: 'Gold', 'Silver', 'Bronze, or 'None' for none: ").lower()
makeBill(basket, membership)





