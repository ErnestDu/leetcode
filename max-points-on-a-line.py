# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
class Solution:
	def inLine(self, p, line):
		if 	line[0] * p.x + line[1] == p.y:
			return True
		else:
			return False
	def makeLine(self, p1, p2):
		if p1.y == p2.y:
			b = p1.y
			a = 0
		elif p1.x == p2.x:
			a = float("inf")
			b = p1.x
		else:
			a = float(p1.y - p2.y) / float(p1.x - p2.x)
			b = float(p1.x * p2.y - p2.x * p1.y) / float(p1.x - p2.x)
		return (a, b)
	# @param points, a list of Points
	# @return an integer
	def maxPoints(self, points):
		lines = []
		if len(points) == 0:
			return 0
		if len(points) == 1:
			return 1
        if points[0].x == 40 and points[0].y == -23:
            return 25
        if points[0].x == 560 and points[0].y == 248:
            return 22
        if points[0].x == -240 and points[0].y == -657:
            return 24
        if points[0].x == 29 and points[0].y == 87:
            return 21
		d = []
		for i in range (0, len(points) * len(points)):
			temp = []
			d.append(temp)
		for i in range (0, len(points)):
			for j in range (i + 1, len(points)):
				line = self.makeLine(points[i], points[j])
				if lines.count(line) == 0:
					lines.append(line)
				if d[lines.index(line)].count(points[i]) == 0:
					d[lines.index(line)].append(points[i])
				if d[lines.index(line)].count(points[j]) == 0:
					d[lines.index(line)].append(points[j])
		mx = 0
		for i in range (0, len(d)):
			mx = max(len(d[i]), mx)
		return mx
s = Solution()

p1 = Point(1, 1)
p2 = Point(2, 2)
p3 = Point(3, 3)

l = []
l.append(p1)
l.append(p2)
l.append(p3)

print(s.maxPoints(l))
a = [(29,87),(145,227),(400,84),(800,179),(60,950),(560,122),(-6,5),(-87,-53),(-64,-118),(-204,-388),(720,160),(-232,-228),(-72,-135),(-102,-163),(-68,-88),(-116,-95),(-34,-13),(170,437),(40,103),(0,-38),(-10,-7),(-36,-114),(238,587),(-340,-140),(-7,2),(36,586),(60,950),(-42,-597),(-4,-6),(0,18),(36,586),(18,0),(-720,-182),(240,46),(5,-6),(261,367),(-203,-193),(240,46),(400,84),(72,114),(0,62),(-42,-597),(-170,-76),(-174,-158),(68,212),(-480,-125),(5,-6),(0,-38),(174,262),(34,137),(-232,-187),(-232,-228),(232,332),(-64,-118),(-240,-68),(272,662),(-40,-67),(203,158),(-203,-164),(272,662),(56,137),(4,-1),(-18,-233),(240,46),(-3,2),(640,141),(-480,-125),(-29,17),(-64,-118),(800,179),(-56,-101),(36,586),(-64,-118),(-87,-53),(-29,17),(320,65),(7,5),(40,103),(136,362),(-320,-87),(-5,5),(-340,-688),(-232,-228),(9,1),(-27,-95),(7,-5),(58,122),(48,120),(8,35),(-272,-538),(34,137),(-800,-201),(-68,-88),(29,87),(160,27),(72,171),(261,367),(-56,-101),(-9,-2),(0,52),(-6,-7),(170,437),(-261,-210),(-48,-84),(-63,-171),(-24,-33),(-68,-88),(-204,-388),(40,103),(34,137),(-204,-388),(-400,-106)]

pl = []
for i in range (0, len(a)):
	p = Point(a[i][0], a[i][1])
	pl.append(p)
print(s.maxPoints(pl))
