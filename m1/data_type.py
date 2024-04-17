product_title = "coffee"  # str it's string
quantity = 10  #  int it's interger
price = 4.5  #  float
colour = None  #  nontype
is_strong = True  #  bool it's boolean

products = ["apple", "water", "coffee"]  #  list have access by index, mutable
order = (1, "coffee", 5, 6.99)  #  tuple, have access by index, unmutable
suppliers = {"ATB": "coffee", "oko": "fuel"}  #  dict it's dictionery
customers = {"Bob", "Nick", "Neal", "Bob"}  #  set 


for product in products: 
    if product=="coffee":
        print("we find coffee")
    else:
        print("try again")


product = suppliers["ATB"]
print(product)


print(customers)

