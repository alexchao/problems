# -*- coding: utf-8 -*-


import unittest


from tree_problems import find_lowest_common_ancestor
from tree_problems import TreeNode


class FindLowestCommonAncestorTest(unittest.TestCase):

    def test_immediate_ancestor(self):
        tree1 = TreeNode(1)
        tree2 = TreeNode(2)
        tree3 = TreeNode(3)
        tree2.left = tree1
        tree2.right = tree3

        lca = find_lowest_common_ancestor(tree2, tree3, tree1)
        self.assertEqual(lca.val, 2)

    def test_immediate_ancestor_reverse(self):
        tree1 = TreeNode(1)
        tree2 = TreeNode(2)
        tree3 = TreeNode(3)
        tree2.left = tree1
        tree2.right = tree3

        lca = find_lowest_common_ancestor(tree2, tree1, tree3)
        self.assertEqual(lca.val, 2)


if __name__ == '__main__':
    unittest.main()
