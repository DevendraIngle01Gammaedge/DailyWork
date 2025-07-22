# inventry  = {}

inventry = {
    'iphone': {'quantity': 20, 'price': 200},
    'nokia': {'quantity': 22, 'price': 399},
    'mi': {'quantity': 21, 'price': 500},
    'samsung_galaxy_s24': {'quantity': 15, 'price': 899},
    'google_pixel_8': {'quantity': 18, 'price': 749},
    'oneplus_12': {'quantity': 25, 'price': 699},
    'macbook_air_m3': {'quantity': 10, 'price': 1099},
    'hp_spectre_x360': {'quantity': 12, 'price': 1299},
    'dell_xps_15': {'quantity': 8, 'price': 1599},
    'apple_watch_series_9': {'quantity': 30, 'price': 399},
    'samsung_galaxy_watch_6': {'quantity': 28, 'price': 299},
    'airpods_pro_2nd_gen': {'quantity': 40, 'price': 249},
    'sony_wh_1000xm5': {'quantity': 15, 'price': 349},
    'jbl_flip_6': {'quantity': 35, 'price': 129}
}


def inventryshwow():
    print("\nStudent Details:")
    print(f"Here are the following products in our inventry")

    for outer_key, outer_value in inventry.items():
        print(f"{outer_key}")
        for inner_key, inner_value in outer_value.items():
            print(f"  {inner_key}, {inner_value}")

def inventryupdate():
        print("Here you can easily update product details price,quantity")
        product = input("enter the product name here")
        if product.lower() in inventry.keys():
            print("select price , or quantity that you want to update")
            pointer = input("Enter the term")
            if pointer in ["price","quantity"]:
                try:
                    valuedata = float(input("Enter the data"))
                    inventry[product][pointer]=valuedata
                    print(f"Updated {product}'s {pointer} value to {valuedata}")
                except ValueError:
                    print("Enter a integer value ")
            else:
                print("Enter a valid term")
             
        

            
def inventrydelete():
    print("Here you can delete inventry products")
    deletepro = input("Enter product name")
    if deletepro.lower() in inventry.keys():
        del inventry[deletepro]
        print("It is deleted successfully from the inventry")
    else: 
        print("Enter the correct prodcut name")



if __name__=="__main__":
    while True:
        print("Welcome to the Inventry Management System")
        operation = input("Here you can do track products, quantities, and prices. \nEnter operation here (or type 'done' to finish).\n1. Show me the inventry items. \n2. Want to Update inventry's product Price or Quantity.\n3.want me to delete inventry product\n")
        try:
            if operation == "done":
                break
            elif int(operation) == 1:
                inventryshwow()
            elif int(operation) == 2:
                inventryupdate()
            elif int(operation) == 3:
                inventrydelete()
        except ValueError:
            print("Enter a valid operation selection")
            continue
    print("Thank you for using the inventry management system")