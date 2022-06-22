# Conveyor challenge

The task was to create a conveyor belt with a certain amount of positions and a worker on either side of the position. 
The workers would then take either part A or part B off the conveyor and combine them to make a finished product.
Once a worker had the finished product they would put it back on to the conveyor to be counted at the end.
If a worker had already interacted with the conveyor position by either taking or placing an object, then the worker on the opposite side of them could not interact with that conveyor position.

To run the simulation create a factory object and pass it the length of the conveyor (plus one for to create a final slot to count the end products) and how times you would want the conveyor to move one space forward (ticks):

f = Factory(desired conveyor length + 1, ticks)

Then call the factorys built in production function to begin:

f.production()

Example output of f.production(3, 10):

In this example Worker 0 and worker 1 are around the first conveyor position. <br />
Worker 2 and worker 3 are around the second conveyor position. 

['PartB', 'PartA', 'PartB'] - How the conveyor begings <br />
Worker0 inventory: PartB   <br />
Worker1 inventory: Nothing <br />
Worker2 inventory: PartA   <br />
Worker3 inventory: Nothing <br />
Products taken off end: {'PartB': 1} <br />
['PartB', 'Nothing', 'Nothing'] <br />
Worker0 inventory: PartB <br />
Worker1 inventory: PartB<br />
Worker2 inventory: PartA <br />
Worker3 inventory: Nothing <br />
Products taken off end: {'PartB': 1, 'Nothing': 1} <br />
['Nothing', 'Nothing', 'Nothing'] <br />
Worker0 inventory: PartB <br />
Worker1 inventory: PartB <br />
Worker2 inventory: PartA <br />
Worker3 inventory: Nothing <br />
Products taken off end: {'PartB': 1, 'Nothing': 2} <br />
['PartB', 'Nothing', 'Nothing'] <br />
Worker0 inventory: PartB <br />
Worker1 inventory: PartB <br />
Worker2 inventory: PartA <br />
Worker3 inventory: Nothing <br />
Products taken off end: {'PartB': 1, 'Nothing': 3} <br />
['PartB', 'PartB', 'Nothing'] <br />
Worker0 inventory: PartB <br />
Worker1 inventory: PartB <br />
Worker2 inventory: Finished Product <br />
Worker3 inventory: Nothing <br />
Products taken off end: {'PartB': 1, 'Nothing': 4} <br />
['Nothing', 'PartB', 'Nothing'] <br />
Worker0 inventory: PartB <br />
Worker1 inventory: PartB <br />
Worker2 inventory: Finished Product <br />
Worker3 inventory: Nothing <br />
Products taken off end: {'PartB': 1, 'Nothing': 5} <br />
['PartA', 'Nothing', 'PartB'] <br />
Worker0 inventory: Finished Product <br />
Worker1 inventory: PartB <br />
Worker2 inventory: Nothing <br />
Worker3 inventory: Nothing <br />
Products taken off end: {'PartB': 2, 'Nothing': 5} <br />
['Nothing', 'Nothing', 'Finished Product'] <br />
Worker0 inventory: Nothing <br />
Worker1 inventory: PartB <br />
Worker2 inventory: Nothing <br />
Worker3 inventory: Nothing <br />
Products taken off end: {'PartB': 2, 'Nothing': 5, 'Finished Product': 1}
