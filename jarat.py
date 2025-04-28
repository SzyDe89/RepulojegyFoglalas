from abc import ABC, abstractmethod

class Jarat(ABC):
    def __init__(self, jaratszam: str, celallomas: str, jegyar: int):
        self.jaratszam = jaratszam
        self.celallomas = celallomas
        self.jegyar = jegyar

    @abstractmethod
    def jarat_tipus(self) -> str:
        pass

class BelfoldiJarat(Jarat):
    def jarat_tipus(self) -> str:
        return "Belföldi"

class NemzetkoziJarat(Jarat):
    def jarat_tipus(self) -> str:
        return "Nemzetközi"
