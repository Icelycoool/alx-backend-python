#!/usr/bin/env python3
"""safe_first_element function"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Safely retrieves the first element of a sequence."""
    if lst:
        return lst[0]
    else:
        return None
