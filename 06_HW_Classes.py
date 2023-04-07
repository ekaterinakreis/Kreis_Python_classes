class Designer:

    def __init__(self, name, customer, contract, project, price):
        self._name = name
        self.customer = customer
        self.contract = contract
        self.project = project
        self.__price = price

    @property
    def get_name(self):
        return f"Hello, My name is {self._name}. I will be your designer"

    def new_customers(self):
        if self.customer == 0:
            return f"Search for new customers..."
        elif self.customer < 2:
            return f"I am ready for new contract!"
        else:
            return f"We will sign the contract later, sorry..."

    def make_contract(self):
        if self.contract:
            return f"Draw up and sign a contract!"

    def make_project(self):
        if self.project is True:
            return f"All is ready for a build!"
        else:
            return f"Need fix the project!"

    def set_price(self):
        return f"It is necessary to spend {self.__price} on construction work"


# designer1 = Designer("Antony", 3, 1, True, 20000)
# print(designer1.__dict__)
# print(designer1.get_name)
# print(designer1.new_customers())
# print(designer1.make_contract())
# print(designer1.make_project())
# print(designer1.set_price())


class Land_designer(Designer):
    '''Инкапсуляция атрибутов'''
    def __init__(self, name, customer, contract, project, price, plant):
        super().__init__(name, customer, contract, project, price)
        self.plant = plant

    def make_project(self):
        if self.customer > 5 and self.project is True:
            return f"We will our work in one month"
        elif self.customer >2 and self.project is True:
            return f"We will our work in two weeks"
        else:
            return f"Need fix the project!"


    def digging(self):
        return f'For planting plants, we will dig this area'

    def to_plant(self):
        return f"For project I`ll plant {self.plant}"

constracter = Land_designer("Roberto", 5, True, True, 10000, "Roses" )
print(constracter.get_name)
print(constracter.new_customers())
print(constracter.make_project())
print(constracter.set_price())
print(constracter.digging())
print(constracter.to_plant())


class Graphic_designer(Designer):

    def __init__(self, name, customer, contract, project, price, photoshop):
        super().__init__(name, customer, contract, project, price)
        self.photoshop = photoshop

    '''Reuse the method from the parent`s class'''
    def make_project(self):
        if self.project is True:
            return f"I will send the ready project for a print"
        else:
            return f"I need to sign a contract"


    def correction(self):
        if self.photoshop == 0:
            return "We does not need Photoshop"
        else:
            return "Let`s make some correction with Photoshop"

# freelancer = Graphic_designer("Mark", 0, 0, 0, 15000, 0)
# print(freelancer.get_name)
# print(freelancer.new_customers())
# print(freelancer.make_project())
# print(freelancer.correction())