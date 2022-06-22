# Harry Cox
# Conveyor challenge

import random

final_products = []

class Factory():
    def __init__(self, belt_length):
        self.belt_length = belt_length
        self.belt = Belt(belt_length)
        self.workers = self.create_workers()

    # This adds a worker to either side of the belt (*2) then removes the from the last position (-2) and names the worker a number
    def create_workers(self):
        workers = []
        [workers.append(Worker("Worker" + str(pos))) for pos in range((self.belt_length * 2) - 2)]
        return workers


class Belt:
    def __init__(self, length):
        self.length = length
        self.conveyor = self.set_conveyor()

    # Creates a list of empty products to populate the conveyor
    def set_conveyor(self):
        conveyor = []
        for i in range(self.length):
            conveyor.append("Prod0")
        return conveyor


class Worker:
    def __init__(self, name):
        self.inventory = "Prod0"
        self.name = name


def random_product():
    prods = ["ProdA", "ProdB", "Prod0"]
    x = random.randint(0, 2)
    return prods[x]


def final_product_calc(to_remove):
    removed = to_remove.pop()       # Remove from end of list
    final_products.append(removed)  # then add to another list
    final_product_count = {i: final_products.count(i) for i in final_products}  # Count how many of each in final list
    return final_product_count


def y_turn(workery, z, belt):
    if workery.inventory == "ProdA":
        if belt[z] == "ProdA" or belt[z] == "Prod0" or belt[z] == "ProdF":
            pass
        else:
            workery.inventory = "ProdF"
            belt[z] = "Prod0"
    elif workery.inventory == "ProdB":
        if belt[z] == "ProdB" or belt[z] == "Prod0" or belt[z] == "ProdF":
            pass
        else:
            workery.inventory = "ProdF"
            belt[z] = "Prod0"
    elif workery.inventory == "Prod0":
        if belt[z] != "Prod0" or belt[z] != "ProdF":
            workery.inventory = belt[z]
            belt[z] = "Prod0"
    elif workery.inventory == "ProdF":
        if belt[z] == "Prod0":
            workery.inventory = "Prod0"
            belt[z] = "ProdF"


def production(steps, conveyor_length):
    f = Factory(conveyor_length)  # Create a factory
    b = f.belt.conveyor           # Get a reference to the conveyor
    w = f.workers                 # Get a reference to the workers

    for _ in range(steps):
        print(b)
        z = 0
        for x, y in zip(w[::2], w[1::2]):                                  # Get every 2 workers and name then x and y
            if x.inventory == "ProdA":                                     # If the worker is holding "Prod A"
                if b[z] == "ProdA" or b[z] == "Prod0" or b[z] == "ProdF":  # but the worker cant pick it up, let the opposite worker have a look
                    y_turn(y, z, b)
                else:                                                      # otherwise create "Prod F"
                    x.inventory = "ProdF"
                    b[z] = "Prod0"
            elif x.inventory == "ProdB":                                   # Same as above but if holding B
                if b[z] == "ProdB" or b[z] == "Prod0" or b[z] == "ProdF":
                    y_turn(y, z, b)
                else:
                    x.inventory = "ProdF"
                    b[z] = "Prod0"
            elif x.inventory == "Prod0":                                   # If the workers hands are empty
                if b[z] != "Prod0" or b[z] != "ProdF":
                    x.inventory = b[z]
                    b[z] = "Prod0"
            elif x.inventory == "ProdF":                                   # If the worker is holding a finished product
                if b[z] == "Prod0":
                    x.inventory = "Prod0"
                    b[z] = "ProdF"
            z = z + 1                                                      # Move on to the next conveyor position

        # Display what the workers are holding on each tick for readability
        for work in w:
            print(work.name + " inventory: " + work.inventory)


        b.insert(0, random_product())  # Add a new element to the start of the conveyor moving the rest of the products up by 1 index

        # Takes the list of final_product and displays how many of each have come off the end

        print("Products taken off end: " + str(final_product_calc(b)))

production(50, 3)










