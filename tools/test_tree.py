import unittest
import tree


class TestTree(unittest.TestCase):
    def test_creation(self):
        my_tree = tree.Tree("root node")
        self.assertEqual(my_tree.data, "root node")
        self.assertIsNone(my_tree.parent)
        self.assertEqual(my_tree.children, [])

    def test_add_child(self):
        my_tree = tree.Tree("root node")
        my_tree.add_child("child a")
        my_tree.add_child("child b")
        my_tree.children[0].add_child("child a, 1")
        my_tree.children[0].add_child("child a, 2")
        my_tree.children[0].add_child("child a, 3")

        self.assertEqual(len(my_tree.children), 2)
        self.assertEqual(my_tree.children[0].data, "child a")
        self.assertEqual(my_tree.children[1].data, "child b")
        self.assertEqual(my_tree.children[0].children[0].data, "child a, 1")
        self.assertEqual(my_tree.children[0].children[2].data, "child a, 3")

        self.assertEqual(len(my_tree.children[0].children), 3)
        self.assertEqual(len(my_tree.children[0].children[0].children), 0)
        self.assertEqual(len(my_tree.children[1].children), 0)

        my_tree.add_child("child b, 1", parent=my_tree.children[1])
        self.assertEqual(len(my_tree.children[1].children), 1)
        self.assertEqual(my_tree.children[1].children[0].data, "child b, 1")

    def test_has_child(self):
        my_tree = tree.Tree("root node")
        my_tree.add_child("child a")
        my_tree.add_child("child b")
        my_tree.children[0].add_child("child a, 1")

        self.assertTrue(my_tree.has_children())
        self.assertTrue(my_tree.children[0].has_children())
        self.assertFalse(my_tree.children[1].has_children())
        self.assertFalse(my_tree.children[0].children[0].has_children())

    def test_max_depth(self):
        my_tree = tree.Tree("root node")
        my_tree.add_child("child a")
        my_tree.add_child("child b")
        my_tree.children[0].add_child("child a, 1")
        my_tree.children[0].add_child("child a, 2")
        my_tree.children[0].add_child("child a, 3")

        self.assertEqual(tree.get_max_depth(my_tree), 2)
        self.assertEqual(tree.get_max_depth(my_tree.children[0]), 1)

    def test_node_depth(self):
        my_tree = tree.Tree("root node")
        my_tree.add_child("child a")
        my_tree.add_child("child b")
        my_tree.children[0].add_child("child a, 1")
        my_tree.children[0].add_child("child a, 2")
        my_tree.children[0].add_child("child a, 3")

        self.assertEqual(tree.get_node_depth(my_tree), 0)
        self.assertEqual(tree.get_node_depth(my_tree.children[0]), 1)
        self.assertEqual(tree.get_node_depth(my_tree.children[1]), 1)
        self.assertEqual(tree.get_node_depth(my_tree.children[0].children[1]), 2)

    def test_get_end_nodes(self):
        my_tree = tree.Tree("root node")
        my_tree.add_child("child a")
        my_tree.add_child("child b")
        my_tree.children[0].add_child("child a, 1")
        my_tree.children[0].add_child("child a, 2")

        self.assertEqual(sorted(list([n.data for n in tree.get_end_nodes(my_tree)])), sorted(list([i.data for i in [
            my_tree.children[1],
            my_tree.children[0].children[0],
            my_tree.children[0].children[1]
        ]])))

    def test_get_branch_items(self):
        my_tree = tree.Tree("root node")
        my_tree.add_child("child a")
        my_tree.add_child("child b")
        my_tree.children[0].add_child("child a, 1")
        my_tree.children[0].add_child("child a, 2")

        self.assertEqual(tree.get_branch_items(my_tree.children[0].children[0]), ['child a, 1', 'child a', 'root node'])
        self.assertEqual(tree.get_branch_items(my_tree), ['root node'])

    def test_get_nodes_at_depth(self):
        my_tree = tree.Tree("root node")
        my_tree.add_child("child a")
        my_tree.add_child("child b")
        my_tree.children[0].add_child("child a, 1")
        my_tree.children[0].add_child("child a, 2")

        self.assertEqual(sorted(list([x.data for x in tree.get_nodes_at_depth(my_tree, 1)])), sorted([
            "child a",
            "child b"
        ]))

        self.assertEqual(sorted(list([x.data for x in tree.get_nodes_at_depth(my_tree, 2)])), sorted([
            "child a, 1",
            "child a, 2"
        ]))

        print(tree.get_nodes_at_depth(my_tree, 1))


if __name__ == '__main__':
    unittest.main()
