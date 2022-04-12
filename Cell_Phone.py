from Phone import Phone

class Cell_Phone(Phone):
    all = []
    def __init__(self, type, model, memory, quantity=0, broken_phones=0):
        #call to super function to have access to all artributes / methods
        super().__init__(
            type, model, memory,
        )
        # validation 
        assert quantity>=0, f"Quantity {quantity} must be equal or greater than zero"
        assert broken_phones>=0, f"Broken Phones {broken_phones} must be greater than or equal to zero"
        self.type = type
        self.model = model
        self.memory = memory
        self.quantity = quantity
        self.broken_phones = broken_phones

        #items to execute
        #Cell_Phone.all.append(self)