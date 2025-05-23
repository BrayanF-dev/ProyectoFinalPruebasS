from typing import Any

from sympy.printing.numpy import NumPyPrinter  # NumPyPrinter is imported for backward compatibility
from sympy.printing.pycode import MpmathPrinter, PythonCodePrinter

__all__ = [
    "PythonCodePrinter",
    "MpmathPrinter",  # MpmathPrinter is published for backward compatibility
    "NumPyPrinter",
    "LambdaPrinter",
    "NumPyPrinter",  # Duplicate, see https://github.com/sympy/sympy/pull/27229
    "IntervalPrinter",
    "lambdarepr",
]

class LambdaPrinter(PythonCodePrinter):
    printmethod = ...

class NumExprPrinter(LambdaPrinter):
    printmethod = ...
    _numexpr_functions = ...
    module = ...
    def blacklisted(self, expr): ...

    _print_ImmutableDenseMatrix = ...
    _print_Dict = ...
    def doprint(self, expr) -> str | tuple[set[tuple[Any, str]], set[Any], str]: ...

class IntervalPrinter(MpmathPrinter, LambdaPrinter): ...

def lambdarepr(expr, **settings) -> str | tuple[set[tuple[Any, str]], set[Any], str]: ...
