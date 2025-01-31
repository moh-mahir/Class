class pharmacy_items:
    # class properties
    available = {}
    needed = []
    check_needed=0

    def __init__(self, name, quantity, price):
        self.name = name
        self.price = price
        self.quantity = quantity
        for i in range(len(pharmacy_items.needed)):
            if name == pharmacy_items.needed[i]:
                pharmacy_items.needed.pop(i)
        pharmacy_items.available [name]={"name": name, "quantity": quantity}


    def sell(self, name, quantity):
        if self.name == name:
            if self.quantity >= quantity:
                self.quantity -= quantity
                print(f" sold {quantity} of {self.name} for {quantity * self.price}$")
                pharmacy_items.available[name]={"name": name, "quantity": self.quantity}
                pharmacy_items.check_sell=1
                
            if self.quantity <= 10 :
                for i in range(len(pharmacy_items.needed)):
                    if name == pharmacy_items.needed[i]:
                        pharmacy_items.check_needed=1
                if pharmacy_items.check_needed==0:
                    pharmacy_items.needed.append(name)
                if self.quantity <= quantity:
                    print("quantity is not available")              
                
                                   
                    
        else:
            print("unavailable")
        
paracetamol = pharmacy_items("paracetamol", 100, 199)
panadol= pharmacy_items("panadol", 13, 99)
insulin=pharmacy_items('insulin',3,1)
print("")
paracetamol.sell("paracetamol", 5)
panadol.sell("panadol", 5)
insulin.sell("insulin", 5)
print("")
print(pharmacy_items.needed)
print(pharmacy_items.available)