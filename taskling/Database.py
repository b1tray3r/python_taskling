from dataclasses import asdict

from pysondb import PysonDB
from Task import dataclass_from_dict
from Task import Task


class Database(PysonDB):
    _id = 0

    def _gen_id(self) -> str:
        return str(self._id + 1)

    def create(self, task: Task) -> str:
        if self._id == 0:
            self._id = len(self.get_all())

        return self.add(asdict(task))

    def create_with_id(self, id: int, task: Task) -> str:
        return ""

    def update(self, id: int, task: Task) -> str:
        return self.update_by_id(id, asdict(task))

    def delete(self, id: int) -> Task:
        data = self.get_by_id(id)
        task = dataclass_from_dict(Task, data)
        self.delete_by_id(id)
        return task
