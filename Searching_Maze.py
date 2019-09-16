from Resources import *

# maze = [[0,0,0,0,0],  where values are :
#         [1,1,0,0,0],  x : Goal Cell
#         [0,1,0,0,1],  0 : Empty Cell
#         [0,0,0,0,1],  1 : Wall Cell
#         [0,0,x,0,0]]
#
# where each cell is Cell(cell value , extra movement cost)

maze = [[Cell( 0 , 0), Cell( 0 , 0), Cell( 0 , 1), Cell( 0 , 0), Cell( 0 , 1)],
        [Cell( 1 , 0), Cell( 1 , 0), Cell( 0 , 2), Cell( 0 , 1), Cell( 0 , 2)],
        [Cell( 0 , 2), Cell( 1 , 0), Cell( 0 , 3), Cell( 0 , 0), Cell( 1 , 0)],
        [Cell( 0 , 0), Cell( 0 , 2), Cell( 0 , 1), Cell( 0 , 1), Cell( 1 , 0)],
        [Cell( 0 , 1), Cell( 0 , 0), Cell('x', 3), Cell( 0 , 1), Cell( 0 , 0)]]

num_rows = len(maze)
num_columns = len(maze[0])


def depth_first_search(x, y):  # if there is a tie, priority for child nodes will be in clockwise orientation (North > East > South > West)
    explored_list = list()
    frontier_stack = Stack()  # to choose between frontiers
    frontier_list = list()  # to avoid choosing element that already in frontier

    loop = True

    while loop:
        maze[x][y].coordinates = [x, y]
        explored_list.append([x, y])

        if maze[x][y].cell_value == 'x':  # if the goal cell is found
            path = list()
            temp_cell = maze[x][y]
            total_cost = 0  # to print total movement points
            while temp_cell is not None:    # to track the path from goal to start with inspecting its parent cell
                path.append(temp_cell.coordinates)
                total_cost = total_cost + temp_cell.cost
                temp_cell = temp_cell.parent_cell
            path.reverse()
            print("Depth First Search\n"
                  "------------------")
            print("Path with total cost of", total_cost, "movement point(s) and in", len(path), "tile(s):")
            print(' --> '.join(map(str, path)))
            print("Explored cells :")
            print(*explored_list, sep=', ')
            print("\n")
            loop = False

        else:   # Begin to check each neighboring cell to add to the frontier
                # since dfs works with stack, order of if blocks are reversed to keep clockwise priority
            if ((y-1) >= 0) and (maze[x][y-1].cell_value != 1) and ([x, y-1] not in explored_list) and ([x, y-1] not in frontier_list):  # West Cell
                frontier_stack.push([x, y-1])
                frontier_list.append([x, y-1])
                maze[x][y-1].parent_cell = maze[x][y]

            if ((x+1) <= (num_rows-1)) and (maze[x+1][y].cell_value != 1) and ([x+1, y] not in explored_list) and ([x+1, y] not in frontier_list):  # South Cell
                frontier_stack.push([x+1, y])
                frontier_list.append([x+1, y])
                maze[x+1][y].parent_cell = maze[x][y]

            if ((y+1) <= (num_columns-1)) and (maze[x][y+1].cell_value != 1) and ([x, y+1] not in explored_list) and ([x, y+1] not in frontier_list):  # East Cell
                frontier_stack.push([x, y+1])
                frontier_list.append([x, y+1])
                maze[x][y+1].parent_cell = maze[x][y]

            if ((x-1) >= 0) and (maze[x-1][y].cell_value != 1) and ([x-1, y] not in explored_list) and ([x-1, y] not in frontier_list):  # North Cell
                frontier_stack.push([x-1, y])
                frontier_list.append([x-1, y])
                maze[x-1][y].parent_cell = maze[x][y]

            if frontier_stack.is_empty():
                print("There is no path to the goal.")
                loop = False

            else:
                next_location = frontier_stack.pop()  # returns the next [x, y] from top of the frontier_stack
                x = next_location[0]
                y = next_location[1]


