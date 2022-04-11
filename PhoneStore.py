class Phone:
    def __init__(self, type, model, memory):
        self.type = type
        self.model = model
        self.memory = memory

    def call_numbers(self):
        print(f"{type} is making a call.")

    def receiving_calls(self):
        print(f"{type} is receiving a call")


p1 = Phone("Iphone","11x", 64)
p2 = Phone("Samsung", "Galaxy 20", 128)


p1.receiving_calls()
p2.call_numbers()
