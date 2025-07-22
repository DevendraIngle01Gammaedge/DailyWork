from inventrydic import inventry
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
if __name__=="__main__":
     inventryupdate()