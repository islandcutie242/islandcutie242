class Phone:
    all = []
    def __init__(self, type, model, memory):
        self.type = type
        self.model = model
        self.memory = memory

        #items to execute
        Phone.all.append(self)

    def call_numbers(self):
        print(f"{type} is making a call.")

    def receiving_calls(self):
        print(f"{type} is receiving a call")

    def __repr__(self):
        return f"Phone('{self.type}','{self.model}','{self.memory}')"


p1 = Phone("Iphone","11x", 64)
p2 = Phone("Samsung", "Galaxy 20", 128)
p3 = Phone("Acatel", "SG10", 34)
p4 = Phone("Huwhei", "15", 64)
p5 = Phone("Samsung", "Galaxy 11", 128)


print(Phone.all)
