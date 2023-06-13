list=['a','b','c']

c=input("")
if c in list:
    print("있음")

idx=list.index(c)

########

import turtle
t=turtle.Turtle()

t.penup()
t.goto(x,y)
t.pendown()
t.begin_fill()
t.color("green")
square(50)  #입력인수를 길이로 갖는 정사각형을 그리는 함수
t.end_fill()

s=turtle.Screen()
s.onscreenclick(drawit) #위의 사각형을 그리고 색을 채우는 함수
                        #drawit은 x,y를 인자로 받음

##########

chart=[]
chart.append('apple')
chart.append('pear')    #list 내용 추가

print(chart[1])

chart[a:b]  #a부터 b-1인덱스까지
chart[a:]   #a부터 끝까지
chart[:a]   #0부터 a-1인덱스까지
chart[:]    #전체

chart.insert(1,'orange')    #1번 인덱스자리에 값을 넣고 뒤에꺼는 밀어냄
chart.remove('apple')       #apple 삭제

del chart[1]                #1번 인덱스 값 삭제

a=chart.pop()   #stack

b=chart.index('orange')     #오렌지 인덱스 반환

chart.sort()                #기본 오름차순
chart.sort(reverse=True)    #내림차순

sort_chart=sorted(chart)

#2차원 배열은
#[[],[]]이따구로 생성함
#list[1][2]이런식으로 호출함

import random
c=random.choice(chart)  #list 내용중에 랜덤으로 뽑음
