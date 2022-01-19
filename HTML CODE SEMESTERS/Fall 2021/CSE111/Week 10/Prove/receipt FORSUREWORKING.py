# import csv file
import csv

def main():
    # product indexes from products.csv
    product_Num = 0
    product_Name = 1
    product_Price = 2
    # request indexes from request.csv
    request_Quantity = 1

    # find and return list of request items from products
    products = list_products("request.csv", "products.csv", product_Num, product_Name, product_Price)

    # finding quantity to total items on request
    quantity = calculate_req_quantitty("request.csv", request_Quantity)

    # calculate subtotal, tax, and total and return
    # total = calculate_total()

    # finding current time
    time = time_format()

    # receipt info text
    print("Inkom Emporium")

    print()
    print(products)

    print()
    print(f"Number of Items: {quantity}")
    print(f"Subtotal: {quantity}")
    print(f"Sales Tax: {quantity}")
    print(f"Total: {quantity}")

    print()
    print("Thank you for shopping at the Inkom Emporium.")
    print(time)


def list_products(file_req, file_pro, productNum, productName, productPri):
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    product_list_req = product_list_R(file_req, productNum)

    product_list_pro = product_list_P(file_pro, product_list_req)

    open(file_req, "rt")

    # for element in product_list_pro:
    #     if element in product_list_pro != element in product_list_req:
    #         print(product_list_pro[productName])
    # print(product_list_pro)

def product_list_R(file_req, productNum):
    with open(file_req, "rt") as csv_file_req:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file_req)

        # The first line of the CSV file contains column
        # headings and not information, so this statement
        # skips the first line of the CSV file.
        next(reader)

        list_product = []
        for row in reader:
            list_product.append(row[productNum])

        return list_product

def product_list_P(file_pro, product_list_req):
    with open(file_pro, "rt") as csv_file_pro:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file_pro)

        # The first line of the CSV file contains column
        # headings and not information, so this statement
        # skips the first line of the CSV file.
        next(reader)

        for row in reader:
            for key in product_list_req:
                if key == row[0]:
                    product = row[1]
                    price = row[2]
                    print(f"{product} {price}")






# calculate quantity
def calculate_req_quantitty(file_req, quantity):
    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(file_req, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column
        # headings and not information, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        quan_sum = 0
        for row in reader:
            quan = int(row[quantity])
            quan_sum += quan

    # Return the quantity.
    return quan_sum


# time format
def time_format():
    # Import the datetime class from the datetime
    # module so that it can be used in this program.
    from datetime import datetime

    # Call the now() method to get the current date and
    # time as a datetime object from the computer's clock.
    current_date_and_time = datetime.now()

    # Print the current day of the week and the current time.
    time = (f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")

    return time







if __name__ == "__main__":
    main()