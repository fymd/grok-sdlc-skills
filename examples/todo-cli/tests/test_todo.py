"""Tests for the todo-cli reference example."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = Path(__file__).resolve().parent.parent / "src" / "todo.py"
_spec = importlib.util.spec_from_file_location("todo", SPEC)
todo = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(todo)


class TestTodo(unittest.TestCase):
    def setUp(self):
        self.store = Path(tempfile.mkdtemp()) / "store.json"

    def test_add_and_list(self):
        todo.add(self.store, "buy milk")
        items = todo.list_items(self.store)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["title"], "buy milk")
        self.assertFalse(items[0]["done"])

    def test_id_increments(self):
        a = todo.add(self.store, "first")
        b = todo.add(self.store, "second")
        self.assertEqual(a["id"], 1)
        self.assertEqual(b["id"], 2)

    def test_complete(self):
        it = todo.add(self.store, "task")
        self.assertTrue(todo.complete(self.store, it["id"]))
        self.assertTrue(todo.list_items(self.store)[0]["done"])
        self.assertFalse(todo.complete(self.store, 999))

    def test_remove(self):
        it = todo.add(self.store, "task")
        self.assertTrue(todo.remove(self.store, it["id"]))
        self.assertEqual(len(todo.list_items(self.store)), 0)
        self.assertFalse(todo.remove(self.store, 999))

    def test_empty_list(self):
        self.assertEqual(todo.list_items(self.store), [])

    def test_persistence_across_loads(self):
        todo.add(self.store, "a")
        todo.add(self.store, "b")
        items = todo.load(self.store)
        self.assertEqual(len(items), 2)


if __name__ == "__main__":
    unittest.main()
