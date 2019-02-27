def fav_colors(**kwargs):
	for person, color in kwargs.items(): #gives us keys and values
		print(f"{person}'s favorite color is {color}")

fav_colors(Johnny="purple", Ruby="red", Ethel="teal")
fav_colors(Johnny="purple", Ruby="red", Ethel="teal", ted="blue")
fav_colors(Johnny="royal deep amazing purple")

#better suited when we're passing dictionaries. 