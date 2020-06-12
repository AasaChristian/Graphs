from room import Room
from player import Player
from world import World
from util import Stack, Queue  
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# map_file = "test_line.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

graph = {}

direct ={
    'n': '?', 's': '?','w': '?', 'e': '?'
}




q = Queue()
# print(player.current_room, "current room")
q.enqueue([player.current_room.id])
graph[player.current_room.id] = direct
visited = set()
path_len = 1

while len(visited) < 2:
    # print(graph[player.current_room.id]['n'])
    for exits in player.current_room.get_exits():
        cur_room = player.current_room.id

        if exits == 'n':
            player.travel(exits)
            graph[cur_room]['n'] = player.current_room.id
        if exits == 's':
            player.travel(exits)
            graph[cur_room]['s'] = player.current_room.id
        if exits == 'w':
            player.travel(exits)
            graph[cur_room]['w'] = player.current_room.id
        if exits == 'e':
            player.travel(exits)
            graph[cur_room]['e'] = player.current_room.id
        







    path = q.dequeue()
    cur_node = path[-1]

    if cur_node not in visited:
        visited.add(cur_node)

    # for next_room in player.current_room.get_exits():

        
    #     path_copy = list(path)
    #     path_copy.append(next_room)
    #     traversal_path.append(next_room)
    #     q.enqueue(path_copy)
        # print(path[0], "path")
        # print(traversal_path, "traversal path")






# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
# print(player.current_room, "cur room")

for move in traversal_path:
    # print(move, "player.travel(move)")
    # print(player.current_room, "player.current_room")
    player.travel(move)
    visited_rooms.add(player.current_room)
    # print(visited_rooms, ":visited rooms", len(room_graph), ":amount of rooms", traversal_path, ":traversalPath")
# print(len(visited_rooms), "len visited rooms", len(room_graph), "amount of rooms", len(traversal_path), " len traversalPath")
if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
