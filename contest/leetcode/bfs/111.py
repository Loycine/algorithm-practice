class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = deque([(root, 1)])

        while q:
            temp_size = len(q)
            for _ in range(temp_size):
                cur, depth = q.popleft()
                if not cur.left and not cur.right: return depth
                if cur.left: q.append((cur.left, depth+1))
                if cur.right: q.append((cur.right, depth+1))


if __name__ == "__main__":
    sln = Solution()
    print(sln.minDepth(TreeNode()));        