# Breadth-First-Search-8-Puzzle-Problem

## Project Description
This repository contains the code for solving the 8-puzzle problem using the Breadth-First Search (BFS) algorithm. The project was developed as part of ENPM661 Project 1.

## Running the Main Code

Before running the main code, please follow these steps:

1. **Modify the Puzzle Configurations**:
   - Open the `proj1_suhas_nagaraj.py` file.
   - Update the starting configuration and the desired end configuration of the puzzle in the code.

2. **Run the Python File**:
   - Execute the file by running the following command in your terminal:
     ```bash
     python3 proj1_suhas_nagaraj.py
     ```

3. **Expected Outputs**:
   - If a solution exists, the code will output the following:
     1. The path to the solution.
     2. The index of the solution node.
     3. The index of the solution node's parent.
     4. Three text files with the following details:

### Text File 1: Nodes.txt
- Contains all the explored states as a list.

### Text File 2: NodesInfo.txt
- Provides information about all nodes explored:
  - **First Column**: Node Index
  - **Second Column**: Parent Node Index
  - **Third Column**: Node Configuration

### Text File 3: nodePath.txt
- Contains the solution to the puzzle as solved by the code. The elements are stored column-wise.
- The states are listed from the start node to the goal node.

## Viewing the Solution Animation

After the text files are generated, you can visualize the solution steps using an animation. To do this, run the `animate.py` file:

```bash
python3 animate.py
```



