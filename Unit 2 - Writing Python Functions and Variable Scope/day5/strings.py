str1 = "hello"
str2 = "alpha"
str3 = "bet"
str4 = "alphabet"

print(len(str1)) # len() is the number of characters in a string
print(len(str4)) # the len() is one more than the largest positive index
print(len("Ryan")) # len() is 4. Largest positive index is 3
print(len("Enzo")) # len() is 4. Largest positive index is 3

print(str4[3]) # select a character using str[n] where n is an index
print(str4[-5])

print("hello"[2]) # selects the third character
print("hello"[-3])

# print("hello"[100]) # string index out of range
# print("hello"[len("hello")]) # String index out of range because "hello"[5] biggest index is 4


#[start:end:step] 

print(str4[2:5]) # End is not included

print("enzo"[2:4]) # gives "zo"

print("alphabet"[5:8])
print("alphabet"[-3:8])
print("alphabet"[-3:])
print("alphabet"[5:])

print("0123456789"[0:10:2]) # 02468
print("0123456789"[0:10:3]) # step of 4 "0369"

print("0123456789"[-1-11:-1]) # "987654321"

print("alphabet"[::2]) # starts at 0 and goes to the end

print("alphabet"[::2])

