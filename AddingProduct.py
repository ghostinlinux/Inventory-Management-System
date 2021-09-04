import json

read_data= open("Project/record.json",'r')
final_data = read_data.read()
read_data.close
final_rec = json.loads(final_data)
print(f"Your current Product >>>> \n\n {final_rec}")

print("\n")
print("\n")

# Adding Product
item_count = int(input("How many item you want to add >> "))
for i in range(item_count):
    product_id = input("Enter the Product id >> ")
    Name = input("Enter the Name >> ")
    Price = int(input("Enter the price >> "))
    Quantity = int(input("Enter the quantity >> "))
    Discount = int(input("Enter the discount >> "))
    Gst = int(input("Enter the gst >> "))

    add_more = {product_id : {'name' : Name, 'price' : Price, 'quantity' : Quantity, 'discount' : Discount, 'gst' : Gst}}

    final_rec.update(add_more)


dump_data = json.dumps(final_rec)
write_data = open("Project/record.json",'w')
write_data.write(dump_data)
write_data.close