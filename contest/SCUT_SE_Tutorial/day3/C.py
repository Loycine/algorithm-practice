n = m = X = 0
a = [[]]
c = []

global_cost = int(1e10)

def isValid(w):
    for j in range(m):
        if(w[j] < X):
            return False
    return True

def dfs(depth, isBuy, cost, w):
    global global_cost
    if(depth >= n):
        return
    if(isBuy):
        cost += c[depth]
        for j in range(m):
            w[j] += a[depth][j]
    
    if isValid(w):
        global_cost = min(global_cost, cost)
    
    dfs(depth + 1, True, cost, w[:])
    dfs(depth + 1, False, cost, w[:])


if __name__ == "__main__":
    n,m,X = map(int, input().split())

    a = [[] for i in range(n)]
    c = []

    for i in range(n):
        digits = list(map(int, input().split()))
        c.append(digits[0])
        for j in range(m):
            a[i].append(digits[j+1])

    w = [0 for i in range(m)]
    dfs(-1, 0, 0, w)

    if(global_cost > 1e9):
        print(-1)
    else:
        print(global_cost)
            