from unittest import TestCase

from taskling.Task import Task


class DataclassTests(TestCase):
    def test_entities(self):
        task = Task(name="test1", description="desc 1")
        self.assertEqual("test1", task.name)
        self.assertEqual("desc 1", task.description)
        self.assertFalse(task.note)
        print(task)

        task2 = Task(name="test2", note=True)
        self.assertTrue(task2.note)
