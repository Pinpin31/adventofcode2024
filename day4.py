grid = []
word = "XMAS"
word_length = len(word)

def isValid(x, y):
    return 0 <= x < rows and 0 <= y < cols

def search_from(x, y):
    count = 0
    for dx, dy in directions:
        end_x = x + dx * (word_length - 1)
        end_y = y + dy * (word_length - 1)
        if isValid(end_x, end_y):
            match = True
            for i in range(word_length):
                if grid[x + i * dx][y + i * dy] != word[i]:
                    match = False
                    break
            if match:
                count += 1
    return count

with open('day4.input', 'r') as f:
    for line in f.readlines():
        grid.append(list(line.replace("\n", "")))
rows = len(grid)
cols = len(grid[0])

directions =  [ 
        (0, 1),    # Droite
        (0, -1),   # Gauche
        (1, 0),    # Bas
        (-1, 0),   # Haut
        (1, 1),    # Diagonale bas-droite
        (1, -1),   # Diagonale bas-gauche
        (-1, 1),   # Diagonale haut-droite
        (-1, -1)   # Diagonale haut-gauche
    ]

total_count = 0
for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'X':
            total_count += search_from(i, j)

print(total_count)
