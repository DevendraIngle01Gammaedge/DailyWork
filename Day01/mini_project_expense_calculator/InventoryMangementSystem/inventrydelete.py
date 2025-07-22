from inventrydic import inventry
def inventrydelete():
    print("Here you can delete inventry products")
    deletepro = input("Enter product name")
    if deletepro.lower() in inventry.keys():
        del inventry[deletepro]
        print("It is deleted successfully from the inventry")
    else: 
        print("Enter the correct prodcut name")
if __name__=="__main__":
    inventrydelete()