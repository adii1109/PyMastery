""""
== Sets Method ==


I] Union and Update: 

> The Union() and update() Method prints all items that are present in two sets
> The Union Method  return a new set .
> update() Method adds item into the existing set from another set


Example: 
s1={"india","England","china","bhutan"}
s2={"india","bhutan","England","Sauth Africa"}

s3=s1.union(s2)
print(s3)
# Output ==> {'England', 'bhutan', 'Sauth Africa', 'china', 'india'}

s1.update(s2)
print(s1)
# Output ==> {'England', 'bhutan', 'Sauth Africa', 'china', 'india'}

----------------------------------------------------------------------------------
ii] intersection() and intersection_update():

> the intersection and intersection_update() prints items that are similar to the both sets
> the intersection method return new set
> intersection_update() method update into existing sets from another set

Example: 

s1={"india","England","Austrilia","bhutan"}
s2={"india","bhutan","England","Sauth Africa"}

s3=s1.intersection(s2)
print(s3)
# Output==> {'England', 'bhutan', 'india'}
s1.intersection_update(s2)
print(s1)
# Output==> {'England', 'bhutan', 'india'}
----------------------------------------------------------------------------------

"""

