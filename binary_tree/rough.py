class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def allPaths(root, sum, nlist): # 
    if root: 

        nlist + [root.val]

        if root.left == None and root.right == None and sum-root.val == 0:   
            return nlist + [root.val] # [1,2,4], [1,3]

        else :
            left = allPaths(root.left, sum-root.val, nlist + [root.val])  # left = allPaths(2) , allPths(none,[1,2]) | left =[] | left =[[1,2,4]]
            right = allPaths(root.right, sum-root.val, nlist + [root.val]) # right = allPath(4,[1,2]) | right = [1,2,4] | allPath(3,[1]) |  rigt = [1,3] 
    
        return [left] + [right] # [[[1,2,4]],[1,3]]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(6) 
root.left.left = TreeNode(3)
root.left.right = TreeNode(4) 

print(allPaths(root, 7, nlist=[]))   

'''
return [left[-1]]
    does not work if the tree has a left child 
'''

'''
    def pathSum(root,sum):
        def path(root, summ, p): # path(5,0,p=[]) | path(4,5,[5]) | path(11,9,[5,4]) | path(7,20,[5,4,11]) || path(2,20,[5,4,11]) | path(8,5,[5]) | path(13,13,[5,8])|path(none,26,[5,8,13])| path(4,13,[5,8]) | path(5,17,[5,8,4,5])
            if root == None: 
                return self.paths 
            
            if root.left == None and root.right == None: # f | f | f | T  || T | f | T | f | T
                if summ + root.val == sum: # 20+7 = 27 != 22 : f || 20+2 = 22 == 22 : t | 13+13=26 != 22 : f | 17+5 = 22 == 22 : T
                    p + [root.val] # p = [5,4,11,2] | p = [5,8,4,5]
                    self.paths + [p] # paths = [5,4,11,2] | path = [5,4,11,2],[5,8,4,5]
                    # print(p) 
                return self.paths 
                # 
            p.append(root.val) # p = [5] | [5,4] | [5,4,11] | [5,8] | [5,8,13] | [5,4,8,4] 

            path(root.left, summ+root.val, p) # path(4,5,[5]) | 👈🏻 path(11,9,[5,4]) | 👈🏻 path(7,20,[5,4,11])  nothing returned | path(13,13,[5,8])| path(none,26,[5,8,13]) | path(none)
            path(root.right, summ+root.val, p) # path(2,20,[5,4,11]) | path(8,5,[5]) | path(4,13,[5,8]) | path(5,17,[5,8,4,5]) | path(1,22,[])

        p = [] 
        path(root,0,p)  
        return self.paths 


# if root: # 1 ,2 
    #     temp.append(root.val)  # temp =[1,2,4]
         
    #     if root.left == None and root.right == None:  #  
    #         return nlist.append(temp)  # nlist=[1,2,4] 

    #     else:
    #         left = allPaths(root.left, nlist, temp[:])  # left = allPaths(2,[],[1]) , left = allPaths(none,[],[1,2])   
    #         right = allPaths(root.right, nlist, temp[:]) # right = allPaths(4,[],[1,2]). allpaths(4,[1,2,4], [1,2,4])

    # return nlist  
'''


'''
nlist = []
def allPaths(root, nlist): # (1,[]) , (2, [1]) , (none, [1,2])  , (3, [1,2]) 
    
    if root == None: 
        return nlist []

    else :
        nlist.append(root.val) # [1,2], []

        left = allPaths(root.left, nlist)  # allPaths(2, [1]) | allpaths(none, [1,2]) | [1,2]
        right = allPaths(root.right, nlist) # allPaths (3, [1,2]) 

    

def allPaths(root, nlist): #  allPaths(1,[]) | allPaths(2,[1]) | appPaths(none,[1,2]) | allPaths(4,[1,2]) | allPaths(3,[1])
    
    if root ==  None : # 
        return [] # []
         
    if root.left == None and root.right == None:   
        return nlist + [root.val] # [1,2,4], [1,3]

    else :
        left = allPaths(root.left, nlist + [root.val])  # left = allPaths(2) , allPths(none,[1,2]) | left =[] | left =[[1,2,4]]
        right = allPaths(root.right, nlist + [root.val]) # right = allPath(4,[1,2]) | right = [1,2,4] | allPath(3,[1]) |  rigt = [1,3] 
    return [left] + [right] # [[[1,2,4]],[1,3]]
'''