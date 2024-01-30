from collections import defaultdict

def number_of_paths_with_odd_weight(graph, s, t):
    def dfs(v, parity):
        print('Stack frame created')
        print(f'Node: {v}')
        # it gets here from one of the paths
        if v == t:
            return 1 if parity == 1 else 0

        if (v, parity) in memo:
            return memo[(v, parity)]

        total_paths = 0
        for u, weight in graph.get(v, []):
            print(f'parity + weight: {parity} + {weight} = {parity + weight}')
            total_paths += dfs(u, (parity + weight) % 2)

        memo[(v, parity)] = total_paths
        return total_paths

    memo = {}
    # return dfs(s, 0) + dfs(s, 1)
    return dfs(s, 0)

# Example graph with at least 3 odd-weight paths
graph_example_updated = {
    's': [('a', 2), ('b', 3)],
    'a': [('c', 4)],
    'b': [('c', 1)],
    'c': [('t', 5), ('d', 2)],
    'd': [('t', 1)],
    't': []
}

result_updated = number_of_paths_with_odd_weight(graph_example_updated, 's', 't')
print(f"Number of paths from 's' to 't' with odd weight: {result_updated}")
