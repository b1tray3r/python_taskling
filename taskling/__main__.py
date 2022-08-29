"""Taskling

Usage:
    taskling
    taskling --create [--note] [--due=<date>] [--board=<board>] <task> <description>...
    taskling --edit [--due=<date>] [--board=<board>] <taskid> [<description>...]
    taskling (--delete | --restore) <taskid>...
    taskling (--begin | --check) <taskid>...
    taskling (--star | --priority=<priority>) <taskid>...
    taskling --list (--timeline | --boards | --priority=(ASC | DESC))
    taskling (--purge | --clear)
    taskling --find <search>


Options:
    none                    Show this usage help text.
    --create, -c            Create a new task.
    --note, -n              Create a note instead of a task.
    --edit, -e              Edit a task.
    --delete, -d            Delete a task.
    --restore, -r           Restore a task.
    --begin, -b             Begin working on a task.
    --check, -x             End working on a task.
    --star, -s              Mark a tasks as important.
    --list                  List the tasks by id.
    --timeline              List the tasks by creation date.
    --boards                List the tasks by boards.
    --purge                 Delete everything.
    --clear                 Move finished tasks to archive.
    --find                  Search for a task

"""
import os

from Database import Database
from docopt import docopt
from Task import Task
from xdg import xdg_config_home


def main():
    args = docopt(__doc__, version="Taskling 1.0")
    print(args)


if __name__ == "__main__":
    main()

    if not os.path.isdir(f"{xdg_config_home()}/taskling/"):
        os.makedirs(f"{xdg_config_home()}/taskling/")

    active = Database(f"{xdg_config_home()}/taskling/active.json")

    new_id = active.create(Task("test", "desc"))
    active.update(new_id, Task("test2", "better desc", note=True))

    print(active.delete(new_id))
