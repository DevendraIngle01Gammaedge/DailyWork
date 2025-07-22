from inventryshow import inventryshow
from inventrydelete import inventrydelete
from inventryupdate import inventryupdate


if __name__=="__main__":
    while True:
        print("Welcome to the Inventry Management System")
        operation = input("Here you can do track products, quantities, and prices. \nEnter operation here (or type 'done' to finish).\n1. Show me the inventry items. \n2. Want to Update inventry's product Price or Quantity.\n3.want me to delete inventry product\n")
        try:
            if operation == "done":
                break
            elif int(operation) == 1:
                inventryshow()
            elif int(operation) == 2:
                inventryupdate()
            elif int(operation) == 3:
                inventrydelete()
        except ValueError:
            print("Enter a valid operation selection")
            continue
    print("Thank you for using the inventry management system")
    inventryshow()