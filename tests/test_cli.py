from unittest import TestCase

from docopt import docopt

usage = """Taskling

Usage:
    taskling
    taskling --create [--note] [--due=<date>] [--board=<board>] <name> <description>...
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


class CLITests(TestCase):
    def test_cli(self):
        cmd = [
            "-c",
            "-n",
            "--due",
            "2022-01-01",
            "--board",
            "testboard",
            "taskname",
            "a",
            "description",
            "message",
        ]
        args = docopt(usage, argv=cmd)
        self.assertTrue(args["--create"])
        self.assertTrue(args["--note"])
        self.assertEqual(args["--due"], "2022-01-01")
        self.assertEqual(args["--board"], "testboard")
        self.assertEqual(args["<name>"], "taskname")
        self.assertEqual(
            args["<description>"], ["a", "description", "message"]
        )

        cmd = ["--delete", "1"]
        args = docopt(usage, argv=cmd)
        self.assertTrue(args["--delete"])
        self.assertEqual(args["<taskid>"], ["1"])
