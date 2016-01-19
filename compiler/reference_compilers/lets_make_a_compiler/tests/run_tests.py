"""

NOTE: for now this is just intended to be run as python -m tests from the
compiler directory (parent directory of this file).
"""
import logging
import unittest

try:
    from tests import TestInitialization, TestArithmetic, TestParenthese
except ImportError:
    # Work around to allow for calling specific unit tests as a script and
    # but all of the unit tests as a module.
    from . tests import TestInitialization, TestArithmetic, TestParenthese


def run_tests():
    # TODO: Accept command line arguments for running tests.
    # TODO: Accept logging arguments.
    # TODO: include better logging capabilities.
    logging.basicConfig()
    unittest.main()
