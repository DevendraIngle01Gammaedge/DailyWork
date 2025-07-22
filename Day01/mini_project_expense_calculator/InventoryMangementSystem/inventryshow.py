from inventrydic import inventry
def inventryshow():
    print(f"Here are the following products in our inventry")

    for outer_key, outer_value in inventry.items():
        print(f"{outer_key}",end =" ")
        for inner_key, inner_value in outer_value.items():
            print(f"{inner_key} = {inner_value}",end ="**")
        print(" ")
# if __name__=="__main__":
#     inventryshow()