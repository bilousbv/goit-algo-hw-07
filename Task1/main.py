import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.tree import Tree

class BinarySearchTree(Tree):
    def find_max(self):
        if self.root is None:
            return None  # Дерево порожнє
        return self._find_max(self.root)

    def _find_max(self, node):
        current = node
        while current.right:
            current = current.right
        return current.key

# Приклад використання
bst = BinarySearchTree()
max_value = bst.find_max()
print("Найбільше значення в дереві:", max_value)