price=10000
print("%d\n"%price)
print("%s\n"%price)

#string index
#0~n-1
#동일하게 -n~-1로도 사용가능

#string[4]이런 식으로 추출해서 사용가능

#string[a:b]
#a~b-1

#string[a:b:c]
#a~b-1, c간격
#or a~b+1 c간격(음수로 내려갈때)

#string[0::1] : all
#string[-1:-1] : 거꾸로 전체
#string[:] : 그냥 전체

#특수 문자열 \n \t \\ \" \'

#stringlength : len(string)

import turtle
t=turtle.Turtle()
t.shape("turtle")

s=turtle.textinput("","이름입력하셈")
t.write("hi"+s)

#조건문
#if {조건}:
#elif {조건}:
#else:

#논리연산자
#x and y
#x or y
#not x

import random
a=random.randrange(2) #0~1
b=random.randint(1,24) #1~24 정수
c=random.choice[True,False] 