import json
import random

def choose_choice():
    what_to_do = int(input("Enter 0 for adding items 'or' 1 for Selling Item >> "))
    if what_to_do == 0:
        Adding_Data()
    elif what_to_do == 1:
        Selling_Product()


def Adding_Data():
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



def Selling_Product():
    read_data= open("Project/record.json",'r')
    final_data = read_data.read()
    read_data.close
    final_rec = json.loads(final_data)
    print(f"Available Product >>>> \n\n {final_rec}")

    print("\n")
    print("\n")

    user_product_id = input("Select Product id from given list >> ")
    user_quantity = int(input("How many item you want to buy >> "))

    for i in final_rec:
        if user_quantity > 0 and final_rec[i]['quantity']>=user_quantity:
            if i == user_product_id:
                print("*"*50)
                print(f"Name : {final_rec[i]['name']}")
                print(f"Price : {final_rec[i]['price']*user_quantity}")
                print(f"Discount : {final_rec[i]['discount']}%")
                print(f"GST : {final_rec[i]['gst']}%")
                dis = ((final_rec[i]['price']*user_quantity)*final_rec[i]['discount'])/100
                normal_discount_value = (final_rec[i]['price']*user_quantity) - dis
                gst_value = (normal_discount_value*final_rec[i]['gst'])/100
                total_bill = normal_discount_value + gst_value
                print(f"Total Billing : {total_bill}")
                print("*"*50)

            # update final_rec

                rest_quantity = final_rec[i]['quantity'] - user_quantity
                update_final_rec = {i : {'name' : final_rec[i]['name'], 'price' : final_rec[i]['price'], 'quantity' : rest_quantity, 'discount' : final_rec[i]['discount'] ,'gst' : final_rec[i]['gst'], }}

                final_rec.update(update_final_rec)
                
                dump_data = json.dumps(final_rec)
                write_data = open("Project/record.json",'w')
                write_data.write(dump_data)
                write_data.close

                # selling details
            
                read_data1= open("Project/selled data.json",'r')
                final_data1 = read_data1.read()
                read_data1.close
                final_rec1 = json.loads(final_data1)

                with_transaction_id = {random.randint(7777777,9999999999) : {'Item sell' : final_rec[i], 'Quantity of item selled' : user_quantity , 'Total Billing' : total_bill}}
                final_rec1.update(with_transaction_id)
                selled_item = json.dumps(final_rec1)
                write_selled_data = open("Project/selled data.json", 'w')
                write_selled_data.write(selled_item)
                write_selled_data.close
                
        else:
            if final_rec[i]['quantity']<=user_quantity:
                print(f"We have only {final_rec[i]['quantity']} items")
                break
            elif user_quantity > 0:
                print("Buy atleast one item")
                break


choose_choice()
