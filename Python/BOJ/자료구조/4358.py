import sys
lines = sys.stdin.readlines()
tree_type = dict()
for line in lines:
    t = line.rstrip()
    if tree_type.get(t) == None:
        tree_type[t] = 1
    else:
        now_count = tree_type[t]
        tree_type[t] = now_count+1
total_num = sum(tree_type.values())
tree_list = sorted(tree_type.items())
for i in tree_list:
    print(f"{i[0]} {i[1]/total_num*100:.4f}")
