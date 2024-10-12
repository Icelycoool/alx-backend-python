#!/usr/bin/env python3
"""element_length function"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Computes the length of each element in an iterable of sequences."""
    return [(i, len(i)) for i in lst]
