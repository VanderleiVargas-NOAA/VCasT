# processing/__init__.py

"""
Processing Module for VCasT
---------------------------
This module contains functionality for parallel computation and data interpolation.

Modules:
- parallel_processing.py: Handles multiprocessing execution for data processing.
- interpolation.py: Implements interpolation techniques for data transformation.
- postprocessing.py: Implements the class StatisticalSignificance.
"""

from .interpolation import interpolate_to_target_grid
from .parallel_processing import process_in_parallel
from .postprocessing import StatiscalSignificance

__all__ = ["process_in_parallel", "interpolate_to_target_grid",
           "StatiscalSignificance"]
