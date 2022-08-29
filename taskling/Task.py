from dataclasses import dataclass


def dataclass_from_dict(klass, dikt):
    try:
        fieldtypes = klass.__annotations__
        return klass(
            **{f: dataclass_from_dict(fieldtypes[f], dikt[f]) for f in dikt}
        )
    except AttributeError:
        if isinstance(dikt, (tuple, list)):
            return [dataclass_from_dict(klass.__args__[0], f) for f in dikt]
        return dikt


@dataclass
class Task:
    name: str
    description: str = ""
    note: bool = False
    due: str = ""
    board: str = "default"
    begin: str = ""
    end: str = ""
    star: bool = False
    priority: int = 5
