
'''
My idea was divide in two steps:
1. Find all neighbors of every n (number of nodes)
2. Do a DFS on every node and keep track of visited nodes
3. Count the number of structs as each time the DFS stack array gets empty
'''

def findNbs(node, edges):
    nbs = set()
    for idx in range(0, len(edges), 2):
        u = edges[idx]
        v = edges[idx+1]
        if u == node: nbs.add(v)
        if v == node: nbs.add(u)
    return sorted(nbs)


def countComponents(n, edges):
    nbs_arr = []
    for node in range(n):
        nbs_arr += [findNbs(node, edges)]
    
    stack = []
    visited = set()
    num_structs = 0
    for count in range(n):
        if len(stack) == 0:
            stack.append(count)
            num_structs += 1
        check_node = stack.pop()
        check_node_nbs = nbs_arr[check_node]
        visited.add(check_node)
        for nb in check_node_nbs:
            if nb not in visited:
                stack.append(nb)  
    return num_structs
