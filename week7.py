import sys

sys.exit() #프로그램 종료


#function

def functionName(inputvalue):
    inputvalue=-inputvalue*2 #파라미터

functionName(2) #인수

def default_test(a, b=0):
    c=a+b
    return c

def return2(a,b):
    return a,b

x,y=return2(2,3)

def function2():
    global a
    a=10

a=20

#키워드 인수 (<->위치 인수)
def calc(a,b):
    return a+b

c=calc(b=20,a=40)
#둘이 섞어쓰려면 차라리 위치 인수를 먼저 써야됨