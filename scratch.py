map_of_board = ["XXXXXXXXXX XXXXXXXXXX",
                "XXXXXXXXXX XXXXXXXXXX",
                "XXXXXXXXXX XXXXXXXXXX",
                "XXXXXXXXXX XXXXXXXXXX",
                "XXXXXXXXXX XXXXXXXXXX",
                "XXXXXXXXXX XXXXXXXXXX",
                "XXXXXXXXXX XXXXXXXXXX",
                "XXXXXXXXXX XXXXXXXXXX",
                "XXXXXXXXXXXXXXXXXXXXX"]
    

line = "XXXXXXXXXX XXXXXXXXXX"


list_tuple = []
for x, y in enumerate(line):
    list_tuple.append((x, y))

# print(list_tuple)

for i in map_of_board:
    print(i)
    print(len(map_of_board))