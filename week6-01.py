import turtle
t=turtle.Turtle()
t.shape('turtle')

t.penup()
t.goto(100,100)
t.write('양수')
t.goto(100,0)
t.write('0')
t.goto(100,-100)
t.write('음수')

t.goto(0,0)
t.pendown()

s=turtle.textinput('','숫자를 입력 : ')
n=int(s)

if n>0:
    t.goto(100,100)
elif n==0:
    t.goto(100,0)
else:
    t.goto(100,-100)