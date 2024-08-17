# -*- coding: utf-8 -*-
"""
ENPM661 Project 1
Breadth First search algorithm for 8-puzzle problem
"""

import numpy as np

# The starting configuration of the puzzle (2D numpy array)
start = np.array([[1, 0, 8], [4, 3, 2], [5, 7, 6]])

# The desired configuration or the end goal of the puzzle (2D numpy array)
desired = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])

# Function to get the position of the blank tile (represented by 0 here)
def get_zero_position(state):
    return np.where(state == 0)

# Function to move the blank tile to the left
def move_left(state):
    zero = get_zero_position(state)
    if zero[1] == 0:
        return None
    new_state = state.copy()
    new_state[zero[0], zero[1]] = state[zero[0], zero[1] - 1]
    new_state[zero[0], zero[1] - 1] = 0
    return new_state

# Function to move the blank tile to the right
def move_right(state):
    zero = get_zero_position(state)
    if zero[1] == 2:
        return None
    new_state = state.copy()
    new_state[zero[0], zero[1]] = state[zero[0], zero[1] + 1]
    new_state[zero[0], zero[1] + 1] = 0
    return new_state

# Function to move the blank tile up
def move_up(state):
    zero = get_zero_position(state)
    if zero[0] == 0:
        return None
    new_state = state.copy()
    new_state[zero[0], zero[1]] = state[zero[0] - 1, zero[1]]
    new_state[zero[0] - 1, zero[1]] = 0
    return new_state

# Function to move the blank tile down
def move_down(state):
    zero = get_zero_position(state)
    if zero[0] == 2:
        return None
    new_state = state.copy()
    new_state[zero[0], zero[1]] = state[zero[0] + 1, zero[1]]
    new_state[zero[0] + 1, zero[1]] = 0
    return new_state

# Function to get the action type - This is used to store the list of actions performed
def get_move_type(action):
  if action==move_left:
    return "left"
  if action==move_right:
    return "right"
  if action==move_up:
    return "up"
  if action==move_down:
    return "down"

# "states" is a list of tuples.
# The length of each tuple is 4 and it contains the following information:
# 1. The puzzle configuration/node
# 2. The history of moves performed to attain that configuration/node
# 3. The index number of the configuration/node
# 4. The index of the parent configuration/node

states = [(start, [] , 1 , 0 )]

# "track" keeps a track of all the configurations explored. It is also a list of tuples.
track = states.copy()

# "possible actions" contains a list of actions that can be performed on the node.
possible_actions=[move_left, move_right, move_up, move_down]

# "visited" is a set of tuples.
# It is similar to "track" but "track" is a list of tupeles containing node, action and index information....
# ....whereas "visited" is a set of tupeles only containing the node configuration information
visited = set()

# "index" is used to keep a track of node index
index=1

# "searching" is a bool which is true while the code is searching for the solution and false when the goal is achieved
searching=True

# Loop that runs while the answer is being searched
while searching:

  # the index 0 element of "states" is poped and its values are stored in variables
  state, history , current_index, parent_index = states.pop(0)

  # loop to perform actions on the current node
  for move_function in possible_actions:
      new_state = move_function(state)
      move_name = get_move_type(move_function)

      # Condition to check if the action is valid
      if new_state is not None:
        new_state_tuple = tuple(map(tuple, new_state))

        # Condition to check if the new node is not already explored
        if new_state_tuple not in visited:

          # indexing
          index = index + 1

          # appending this new node to "states" and "track" along with the action and index
          states.append((new_state, history + [move_name], index , current_index))
          track.append((new_state, history + [move_name], index , current_index))

          # adding the configuration to visited
          visited.add(new_state_tuple)

          # Condition statement to check if this new node is the solution
          if np.array_equal(new_state, desired):
              print("Solution Reached")
              print("Path:", history + [move_name])
              print("Current Index:", index)
              print("Parent Index:", current_index)
              searching = False
              break

# Code to write the node configuration information to Nodes.txt
with open("Nodes.txt", "w") as file:
  for i in track:
    node_list=[]
    node=i[0]
    for j in range(3):
      for k in range(3):
        node_list.append(node[k,j])
    node_string = ''.join(str(num) for num in node_list)
    file.write(node_string)
    file.write("\n")

# Code to write the node configuration and index information to NodesInfo.txt
with open("NodesInfo.txt", "w") as file:
  file.write(f"{'Node Index'} {'Parent Index'} {'Node'}\n")
  for i in track:
    node_list=[]
    node=i[0]
    for j in range(3):
      for k in range(3):
        node_list.append(node[k,j])
    node_string = ''.join(str(num) for num in node_list)
    file.write(f"{i[2]} {i[3]} {node_string}\n")

# Code to write the solution to the puzzle as solved by the code above, to nodePath.txt
solution = track[-1]
parent = solution[3]
solution_path=[solution[0]]
while True:
  if parent==0:
    break
  for i in track:
    if i[2]==parent:
      solution_path.append(i[0])
      parent=i[3]

solution_path=solution_path[::-1]

with open("nodePath.txt", "w") as file:
  for i in solution_path:
    node_list=[]
    for j in range(3):
      for k in range(3):
        node_list.append(i[k,j])
    # node_string = str(node_list)
    node_string = ''.join(str(num) for num in node_list)
    file.write(node_string)
    file.write("\n")