def breadth_first_search(x, y):  # if there is a tie, priority for child nodes will be in clockwise orientation (North > East > South > West)
    explored_list = list()
    frontier_queue = Queue()  # to choose between frontiers
    frontier_list = list()  # to avoid choosing element that already in frontier

    loop = True

    while loop:
        maze[x][y].coordinates = [x, y]
        explored_list.append([x, y])

        if maze[x][y].cell_value == 'x':  # if the goal cell is found
            path = list()
            temp_cell = maze[x][y]
            total_cost = 0  # to print total movement points
            while temp_cell is not None:    # to track the path from goal to start with inspecting its parent cell
                path.append(temp_cell.coordinates)
                total_cost = total_cost + temp_cell.cost
                temp_cell = temp_cell.parent_cell
            path.reverse()
            print("Breadth First Search\n"
                  "--------------------")
            print("Path with total cost of", total_cost, "movement point(s) and in", len(path), "tile(s):")
            print(' --> '.join(map(str, path)))
            print("Explored cells :")
            print(*explored_list, sep=', ')
            print("\n")
            loop = False

        else:   # Begin to check each neighboring cell to add to the frontier
            if ((x-1) >= 0) and (maze[x-1][y].cell_value != 1) and ([x-1, y] not in explored_list) and ([x-1, y] not in frontier_list):  # North Cell
                frontier_queue.enqueue([x - 1, y])
                frontier_list.append([x - 1, y])
                maze[x - 1][y].parent_cell = maze[x][y]

            if ((y+1) <= (num_columns-1)) and (maze[x][y+1].cell_value != 1) and ([x, y+1] not in explored_list) and ([x, y+1] not in frontier_list):  # East Cell
                frontier_queue.enqueue([x, y+1])
                frontier_list.append([x, y+1])
                maze[x][y+1].parent_cell = maze[x][y]

            if ((x+1) <= (num_rows-1)) and (maze[x+1][y].cell_value != 1) and ([x+1, y] not in explored_list) and ([x+1, y] not in frontier_list):  # South Cell
                frontier_queue.enqueue([x+1, y])
                frontier_list.append([x+1, y])
                maze[x+1][y].parent_cell = maze[x][y]

            if ((y-1) >= 0) and (maze[x][y-1].cell_value != 1) and ([x, y-1] not in explored_list) and ([x, y-1] not in frontier_list):  # West Cell
                frontier_queue.enqueue([x, y-1])
                frontier_list.append([x, y-1])
                maze[x][y-1].parent_cell = maze[x][y]

            if frontier_queue.is_empty():
                print("There is no path to the goal.")
                loop = False

            else:
                next_location = frontier_queue.dequeue()  # returns the next [x, y] from head of the queue
                x = next_location[0]
                y = next_location[1]


def uniform_cost_search(x, y):
    explored_list = list()
    frontier_queue = PriorityQueue()  # to choose between frontiers
    frontier_list = list()  # to avoid choosing element that already in frontier

    loop = True

    while loop:
        maze[x][y].coordinates = [x, y]
        explored_list.append([x, y])

        if maze[x][y].cell_value == 'x':  # if the goal cell is found
            path = list()
            temp_cell = maze[x][y]
            total_cost = 0  # to print total movement points
            while temp_cell is not None:  # to track the path from goal to start with inspecting its parent cell
                path.append(temp_cell.coordinates)
                total_cost = total_cost + temp_cell.cost
                temp_cell = temp_cell.parent_cell
            path.reverse()
            print("Uniform Cost Search\n"
                  "-------------------")
            print("Path with total cost of", total_cost, "movement point(s) and in", len(path), "tile(s):")
            print(' --> '.join(map(str, path)))
            print("Explored cells :")
            print(*explored_list, sep=', ')
            print("\n")
            loop = False

        else:   # Begin to check each neighboring cell to add to the frontier
            if ((x-1) >= 0) and (maze[x-1][y].cell_value != 1) and ([x-1, y] not in explored_list) and ([x-1, y] not in frontier_list):  # North Cell
                maze[x-1][y].calculate_cumulative_cost(maze[x][y])
                frontier_queue.enqueue(maze[x-1][y])
                frontier_list.append([x-1, y])
                maze[x-1][y].parent_cell = maze[x][y]
                maze[x-1][y].coordinates = [x-1, y]

            if ((y+1) <= (num_columns-1)) and (maze[x][y+1].cell_value != 1) and ([x, y+1] not in explored_list) and ([x, y+1] not in frontier_list):  # East Cell
                maze[x][y+1].calculate_cumulative_cost(maze[x][y])
                frontier_queue.enqueue(maze[x][y+1])
                frontier_list.append([x, y+1])
                maze[x][y+1].parent_cell = maze[x][y]
                maze[x][y+1].coordinates = [x, y+1]

            if ((x+1) <= (num_rows-1)) and (maze[x+1][y].cell_value != 1) and ([x+1, y] not in explored_list) and ([x+1, y] not in frontier_list):  # South Cell
                maze[x+1][y].calculate_cumulative_cost(maze[x][y])
                frontier_queue.enqueue(maze[x+1][y])
                frontier_list.append([x+1, y])
                maze[x+1][y].parent_cell = maze[x][y]
                maze[x+1][y].coordinates = [x+1, y]

            if ((y-1) >= 0) and (maze[x][y-1].cell_value != 1) and ([x, y-1] not in explored_list) and ([x, y-1] not in frontier_list):  # West Cell
                maze[x][y-1].calculate_cumulative_cost(maze[x][y])
                frontier_queue.enqueue(maze[x][y-1])
                frontier_list.append([x, y-1])
                maze[x][y-1].parent_cell = maze[x][y]
                maze[x][y-1].coordinates = [x, y-1]

            if frontier_queue.is_empty():
                print("There is no path to the goal.")
                loop = False

            else:
                next_location = frontier_queue.dequeue().coordinates
                x = next_location[0]
                y = next_location[1]

    for ix in range(num_rows):  # resetting all cells to their original values (cumulative costs)
        for iy in range(num_columns):
            maze[ix][iy].reset_values()


