#how tall is the tree 
#use 1 loop and 3 for loop 
#4 space : 1 hash 
#3 space : 3 hash
#2 space : 5 hash
#1 space : 7 hash
#0 space : 9 hash
#4 space : 1 hash
#decrement the space by 1 unit 
#increment the hash by 2 unit 
#calculate the space height of the tree minus 1


#get the number of rows for the trees
Tree_height = input("how much height do you want ")
Tree_height = int(Tree_height)
spaces = Tree_height - 1 
hashes = 1 
stump_spaces = Tree_height - 1

while Tree_height != 0:
    for i in range(spaces):
        print(' ',end="")
    for i in range(hashes):
        print('#',end="")
    print()
    spaces -= 1
    hashes += 2
    Tree_height -= 1

for i in range(stump_spaces):
    print(' ',end="")

print("#")
