from replit import db

class Cell:
	def __init__(self, x, y, map):
			self.x = x
			self.y = y
			self.point = db[map][30 - x][y - 1]

	def __setitem__(self, key, value):
		self.point[key] = value 

	def __getitem__(self, key):
		return self.point[key] if key in self.point else None


# point = Cell(30, 1, "MAP")
# point["team"] = "Орлы"

# point2 = Cell(30, 1, "MAP")
# print(point2["team"])
# db["MAP"] = [[{} for j in range(30)]for i in range(30)]






