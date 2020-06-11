from util import Stack, Queue  # These may come in handy

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def get_ancestor(ancestors, child):
    hiers = []
    for hier in ancestors:
        if hier[1] == child:
            hiers.append(hier[0])
    return hiers
def earliest_ancestor(ancestors, starting_node):
    q = Queue()
    q.enqueue([starting_node])
    visited = set()
    path_len = 1
    oldest_parent = -1
    while q.size() > 0:
        path = q.dequeue()
        cur_node = path[-1]

        if cur_node not in visited:
            visited.add(cur_node)

        if len(path) >= path_len and cur_node < oldest_parent or len(path) > path_len:
            path_len = len(path)
            oldest_parent = cur_node

        for father in get_ancestor(ancestors, cur_node):
            path_copy = list(path)
            path_copy.append(father)
            q.enqueue(path_copy)

    return oldest_parent

# print(earliest_ancestor(test_ancestors, 1))
# print(earliest_ancestor(test_ancestors, 2))
# print(earliest_ancestor(test_ancestors, 3))
# print(earliest_ancestor(test_ancestors, 4))
# print(earliest_ancestor(test_ancestors, 5))
# print(earliest_ancestor(test_ancestors, 6))
# print(earliest_ancestor(test_ancestors, 7))
# print(earliest_ancestor(test_ancestors, 8))
# print(earliest_ancestor(test_ancestors, 9))





