class Solution:
    def connect(self, root):
        if not root:
            return root

        level = [root]

        while level:
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]

            level[-1].next = None

            next_level = []
            for node in level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            level = next_level

        return root