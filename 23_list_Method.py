'''
Lists Method :

1] Append():
This method of list where elements add in last position 

lst=[2,3,4,6]
lst.append(5)
print(lst)

Output ==> [2, 3, 4, 6, 5]


2] Sort ():
This method sort the list asending order . The original list updated


lst=[34,11,9,2,23,345]
lst.sort()
print(lst)

Output ==> [2, 9, 11, 23, 34, 345]


Decending Order: 
lst=[34,11,9,2,23,345]

lst.sort(reverse=True)
print(lst)

OUtput ==> [345, 34, 23, 11, 9, 2]

3] reverse :

This method used to reverse the list 

4] index():

This method returns the index of the first occurence of the list  item 

a=[2,3,2,2,5,2]

print(a.index(2,2,4))
            (value , start ,end)

outPut==> 2

5]Count():
Returns the count of the numbers of items with given value

b=[2,3,2,3,2,2]

print(b.count(2)) //4
print(b.count(3)) //2

6] Copy():

i]

l=[2,23,45,22,11]

ml=l

ml[0]=1

print(l) ==> [1, 23, 45, 22, 11] // It changes Original [l list]

ii]

instance of this use copy() method safe

l=[2,23,45,22,11]

ml=l.copy()
ml[0]=1
print(l) // [2, 23, 45, 22, 11]
print(ml) //[1, 23, 45, 22, 11]


'''

