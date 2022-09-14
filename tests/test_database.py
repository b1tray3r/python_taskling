import os
from genericpath import isdir
from pprint import pprint
from unittest import TestCase

import taskling
from taskling.Database import Database
from taskling.Task import dataclass_from_dict
from taskling.Task import Task


class DatabaseTests(TestCase):
    def test_entities(self):
        task = Task(name="test1", description="desc 1")
        self.assertEqual("test1", task.name)
        self.assertEqual("desc 1", task.description)
        self.assertFalse(task.note)

        if not os.path.isdir("tests/assets/"):
            os.mkdir("tests/assets/")

        if os.path.isfile("tests/assets/test.json"):
            os.remove("tests/assets/test.json")

        database = Database("tests/assets/test.json")
        database.create(task)
        self.assertEqual(1, len(database.get_all()))

        task_by_id = database.get_task(1)
        self.assertEqual("test1", task_by_id.name)

        task2 = Task(
            name="test2",
            description="desc 2",
        )
        database.create(task2)

        task_by_query = database.search_task("test1")
        self.assertEqual(len(task_by_query), 1)

        task_by_query = database.search_task("test2")
        self.assertEqual(len(task_by_query), 1)

        tasks_by_query = database.search_task("test")
        self.assertEqual(len(tasks_by_query), 2)
