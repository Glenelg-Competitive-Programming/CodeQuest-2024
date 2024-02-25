import sys
sys.stdin = open("test.in", "r")
paths = set()
def get_neighbors(cur_node, cur_path, n, maze):

    sx = [0, 1, -1, 0]
    sy = [1, 0, 0, -1]
    res = []
    for px,py in zip(sx, sy):
        x = cur_node[0] + px
        y = cur_node[1] + py

        if (x>=n or x<0 or y>=n or y<0 or (x,y) in cur_path or maze[x][y] == "0"):
            continue
        res.append((x,y))
    return res



def dfs(cur_path, cur_node, maze, n ):
    from copy import copy
    neighbors = get_neighbors(cur_node, cur_path, n, maze)
    for node in neighbors:
        if maze[node[0]][node[1]] == "&":
            paths.add(",".join([str(i) for i in cur_path]))
            continue
        
        cur_path.append(node)
        dfs(cur_path, node, maze, n)
        cur_path.remove(node)

def solve_test_case():
    n = int(input())
    maze = []
    for _ in range(n):
        maze.append(list(input()))
    
    maze[0][0] = "*"
    maze[n-1][n-1] = "&"

    path = [(0,0)]
    cur_node = (0,0)
    dfs(path, cur_node, maze, n)

    print(paths)
    print(len(paths))




for _ in range (int(input())):
    solve_test_case()