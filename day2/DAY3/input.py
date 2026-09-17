shopping_list =[]
shopping_list.append("Milk")
shopping_list.append("Bread")
shopping_list.append("eggs")
shopping_list.append("Rice")
shopping_list.remove("Bread")
print(shopping_list)

item_to_check = "Eggs"
if item_to_check in shopping_list:
    print(f"{item_to_check}is on the list")

print("number of items:", len(shopping_list))

for i in range(len(shopping_list)):
 idx = i+1
 item = shopping_list[i]
 print(f"{idx}.{item}" )