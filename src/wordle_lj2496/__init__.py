# read version from installed package
from importlib.metadata import version
__version__ = version("wordle_lj2496")
from wordle_lj2496.wordle_lj2496 import validate_guess, check_guess

__all__ = ["validate_guess", "check_guess"]