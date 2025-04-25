"""
Given a temp in F convert to C
"""

temp_f = input("temp in F")
print(type(temp_f))

#convert to int 
temp_c = (int(temp_f) -32)* 5/9

print("temp in c: " + str(temp_c))