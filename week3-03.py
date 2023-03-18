import turtle
t=turtle.Turtle()
t.shape("turtle")

t.shape('square')

t.width(10)
t.color('blue')

for i in range(6):
    #t.speed(0)
    t.forward(100)
    t.left(60)

t.up() #그리기 멈춤, 펜을 들었음
t.goto(0,-200) # 해당 좌표로 이동
t.down() # 펜을 떨구고 다시 그릴 수 있는 상태
t.goto(100,-200)
t.up()