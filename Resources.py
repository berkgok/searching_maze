class Cell:
    def __init__(self, cell_value, cost):
        self.cell_value = cell_value
        self.cost = cost
        self.heuristic = 0
        self.parent_cell = None
        self.coordinates = None
        self.cumulative_cost = cost

    def calculate_cumulative_cost(self, cell):
        self.cumulative_cost = self.cost + cell.cumulative_cost

    def calculate_cumulative_cost_with_heuristic(self, cell):
        self.cumulative_cost = self.cost + self.heuristic + cell.cumulative_cost

    def admissible_heuristic(self, goal_cell_coordinate):   # sum of coordinate value differences(both x and y) between current and goal cell
        self.heuristic = ((abs(goal_cell_coordinate[0] - self.coordinates[0])) + (abs(goal_cell_coordinate[1] - self.coordinates[1])))

    def inadmissible_heuristic(self, maze):  # ((1 + sum of current cell's coordinate values) * number of cells in the maze)
        self.heuristic = ((1 + (self.coordinates[0] + self.coordinates[1])) * (len(maze) * len(maze[0])))

    def reset_values(self):
        self.heuristic = 0
        self.cumulative_cost = self.cost


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class PriorityQueue:    # minimum value has the highest priority
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, cell):    # item will be a cell
        if self.items:
            for index in range(len(self.items)):
                if cell.cumulative_cost >= self.items[index].cumulative_cost:
                    self.items.insert(index, cell)
                    break
                if index == len(self.items)-1:
                    self.items.append(cell)
        else:
            self.items.append(cell)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