def a_star_search(x, y, admissible):    # enter True for admissible search, False for inadmissable search
    explored_list = list()
    frontier_queue = PriorityQueue()  # to choose between frontiers
    frontier_list = list()  # to avoid choosing element that already in frontier

    loop = False
    is_there_goal = False
    goal_cell_coordinates = None

    for ix in range(num_rows):  # since it's informed search, program should know the coordinates of the goal cell (not the shortest path but its existence)
        for iy in range(num_columns):
            if maze[ix][iy].cell_value == 'x':
                goal_cell_coordinates = [ix, iy]
                is_there_goal = True
                loop = True

    while loop:
        maze[x][y].coordinates = [x, y]
        explored_list.append([x, y])

        if maze[x][y].cell_value == 'x':  # if the goal cell is found
            path = list()
            temp_cell = maze[x][y]
            total_cost = 0     # to print total movement points (without heuristic)
            while temp_cell is not None:  # to track the path from goal to start with inspecting its parent cell
                path.append(temp_cell.coordinates)
                total_cost = total_cost + temp_cell.cost
                temp_cell = temp_cell.parent_cell
            path.reverse()
            print("A* Search\n"
                  "---------")
            print("Path with total cost of", total_cost, "movement point(s) and in", len(path), "tile(s):")
            print(' --> '.join(map(str, path)))
            print("Explored cells :")
            print(*explored_list, sep=', ')
            print("\n")
            loop = False

        else:
            # Begin to check each neighboring cell to add to the frontier
            if ((x-1) >= 0) and (maze[x-1][y].cell_value != 1) and ([x-1, y] not in explored_list) and ([x-1, y] not in frontier_list):  # North Cell
                maze[x-1][y].parent_cell = maze[x][y]
                maze[x-1][y].coordinates = [x-1, y]
                if admissible:  # according to the parametric value, it will calculate either an admissible heuristic or inadmissable heurisic
                    maze[x-1][y].admissible_heuristic(goal_cell_coordinates)
                else:
                    maze[x-1][y].inadmissible_heuristic(maze)
                maze[x-1][y].calculate_cumulative_cost_with_heuristic(maze[x][y])
                frontier_queue.enqueue(maze[x-1][y])
                frontier_list.append([x-1, y])

            if ((y+1) <= (num_columns-1)) and (maze[x][y+1].cell_value != 1) and ([x, y+1] not in explored_list) and ([x, y+1] not in frontier_list):  # East Cell
                maze[x][y+1].parent_cell = maze[x][y]
                maze[x][y+1].coordinates = [x, y+1]
                if admissible:
                    maze[x][y+1].admissible_heuristic(goal_cell_coordinates)
                else:
                    maze[x][y+1].inadmissible_heuristic(maze)
                maze[x][y+1].calculate_cumulative_cost_with_heuristic(maze[x][y])
                frontier_queue.enqueue(maze[x][y+1])
                frontier_list.append([x, y+1])

            if ((x+1) <= (num_rows-1)) and (maze[x+1][y].cell_value != 1) and ([x+1, y] not in explored_list) and ([x+1, y] not in frontier_list):  # South Cell
                maze[x+1][y].parent_cell = maze[x][y]
                maze[x+1][y].coordinates = [x+1, y]
                if admissible:
                    maze[x+1][y].admissible_heuristic(goal_cell_coordinates)
                else:
                    maze[x+1][y].inadmissible_heuristic(maze)
                maze[x+1][y].calculate_cumulative_cost_with_heuristic(maze[x][y])
                frontier_queue.enqueue(maze[x+1][y])
                frontier_list.append([x+1, y])

            if ((y-1) >= 0) and (maze[x][y-1].cell_value != 1) and ([x, y-1] not in explored_list) and ([x, y-1] not in frontier_list):  # West Cell
                maze[x][y-1].parent_cell = maze[x][y]
                maze[x][y-1].coordinates = [x, y-1]
                if admissible:
                    maze[x][y-1].admissible_heuristic(goal_cell_coordinates)
                else:
                    maze[x][y-1].inadmissible_heuristic(maze)
                maze[x][y-1].calculate_cumulative_cost_with_heuristic(maze[x][y])
                frontier_queue.enqueue(maze[x][y-1])
                frontier_list.append([x, y-1])

            if frontier_queue.is_empty():
                print("There is no path to the goal.")  # there is a goal cell, but program can't reach it
                loop = False

            else:
                next_location = frontier_queue.dequeue().coordinates
                x = next_location[0]
                y = next_location[1]

    if is_there_goal:
        for ix in range(num_rows):  # resetting all cells to their original values (cumulative costs and heuristics)
            for iy in range(num_columns):
                maze[ix][iy].reset_values()

    else:
        print("There is no goal.")


