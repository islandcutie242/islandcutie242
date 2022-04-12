import csv
class Phone:
    all = []
    def __init__(self, type, model, memory):
        # validation 
        assert memory >=0, f"Memory {memory} must be greater than 0"
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

    @classmethod
    def instantiate_from_csv(cls):
        with open('CellStore.csv', 'r') as f:
            reader = csv.DictReader(f)
            Phones = list(reader)

        for device in Phones:
            Phone(
                type=device.get('type'),
                model=device.get('model'),
                memory=int(device.get('memory')),
            )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # i.e 5.0, 6.0 etc
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False




print(Phone.is_integer(2))
#Phone.instantiate_from_csv()
# print(Phone.all)
