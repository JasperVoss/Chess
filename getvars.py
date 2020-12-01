def get_board_vars():
	file = open("board_vars.txt", 'r')
	text = file.read()
	file.close()
	var = []
	curr_string = ""
	for v in text:
		if v == "\n":
			var.append(curr_string)
			curr_string = ""
		else:
			curr_string = curr_string + v
	for i in range(len(var)):
		var[i] = float(var[i])

	return var


print(get_board_vars())