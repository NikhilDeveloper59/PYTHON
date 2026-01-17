# Condition: If s2 is rotation of s1, then s2 will be inside s1+s1.
# s1 = "ABCD"
# s1+s1 = "ABCDABCD"
# "CDAB" exists inside → rotation

s1 = "ABCD"
s2 = "CDAB"

new_string = s1*2

if(len(s2) != len(s1)):
    print("Rotation not exist becouse both having diffrent length")
else:
    if(s2 in (new_string)):
        print("Rotation is exist")
    else:
        print("Rotation not exist")
