from dataclasses import dataclass


@dataclass
class Dataset:
    dname: object
    sname: object
    fname: object
    train: object
    test: object
    id: object
    label: object

    @property
    def dname(self) -> object: return self._dname

    @dname.setter
    def dname(self, dname) -> object: self._dname = dname

    @property
    def sname(self) -> object: return self._sname

    @sname.setter
    def sname(self, sname) -> object: self._sname = sname

    @property
    def fname(self) -> object: return self._fname

    @fname.setter
    def fname(self, fname) -> object: self._fname = fname

    @property
    def train(self) -> object: return self._train

    @train.setter
    def train(self, train) -> object: self._train = train

    @property
    def test(self) -> object: return self.test

    @test.setter
    def test(self, test) -> object: self.test = test

    @property
    def label(self) -> object: return self.label

    @label.setter
    def label(self, label) -> object: self.label = label

    @property
    def id(self) -> object: return self.id

    @id.setter
    def id(self, id) -> object: self.id = id