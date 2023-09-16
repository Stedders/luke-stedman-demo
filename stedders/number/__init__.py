import sys

from stedders.number._pretend_number import _PretendNumber

if __name__ == "__main__":
    raise RuntimeError("Module must be imported, it is not runnable")

sys.modules[__name__] = _PretendNumber(1)