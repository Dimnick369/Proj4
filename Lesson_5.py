# region list, index, read list
# print([],len([]),type([]))


# b=[1,2,3,'fsg',3,4,7]
# print(b[3],b[-2])

# i=[int(i) for i in input().split()]
# endregion
#####################################################
# region print(sep,end,split)
# a=[]
# a.append([2,4])
# a.append('123')
# a.append(6)
# a+=[3]
# print(a)
# print(a[1])

# c=input()
# b=c.split()
# print(b,1,2,3,sep=' #D# ')
# print(*b,sep=' #D# ')
# print(a,b,c,sep=' #D# ')

# endregion
#####################################################
# region list create
# n=12
# a=[0]*n
# a=[0 for i in range(n)]
# a=[int(i) for i in input().split()] # generator
# print(a)
# endregion
#####################################################
# region list gen + if
# a=[i for i in range(20) if i%2]
# print(a)
# #
# a=[i if i%2 else i**2 for i in range(20) ]
# print(a)
# endregion
#####################################################
# region list=list
# a=[1,2,3]
# b=a
# print(a,b)
# a.append(456)
# print(a,b)
# endregion
#####################################################
# region list==list
# a=[1,2]
# b=[1,2]
# print(a==b,id(a),id(b),sep='\n')
#
# a=[1,2,3,4,5,6,7,8]
# b=[1,2,3,4,5,6,7,8]
# print(a==b,id(a),id(b),sep='\n')
# endregion
#####################################################
# region list +,*,append,insert,remove,del, in. a.index[value]
# a=[1,2]
# b=[3,4]
# c=a+b
# d=a*4
# print(a,b,c,d,sep='\n')

# students = [i for i in input().split()] #!!!!!
# print(students)

# a=[1,2,3,4]
# a.append([5,6])
# print(a)

# a=[1,2,3,4,5,6,4]
# print(a)
# a.remove(4)
# print(a)
# a.remove(4)
# print(a)
# del a[3]

# endregion
#####################################################
# region list slice minus index
# a=[1,2,3,4,5,6,7,8]
# print(a[7:-7:-1])
# print(a[-7:7:1])
# print(a[::-1]) #reverse, reversed
# endregion
#####################################################
# region sort/sorted reverse/reversed
# a=[1,5,8,9,2,3,5,7,8,2,3,4,5]
# print(a)
# a.sort()
# print(a)
# endregion
#####################################################
# region n size lists
# a=[[1,2,3],[3,4,5]]
# print(a[1][1])

n=int(input())
a=[[[0]*n]*n]*n
a[1][1]=123
print(*a,sep='\n')
print('ZZZZZZZZZZZZZZZZZZZZZZZZZZ')
a=[[[0]*n for j in range(n)] for i in range(n)]
a[1][1]=123
print(*a,sep='\n')
# endregion
#####################################################














