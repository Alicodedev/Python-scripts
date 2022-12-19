play = True
z = "x"
while play:

	game = [[0, 0, 0],
		    [0, 0, 0],
		    [0, 0, 0]]
	game[y][x] = z
    print(game)
    y = int(input("enter a number"))
    x = int(input("enter a number"))
