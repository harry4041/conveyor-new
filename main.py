# Harry Cox
# Conveyor challenge

import random

final_products = []

class Factory():
    def __init__(self, belt_length, steps):
        self.belt_length = belt_length
        self.belt = Belt(belt_length)
        self.workers = self.create_workers()
        self.steps = steps

    # This adds a worker to either side of the belt (*2) then removes the from the last position (-2) and names the worker a number
    def create_workers(self):
        workers = []
        [workers.append(Worker("Worker" + str(pos))) for pos in range((self.belt_length * 2) - 2)]
        return workers

    def final_product_calc(self, to_remove):
        removed = to_remove.pop()  # Remove from end of list
        final_products.append(removed)  # then add to another list
        final_product_count = {i: final_products.count(i) for i in
        final_products}  # Count how many of each in final list
        return final_product_count

    def production(self):
        belt = self.belt.conveyor  # Get a reference to the conveyor
        w = self.workers  # Get a reference to the workers

        # Just to make things clearer for the user
        print("A conveyor with the length of " + str(self.belt_length) + ".")
        print("Thats " + str(self.belt_length - 1) + " production slots and 1 final slot for counting what comes off  of the end.")
        print("producing for " + str(self.steps) + " steps.")
        print("Thats two workers on either side of the conveyor (" + (str(len(self.workers))) + " total workers.")

        for _ in range(self.steps):
            print(belt)
            conveyor_position = 0
            for worker_1, worker_2 in zip(w[::2], w[1::2]):  # Get every 2 workers and name then x and y
                if worker_1.inventory == "ProdA":  # If the worker is holding "Prod A"
                    if belt[conveyor_position] == "ProdA" or belt[conveyor_position] == "Prod0" or belt[
                        conveyor_position] == "ProdF":  # but the worker cant pick it up, let the opposite worker have a look
                        worker_1.worker_2_turn(worker_2, conveyor_position, belt)
                    else:  # otherwise create "Prod F"
                        worker_1.inventory = "ProdF"
                        belt[conveyor_position] = "Prod0"
                elif worker_1.inventory == "ProdB":  # Same as above but if holding B
                    if belt[conveyor_position] == "ProdB" or belt[conveyor_position] == "Prod0" or belt[conveyor_position] == "ProdF":
                        worker_1.worker_2_turn(worker_2, conveyor_position, belt)
                    else:
                        worker_1.inventory = "ProdF"
                        belt[conveyor_position] = "Prod0"
                elif worker_1.inventory == "Prod0":  # If the workers hands are empty
                    if belt[conveyor_position] != "Prod0" or belt[conveyor_position] != "ProdF":
                        worker_1.inventory = belt[conveyor_position]
                        belt[conveyor_position] = "Prod0"
                elif worker_1.inventory == "ProdF":  # If the worker is holding a finished product
                    if belt[conveyor_position] == "Prod0":
                        worker_1.inventory = "Prod0"
                        belt[conveyor_position] = "ProdF"
                conveyor_position = conveyor_position + 1  # Move on to the next conveyor position

            # Display what the workers are holding on each tick for readability
            for work in w:
                print(str(work.name) + " inventory: " + str(work.inventory))

            belt.insert(0, Product().name)  # Add a new element to the start of the conveyor moving the rest of the products up by 1 index

            # Takes the list of final_product and displays how many of each have come off the end
            print("Products taken off end: " + str(f.final_product_calc(belt)))


class Belt:
    def __init__(self, length):
        self.length = length
        self.conveyor = self.set_conveyor()

    # Creates a list of empty products to populate the conveyor
    def set_conveyor(self):
        conveyor = []
        for i in range(self.length):
            conveyor.append(Product().name)
        return conveyor


class Worker:
    def __init__(self, name):
        self.inventory = "Prod0"
        self.name = name

    def worker_2_turn(self, worker, z, belt):
        if worker.inventory == "ProdA":
            if belt[z] == "ProdA" or belt[z] == "Prod0" or belt[z] == "ProdF":
                pass
            else:
                worker.inventory = "ProdF"
                belt[z] = "Prod0"
        elif worker.inventory == "ProdB":
            if belt[z] == "ProdB" or belt[z] == "Prod0" or belt[z] == "ProdF":
                pass
            else:
                worker.inventory = "ProdF"
                belt[z] = "Prod0"
        elif worker.inventory == "Prod0":
            if belt[z] != "Prod0" or belt[z] != "ProdF":
                worker.inventory = belt[z]
                belt[z] = "Prod0"
        elif worker.inventory == "ProdF":
            if belt[z] == "Prod0":
                worker.inventory = "Prod0"
                belt[z] = "ProdF"


class Product:
    def __init__(self):
        self.name = self.random_product()

    def random_product(self):
        prods = ["ProdA", "ProdB", "Prod0"]
        x = random.randint(0, 2)
        return prods[x]


f = Factory(3, 50)
f.production()
