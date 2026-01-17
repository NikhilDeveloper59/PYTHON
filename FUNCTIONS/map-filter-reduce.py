# map() :Apply function on every element.

nums = [1,2,3,4,5,6,7,8,9,10]

square = list(map(lambda x:x*x , nums))
print(square)

even = list(map(lambda x:x%2==0,nums)) # This is not filtr even number it only tells which is even or not
print(even)

cube = list(map(lambda x:x*x*x,nums))
print(cube)


# filter() : Filter elements based on condition.

nums = [1,2,3,4,5,6]
even = list(filter(lambda x: x%2==0, nums))
print(even)

odd = list(filter(lambda x:x%2 !=0,nums))
print(odd)

age = dict(Nikhil=21,Mohit=82,Rohit = 23,Sohan = 14,Sweta = 8,Chikku = 25)
print("<------Filter the age greater than 18 year------>")

result = list(filter(lambda item:item[1]>18,age.items()))
print(result)

# filter keys > 20
name = list(map(lambda item :item[0],filter(lambda item:item[1]>20,age.items())))
print(name)


d = dict(
    Nikhil=dict(age=33,roll=13,gender="male"),
    Mohit=dict(age=12,roll=13,gender="male"),
    Rohit=dict(age=23,roll=13,gender="male"),
    Sonu=dict(age=44,roll=13,gender="male")
)
name = list(map(lambda item:item[0],filter(lambda item:item[1]["age"]>23,d.items())))

# reduce():Needs: from functools import reduce
from functools import reduce

nums = [1,2,3,4]
product = reduce(lambda a,b: a*b, nums)
print(product)

sum = reduce(lambda a,b:a+b,nums)
print(sum)
