st = {1,2,5,7,8,4,9}

print(st)

# remove() vs discard()
st.remove(5) # show errom when element is not found
st.discard(10) # no error 

print(st)

# pop() (removes random item)
st.pop()
print(st)


st.clear()
print(st) # set()