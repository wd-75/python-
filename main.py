class Laptop:
    def __init__(self, brand, model, price, ram, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.ram = ram       
        self.storage = storage  


    def info(self):
        
        print(f" product name {self.brand} | product model{self.model} | RAM: {self.ram}GB | Storage: {self.storage}GB | Price: ${self.price}")
    
    """done """
    
p1 = Laptop("Dell", "XPS 13", 99999, 16, 512)
p2 = Laptop("Apple", "MacBook Pro", 129999, 32, 1024)
p1.info()
p2.info()


