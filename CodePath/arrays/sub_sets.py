def sub_sets(num):
    if num == []:
        return [[]]
    else:
        x, xs = num[0], num[1:] 
        # print(x)
        # print(xs)
        sub = sub_sets(xs)
        # print(sub + [s + [x] for s in sub])
        return sub + [s + [x] for s in sub] 

print("subsets -> ",sub_sets([1,2,3]))