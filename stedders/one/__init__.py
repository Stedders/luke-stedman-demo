"""
Demonstrates the dynamic nature of Python as a programming language.

The module "one" is actually an instance of _PretendNumber, which in turns inherits from a basic integer.

You can perform common integer actions to the module, e.g. `one + one` or `one * 5`.

The code will then emit another module representing the new number, e.g. one + one will return 2 and write the module
`two` to disk. The output module can then be imported as well (`import two`) and used in the same way.

The code uses several features of the language to achieve this.

 * A decorator takes the output of the function and writes the module
 * The decorator creates the module by reading the code (this file) and replacing 1 with the new value
 * The decorator is applied outside the class using reflection and monkeypatching, showing how it could be dynamically
   applied
 * The code then updates the module in memory using sys.modules

This is not intended to be a demonstration of good practice or of any actual use, but to show what you can do with
Python if you have a deep understanding of the language and its features.
"""

import sys
from functools import wraps
from pathlib import Path

import inflect

if __name__ == "__main__":
    raise RuntimeError("Module must be imported, it is not runnable")


def _convert_int(func: callable) -> callable:
    @wraps(func)
    def wrapper(self: _PretendInt, other: int | _PretendInt) -> int:
        result: int = func(self, other)
        module_name = (
            inflect.engine().number_to_words(result).replace(" ", "_").replace("-", "_")
        )
        Path(f"{module_name}.py").write_text(
            Path(__file__).read_text().replace(f"{int(self)}", f"{int(result)}")
        )
        return result

    return wrapper


class _PretendInt(int):
    pass


for method_name in (
    "__add__",
    "__sub__",
    "__mul__",
):
    setattr(_PretendInt, method_name, _convert_int(getattr(_PretendInt, method_name)))

sys.modules[__name__] = _PretendInt(1)
