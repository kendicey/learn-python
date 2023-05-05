class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it. (docstring)
    '''
    num_rooms = 5
    bathrooms = 2

    # self is a convention in python to point to any instance of the Class when called
    def getNum_rooms(self):
        # functionality to return the number of rooms in the house
        print(self.num_rooms)
        pass  # to signal python to continue execution without throwing an error

    # self is a convention in python to point to any instance of the Class when called
    def cost_evaluation(self, rate):
        # functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost


house = House()
house.getNum_rooms()    # 5
print(House.num_rooms)  # 5

House.num_rooms = 8
house.getNum_rooms()    # 8
print(House.num_rooms)  # 8

house.num_rooms = 7
house.getNum_rooms()    # 7
print(House.num_rooms)  # 8

print(house.cost_evaluation(1.5))   # 10.5
