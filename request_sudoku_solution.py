import requests

# URL of the API endpoint
url = "http://127.0.0.1:5000/solve"

# Payload containing the Sudoku puzzle grid
payload = {
    "grid": [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
}

# Headers indicating the content type
headers = {'Content-Type': 'application/json'}

# Making the POST request to the API
response = requests.post(url, json=payload, headers=headers)

# Checking the response status and printing the solution or error
if response.status_code == 200:
    print("Solved Sudoku Grid:")
    solved_grid = response.json().get('solution')
    for row in solved_grid:
        print(row)
else:
    print("Error:", response.json())
