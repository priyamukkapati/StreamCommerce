import importlib.util
import pathlib
import unittest


def load(name):
    path = pathlib.Path(__file__).resolve().parents[1] / "app.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ProjectTests(unittest.TestCase):
    def test_purchase_retry_and_conflict(self):
        store = load("streamcommerce").Store()
        for _ in range(2):
            store.purchase("req", "viewer", "creator", "gift", 500)
        self.assertEqual(store.revenue("creator"), 500)
        with self.assertRaises(ValueError):
            store.purchase("req", "viewer", "creator", "gift", 900)
        self.assertEqual(store.revenue("creator"), 500)
        with self.assertRaises(ValueError):
            store.purchase("bad", "viewer", "creator", "gift", -1)

