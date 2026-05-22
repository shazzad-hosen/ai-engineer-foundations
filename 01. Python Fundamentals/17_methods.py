class Laptop:
    storage_type = "SSD"
    
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage
        
    # instance method -> can access instance attributes as well as class attributes
    def get_info(self): 
        print(f"laptop has {self.ram} RAM & {self.storage} {self.storage_type}")
        
    # class method -> can only access class attributes
    @classmethod # decorator function -> that makes the following method a class method
    def get_storage_type(cls):
        print(f"storage type is: {cls.storage_type}")
        
laptop1 = Laptop("128GB", "4TB")
laptop2 = Laptop("64GB", "1TB")

# calling instance methods
laptop1.get_info()
laptop2.get_info()

# calling class methods
laptop1.get_storage_type()
Laptop.get_storage_type()