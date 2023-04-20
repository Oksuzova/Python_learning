from PyQt6.QtCore import QObject, pyqtSignal
import re
import random


class SetManager(QObject):
    value_changed = pyqtSignal(str)
    range_changed = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__()
        self.sets_names = ["setA", "setB", "setC", "setU"]
        self._store = {i: set() for i in args}
        self._weight = {i: dict(min=0, max=0) for i in args}  # we use max value by default weight

    def get_value(self, name: str):
        return self._store.get(name)

    def get_weight_value(self, name: str):
        return self._weight.get(name)["max"]

    def set_value(self, name: str, value: set):
        self._store[name] = value
        self.value_changed.emit(name)

    def set_value_from_str(self, name: str, value: str):
        val = set(re.split(r"[,:;\s]", value))
        val.discard("")
        self.set_value(name, val)

    def set_range(self, name: str, value: int):
        if name == 'setU_max':
            self._weight['setU']['max'] = int(value or 0)
            self.range_changed.emit('setU')
        elif name == 'setU_min':
            self._weight['setU']['min'] = int(value or 0)
            self.range_changed.emit('setU')
        else:
            self._weight[name]['max'] = int(value or 0)
            self.range_changed.emit(name)

    def gen_random_sets(self):
        self.random_uniset_range = range(self._weight['setU']['min'], self._weight['setU']['max'])
        for i in self.sets_names[:-1]:
            self.set_value(i, set(random.sample(self.random_uniset_range, self.get_weight_value(i))))
        self.make_unisets()
        self.save_sets()

    def gen_by_hand_sets(self):
        for i in self.sets_names[:-1]:
            self._store.get(i)
        self.make_unisets()
        self.save_sets()

    def make_unisets(self):
        uniset = set()
        for i in self.sets_names[:-1]:
            uniset |= self.get_value(i)
        self.set_value("setU", uniset)

    def save_sets(self):
        with open ("result.txt", "w") as f:
            for i in self.sets_names:
                f.write(f"{i}: {self.get_value(i)}\n")
