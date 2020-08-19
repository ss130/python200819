scores=[]
maxscores=0
minscores=100
maxname = 0
minsame=0
total=0
for i in range(5):
    n=int(input("成績:"))
    name = input("name:")
    scores.append(n)
    if n>maxscores:
        maxscores=n
        maxsname=name
    if n<minscores:
        minscores=n
        minsname=name
    total=total+n
s=total/len(scores)
print('總分',total)
print('平均',s)
print('最高分',maxscores)
print('最低分',minscores)
print('最高分人',maxsname)
print('最低分人',minsname)

