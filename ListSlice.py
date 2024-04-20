l=[1,2,1.1,2.2,"tops",True,"python",10,20,1,2,"java",False,100,200,400,60]

print(len(l))
print(l[1:3:4])
print(l[15::5])
print(l[:1:5])
print(l[::10])
print(l[10:15])

print(l[-17:-15:3])
print(l[-7::7])
print(l[:-16:12])
print(l[::-5])
print(l[-14:-12])

for i in l:
    print(i)
print(101 in l)
