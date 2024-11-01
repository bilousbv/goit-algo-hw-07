import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.tree import Tree

class BinarySearchTree(Tree):
    def sum_tree(self):
        return self._sum_tree(self.root)

    def _sum_tree(self, node):
        if node is None:
            return 0
        # Рекурсивно обчислюємо суму лівого та правого піддерев і додаємо значення поточного вузла
        return node.key + self._sum_tree(node.left) + self._sum_tree(node.right)


# Приклад використання
bst = BinarySearchTree()
total_sum = bst.sum_tree()
print("Сума всіх значень у дереві:", total_sum)