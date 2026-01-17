d = {"a": 10, "c": 5, "b": 25}


#  sort based on key
sorted_dict = dict(sorted(d.items()))
print(sorted_dict) # {'a': 10, 'b': 25, 'c': 5}

#  sort based on value 
#  Before sort we have to know about that
# lambda arguments: expression , example: lambda x: x + 1 ,that means take x and return x + 1
# key=lambda x: x[1] means: x is one tuple like ["a",10] , so x[0] is a key and x[1] is a value


sorted_dict = dict(sorted(d.items(),key=lambda x:x[0])) # sort based on key
sorted_dict = dict(sorted(d.items(),key=lambda x:x[1])) # sort based on value

print(sorted_dict)