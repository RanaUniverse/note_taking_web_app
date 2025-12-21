"""
This is for my learning checking codes...
"""

from functools import partial


def greet(
    name: str,
    language: str,
):
    if language == "en":
        return f"Hello {name}"
    if language == "bn":
        return f"নমস্কার {name}"


abc = greet("Rana", "en")
abc = greet("Rana", "bn")

def english_greet(name:str):
    return greet(name, "en")

abc = english_greet("Rana")
print(abc)


greet_english = partial(greet, language="eln")
xyz = greet_english("John Cena", language="bn")
print(xyz)