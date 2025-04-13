def detect_cycle(dependencies):
    from collections import defaultdict

    graph = defaultdict(list)
    for a, b in dependencies:
        graph[a].append(b)
    
    visited = set()
    stack = set()
    cycle = []

    def dfs(node):
        if node in stack:
            cycle.append(node)
            return True
        if node in visited:
            return False

        visited.add(node)
        stack.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                cycle.append(node)
                return True
        stack.remove(node)
        return False

    for node in graph:
        if dfs(node):
            break

    return cycle[::-1] if cycle else []


deps = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('D', 'E')]
print(detect_cycle(deps))
