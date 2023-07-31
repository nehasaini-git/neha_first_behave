#  reverse a list
# list1 = [100, 200, 300, 400, 500]
# name = 'Neha'
# rev_list = list1[::-1]
# rev_name = name[::-1]
# print (rev_list)
# print (rev_name)

# Concatenate two lists index-wise
# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# list3 = [x+y for x,y in zip(list1,list2)]
# print (list3)

# Exercise 3: Turn every item of a list into its 
# numbers = [1, 2, 3, 4, 5, 6, 7]
# squared = [n**2 for n in numbers]
# print(squared)

#  Concatenate two lists
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# for x in list1:
#     for y in list2:
#         print (x+y)

#  Iterate both lists simultaneously
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for x,y in zip(list1,list2[::-1]):
#     print (x,y)

#remove blank spaces
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# print (filter(None,list1))

#   write a program to remove all occurrences of item 20.
# list1 = [5,20,15,20,25,50,20]
# while 20 in list1:
#     list1.remove(20)
# print (list1)
# print (list1.remove(200))

def solution(X, Y, A):
    N = len(A)
    result = -1
    nX = 0
    nY = 0
    for i in range(N):
        if A[i] == X:
            nX += 1
        elif A[i] == Y:
            nY += 1
        if nX == nY:
            result = i
        if nX == 0 and nY == 0:
            result = -1
    return result

c1 = (7 ,42, [6, 42,42, 11, 7, 1, 42])
c2 = (6, 13, [13, 13, 1, 6])
c3 =  (100, 63, [100, 63, 1, 6, 2, 13])

print (solution(7 ,42, [6, 42,42, 11, 7, 1, 42]))