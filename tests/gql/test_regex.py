import sys

from project.gql.interpreter.types.regex import Regex
from project.gql.interpreter.exceptions import NotImplementedException
import pytest

if sys.platform.startswith("win"):
    pytest.skip("Windows is unsupported", allow_module_level=True)
else:
    from tools import interpret

