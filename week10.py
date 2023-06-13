hmm=[[x,y,color],[x1,y1,c1],[x2,y2,c2]]

for x,y,c in hmm:
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(c,c)
    t.begin_fill()
    t.circle(3)
    t.end_fill()

#########

#dictionary

dic={}
dic["idx1"]="dic1idxData"
dic["dix2"]="dic2idxData"

print(dic["idx1"])  #--> dic1idxData

print(dic.keys())
#--> dic.keys(["idx1","idx2"])
#     dic.values()

dic.clear() #전체 삭제

dic2={"key1":1,"key2":2}

for k,v in dic2.items():
    print('{},{}'.format(k,v))

#집합

s=set() #집합 선언
s={1,2,5}
s.add(10)   #->1 2 5 10

s.discard(5)    #값 삭제
s.remove(2)     #값 삭제
s.clear()       #전체 삭제