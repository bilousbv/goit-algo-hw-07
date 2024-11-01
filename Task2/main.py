import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modules.tree import Tree

class BinarySearchTree(Tree):
    def find_min(self):
        if self.root is None:
            return None  # Дерево порожнє
        return self._find_min(self.root)

    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current.key

# Приклад використання
bst = BinarySearchTree()
min_value = bst.find_min()
print("Найменше значення в дереві:", min_value)