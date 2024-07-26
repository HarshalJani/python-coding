#314 - LC - Binary Tree Vertical Order Traversal

class TreeNode:
	def __init__(self, val, left, right):
		self.val = val
		self.left = left
		self.right = right

class Solution:
   	def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
		
		mapper = defaultdict(list)
		
        	def dfs(x, y, node):
            		if not node: return
            			dfs(x-1,y+1,node.left) #we decrement x by 1 as we go further left and increment y by 1 as we go down to next level
            			dfs(x+1,y+1,node.right)#we increment x by 1 as we go further right and increment y by 1 as we go down to next level
            			mapper[(x,y)].append(node.val)
		
        	dfs(0,0, root)
		
        	output = []
        	leftmost_position = float("-inf")
        	print("mapper", sorted(mapper.items()))
        	for k, v in sorted(mapper.items()):
           		print("v",v)
            		if k[0] != leftmost_position:
                		output.append([])
            		output[-1].extend(sorted(v))
            		leftmost_position = k[0] #We will move the leftmost position so we can add vertically from left to right
            
        	return output