# instance methods
class Laptop:
    storage_type = "SSD"
    
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage
        
    def get_info(self): # instance method -> can access instance attributes and class attributes 
        print(f"laptop has {self.ram} RAM & {self.storage} {self.storage_type}")
        
laptop1 = Laptop("128GB", "4TB")
laptop2 = Laptop("64GB", "1TB")
laptop3 = Laptop("32GB", "512GB")

laptop1.get_info()
laptop2.get_info()
laptop3.get_info()