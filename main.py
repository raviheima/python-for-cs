name, name_length = "neut", 4
list = [1,2,3,4]
dict = {"ls":"list current directory"}
tuple = ("food", "stew")
set = {1,2,3,4}
frozenset = { ("am", "i", "frozen")}

var_list = [list,dict,tuple,set,frozenset]
print(name)
print(name_length)

print(type(name_length))

for value in var_list:
    print(type(value))

boy = "7"

hmm = int(boy)
print("i am an ", type(hmm))