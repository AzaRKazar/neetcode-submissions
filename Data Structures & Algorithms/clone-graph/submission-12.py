"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node :
            return None
        old_new={}

        def clone(node):
            if node in old_new:
                return old_new[node]

            old_new[node]=Node(node.val)
            
            copy=old_new[node]
            
            for neighbor in node.neighbors:
                copy.neighbors.append(clone(neighbor))
            return copy
        
        return clone(node)