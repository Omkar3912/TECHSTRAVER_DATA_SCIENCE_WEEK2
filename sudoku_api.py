from flask import Flask, request, jsonify
import copy

app = Flask(__name__)

def find_empty(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid(grid, num, pos):
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if is_valid(grid, i, (row, col)):
            grid[row][col] = i
            if solve(grid):
                return True
            grid[row][col] = 0
    return False

@app.route('/solve', methods=['POST'])
def solve_sudoku():
    data = request.json
    grid = data.get('grid')

    if not grid or not isinstance(grid, list) or len(grid) != 9 or any(len(row) != 9 for row in grid):
        return jsonify({"error": "Invalid input"}), 400

    solution = copy.deepcopy(grid)
    if solve(solution):
        return jsonify({"solution": solution})
    else:
        return jsonify({"error": "No solution found"}), 400

if __name__ == '__main__':
    app.run(debug=True)
