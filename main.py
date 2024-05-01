import numpy as np
angle = 0

def locationa(locations):
    flag = 0
    temp = []
    try:
        for i in range(len(locations)):
            a=(locations[i][0]+1,locations[i][1])
            # print(a)
            if locations[i][1]==locations[i+1][1] - 1 and flag ==0:
                temp.append(locations[i])
                flag = 1
            elif locations[i][1]!=locations[i+1][1] - 1 or locations[i][0]!=locations[i+1][0]:
                flag = 0
    except:
        pass
    return temp


def chodas(sub):
    global angle
    # print(sub)
    suma1 = sum(sum(sub))+1
    hori = (suma1,0)
    vert = (suma1,0)

    for i in range(len(sub)):

        if sum(sum(sub[i:i+1])) == 0:
            if i == 0:
                a = sum(sum(sub[i:]))

            elif i == len(sub)-1:
                a = sum(sum(sub[:i]))
            else:
                a = abs(sum(sum(sub[:i])) - sum(sum(sub[i:])))
            # a = 10
            if a < hori[0]:

                hori = (a,i)
            else:
                break
    for i in range(len(sub[1])):
        if sum(sum(sub[:,i:i+1])) == 0:
            if i == 0:
                a = sum(sum(sub[:,i:]))
            elif i == len(sub[1])-1:
                a = sum(sum(sub[:,:i]))
            else:
                a = abs(sum(sum(sub[:,:i])) - sum(sum(sub[:,i:])))
            if a < vert[0]:
                vert = (a,i)
            else:
                break
    # print(min(hori,vert))
    if hori[0] < vert[0]:
        angle = hori[1]
    else:
        angle = vert[1]
    return min(hori[0],vert[0])


Nlists = (input().split())
inputLists = []
for k in range(int(Nlists[0])):
    lala = input()
    oneList = list(map(int,list(lala)))
    # print(oneList)
    inputLists.append(oneList)
working = np.array(inputLists)
transpose = working.transpose()
corners = []
mask = (working==1)
ans = np.where(mask)
ans2 = np.where(transpose==1)
locations = list(zip(ans[0], ans[1]))
locations2 = list(zip(ans2[0], ans2[1]))
print(locations)
print(locations2)
print((3,6) in locations)
rows = ans[0]
colums = ans[1]
temp1 = locationa(locations)
temp2 = locationa(locations2)

temp1.sort(key= lambda x:(x[1],x[0]))
temp2.sort(key= lambda x:x[1])
print(temp1)
print(temp2)
dimens = []
search = [i[1] for i in temp2]
def cleaner(thing):
    flag = 0
    temp1 = thing
    try:
        while True:
            for i in range(len(temp1)):
                if i == len(temp1)-1:
                    if temp1[i][1]!=temp1[i-1][1]:
                        del temp1[i]
                        break
                if i == 0:
                    if temp1[0][1]!=temp1[1][1]:
                        del temp1[0]
                        break
                if temp1[i][1] != temp1[i+1][1] and flag==0:
                    print('middle')
                    del temp1[i]
                    break
                else:
                    flag = 1
    except:
        pass
    return temp1
tata1 = temp1
tata2 = temp2
temp1 = cleaner(tata1)
temp2 = cleaner(tata2)
print(temp1)
print(temp2)
print(len(temp1))
for i in range(0,len(temp1),2):

    t = search.index(temp1[i][0])
    dimens.append((temp1[i][0],abs(temp2[t+1][0]-0),temp1[i+1][0],temp1[i][1]))
final  = 0
# print(dimens)
for i in dimens:

    sub = working[i[0]+1:i[2],i[3]+1:i[1]]
    print(sub)

    # print(angle)
    final += chodas(sub)
print(final)






# 7 7
# 1111111
# 1203041
# 1000001
# 1706051
# 1000001
# 1908021
# 1111111
'''
16 28
0000000000000000000000000000
0300000000000000000000600000
0011111111000000000000000000
0013000031000111111111111111
0010030201000130002000300201
0010000001540100030003000001
0012500001030100000000000001
0010000041000102003030000001
0010000001000111111111111111
0013000001000000000000000000
0010200001001111100000000000
0010050001001205100000111100
0011111111001000100005130100
0000000000001403180000102100
0002000000001111180000100100
0000000000000000000000111100



[[0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 3 0 0 0 0 0 0 0 0 0 0 0 0 0 0]
 [0 0 1 1 1 1 1 1 1 1 1 1 1 0 0 0]
 [0 0 1 3 0 0 2 0 0 3 0 0 1 0 2 0]
 [0 0 1 0 0 0 5 0 0 0 2 0 1 0 0 0]
 [0 0 1 0 3 0 0 0 0 0 0 5 1 0 0 0]
 [0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0]
 [0 0 1 0 2 0 0 0 0 0 0 0 1 0 0 0]
 [0 0 1 3 0 0 0 4 0 0 0 0 1 0 0 0]
 [0 0 1 1 1 1 1 1 1 1 1 1 1 0 0 0]
 [0 0 0 0 0 5 0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 4 3 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 0]
 [0 0 0 1 1 1 1 1 1 0 1 2 0 4 1 0]
 [0 0 0 1 3 0 0 0 1 0 1 0 0 0 1 0]
 [0 0 0 1 0 0 0 2 1 0 1 5 0 3 1 0]
 [0 0 0 1 0 0 0 0 1 0 1 1 1 1 1 0]
 [0 0 0 1 0 3 0 0 1 0 0 0 0 8 8 0]
 [0 0 0 1 2 0 0 3 1 0 0 0 0 0 0 0]
 [0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0]
 [0 0 0 1 0 0 0 3 1 0 0 0 0 0 0 0]
 [0 0 0 1 0 3 0 0 1 0 0 0 5 0 0 0]
 [0 6 0 1 3 0 0 0 1 0 0 1 1 1 1 1]
 [0 0 0 1 0 0 0 0 1 0 0 1 3 0 0 1]
 [0 0 0 1 0 0 0 0 1 0 0 1 0 2 0 1]
 [0 0 0 1 2 0 0 0 1 0 0 1 1 1 1 1]
 [0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0]
 [0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0]]
 
 
 
'''