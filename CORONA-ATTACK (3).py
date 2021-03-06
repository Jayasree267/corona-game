import turtle
import time
import random

def check():
	global lifes , score , level , difficult , enemySpeed

	for i in range(len(enemies)):
		if(plane.distance(enemies[i]) < 50 ):
			enemies[i].goto(1000,1000)
			lifes -= 1

	if(lifes <= 0):

		pen.goto(0, 0)
		pen.write("STAY HOME WITH ME ", align="center", font=("Courier", 24, "normal"))
		
		for i in range(len(enemies)):
			enemies[i].goto(2000,2000)
		for i in range(len(bullets)):
			bullets[i].goto(2000,2000)

		enemies.clear()
		bullets.clear()
		time.sleep(3)
		pen.clear()
		lifes = 3
		score = 0
		level = 0
		difficult = 3
		levelUpgrade = 10
		enemySpeed = 5
		pen.goto(0, 320)
		createEnemies()
		createEnemies()

planeSpeed = 30


score = 0
lifes = 3
level = 0
levelUpgrade = 10
difficult = 3
picEnimes = ["first1.gif","fourth1.gif","fourth1.gif","fourth1.gif"]

#SCREEN

wn = turtle.Screen()
wn.setup(width = 700, height = 700)
wn.title("CORONA ATTACK")
wn.bgpic("maskk.gif")
wn.tracer(0)
wn.register_shape("dettol2.gif")
wn.register_shape(picEnimes[0])
wn.register_shape(picEnimes[1])
wn.register_shape(picEnimes[2])
wn.register_shape(picEnimes[3])
wn.register_shape("shoot.gif")

# plane 

plane = turtle.Turtle()
plane.shape("dettol2.gif")
plane.color("white")
plane.penup()
plane.goto(0,-320)
plane.speed(0)
plane.direction = "stop"

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 320)

# Enemy

enemies = []
def createEnemies():
	global selectEnemies
	enemy = turtle.Turtle()
	selectEnemies = random.randint(0,3)
	enemy.shape(picEnimes[selectEnemies])
	enemy.color("red")
	enemy.penup()
	enemy.goto(random.randint(-320,320),random.randint(150,320))
	enemy.speed(0)
	enemies.append(enemy)

enemySpeed = 5

# move enemies 

def moveEnemies():
	global enemySpeed
	for i in range(len(enemies)):
		enemies[i].sety(enemies[i].ycor() - enemySpeed)

#bullets
bulletSpeed = 20
bullets = []

def fire():
	bullet = turtle.Turtle()
	bullet.shape('shoot.gif')
	bullet.color("yellow")
	bullet.penup()
	bullet.shapesize(.5,.5)
	bullet.goto(plane.xcor() , plane.ycor()+bulletSpeed)
	bullets.append(bullet)

# move bullet to kill the target

def moveBullets():
	global bulletSpeed , level , levelUpgrade

	for b in range(len(bullets)):
		bullets[b].sety(bullets[b].ycor()+bulletSpeed)

		for e in range(len(enemies)):
			if(bullets[b].distance(enemies[e]) < 30):

				global score
				score += 1
				enemies[e].goto(3000,3000)
				bullets[b].goto(2000,2000)

				if(score % levelUpgrade == 0):
					level += 1

# check


def up():
	if(plane.ycor() < 320):
		plane.sety(plane.ycor()+planeSpeed)

def down():
	if(plane.ycor() > -320):
		plane.sety(plane.ycor()-planeSpeed)

def right():
	if(plane.xcor() < 320):
		plane.setx(plane.xcor()+planeSpeed)

def left():
	if(plane.xcor() > -320):
		plane.setx(plane.xcor()-planeSpeed)

wn.listen()
wn.onkeypress(up,'w')
wn.onkeypress(down,'s')
wn.onkeypress(right,'d')
wn.onkeypress(left,'a')
wn.onkeypress(fire,'space')

createEnemies()
createEnemies()
createEnemies()
createEnemies()
mytime = 0

while True:
	wn.update()
	check()
	moveEnemies()
	moveBullets()
	pen.clear()
	mytime += 1
	pen.write("score: {}      level: {}       lifes: {} ".format(score,level,lifes), align="center", font=("Helvetica", 16, "bold"))
	
	if(mytime > 100/difficult):
		for i in range(difficult):
			createEnemies()
		mytime = 0

	if (score > 0):
		if (score % levelUpgrade == 0 or score > levelUpgrade):
			levelUpgrade += 5
			enemySpeed += 0.5
			print("level =", level)
			print('enemySpeed =',enemySpeed)
			if (level % 5 == 0):
				difficult += 1
				print("difficult =",difficult)
				

	time.sleep(.1)

turtle.done()
