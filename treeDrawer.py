import turtle as tt
import random

tt.bgcolor("black")
#turn off animations
tt.tracer(0,0)
tt.pencolor("black")
tt.setpos(0,-400)
#draw trunk
trunkLen = 500
trunkWidth = 50
tt.pencolor("brown")
tt.left(90)
tt.pensize(trunkWidth)
tt.forward(trunkLen)
tt.backward(5)

tt.speed(9)
tt.update()

def drawFlower(size):
	if random.randint(0,3)==0:
		tt.pencolor("yellow")
	else:
		tt.pencolor("pink")
	tt.pensize(3)
	tt.forward(size)
	tt.backward(size*2)
	tt.forward(size)
	tt.left(90)
	tt.forward(size)
	tt.backward(size*2)
	tt.forward(size)
	tt.right(90)
	return 0

def drawBranch(level,direction):
	#CONSTANT THAT AFFECT TREE SHAPE
	angle = 30
	maxThickness = 40
	flowerFreq = 30
	#^^lower is more : 0 is none
	maxDepth = 29
	#^controls foliage levels | 22 is good | 25 is great but slow | above does not increase quality
	maxLength = 80


	if level >= maxDepth:
		return 0

	#controls leaf level
	if level >maxDepth-7:
		color = "green"
	else:
		color = "brown"

	if int(maxDepth/3)==level:
		tt.update()

	if not flowerFreq==0:
		if level == maxDepth-1 and random.randint(0,flowerFreq-1)==0:
			drawFlower(4)
			return 0

	randomLen = random.uniform(0.5,1.2)
	
	randomAng = random.uniform(0.5,1.2)
	

	angle *=randomAng
	tt.pencolor(color)
	tt.left(angle+(360-angle*2)*direction)
	tt.pensize(max([maxThickness-level*2,1]))
	tt.forward((maxLength-maxLength*(level/maxDepth))*randomLen)

	randomJump = random.randint(0,1)
	drawBranch(level+1+randomJump,0)

	randomJump = random.randint(0,1)
	drawBranch(level+1+randomJump,1)

	tt.pencolor(color)
	tt.left(180)
	tt.pensize(max([maxThickness-level*2,1]))
	tt.forward((maxLength-maxLength*(level/maxDepth))*randomLen)
	tt.left((180-angle)+angle*2*direction)

drawBranch(1,0)
tt.update()
print("50%")
drawBranch(1,1)
tt.ht()
tt.update()
print("done")
tt.done()
