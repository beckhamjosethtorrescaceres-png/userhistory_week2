
def agg():
 vn = True
 while vn :
            product = input("Enter the product name: ").strip()
            try :
                if product:
                    break
                else:
                    print("The product name cannot be empty..")
            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user. Exiting...")
 vp = True
 while vp :
            price = (input("Enter the product price: ")).strip()
            try:
                price = float(price)
                if price > 0:
                    vp = False
                else:
                    print(" The price must be greater than 0.")
            except ValueError:
                print(" You must enter a valid number for the price.")
                continue
            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user. Exiting...")
                continue
 vq= True
 while vq :
            quantity = (input("Enter the quantity of the product: "))
            try:
                quantity = int(quantity)
                if quantity > 0:
                    vq = False
                else:
                    print(" The quantity must be greater than 0.")
            except ValueError:
                print(" You must enter a valid integer for the quantity.")
                continue
            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user. Exiting...")
                continue

            product_info = {
                "name": product,
                "price": price,
                "quantity": quantity
            }
            return product_info