"""
Basic tests for the one module, demonstrate how to properly assert all behaviours.

Expected behaviour:
 1. The basic int operations (+, -, *) all work
 2. The returned result is correct, e.g. one + 1 == 2
 3. When the int operation is performed a new module is produced, e.g. two.py for the above operation
 4. The new module can be imported
 5. The module represents the correct value

Bonus points:
 1. Store the output in a temp directory
 2. Clean up after the test to prevent artifacts clogging up folders
"""

import os
import shutil
import sys
import tempfile
from pathlib import Path

import pytest

from stedders import one


@pytest.fixture(name="one_test_fixture", scope="function", autouse=True)
def one_test_setup_and_teardown() -> None:
    """
    Pytest fixture to setup and teardown the test directory.

    Set to be called for each test function, automatically used so you don't need to call it.

    Set-up:
        Creates a temporary directory in the OS tmp path, cd's to the directory, adds the directory to the sys.path

    Run Test

    Teardown:
        Removes the directory from the sys.path, changes back to the current directory and deletes the temp folder

    :return: None
    """

    # tempfile context manager is really useful, creates a temp directory for you
    with tempfile.TemporaryDirectory() as tmp_dir:
        # Get the current path
        cwd = Path.cwd()
        # cd to the tmp dir created, this ensures the modules are written to the temp folder
        os.chdir(tmp_dir)
        # Add the tmp dir to the sys path, this allows python to import them
        sys.path.append(tmp_dir)
        # The yield statement is usually associated with generators, in this instance it yields to the running test
        yield
        # Remove the tmp dir from the path, prevent polluting imports for other tests
        sys.path.pop(-1)
        # cd back to the original directory
        os.chdir(cwd)
        # remove the temp dir and the contents
        shutil.rmtree(tmp_dir)


def test_initial_number():
    # Basic test to check our module is consistent
    assert one == 1


def test_addition():
    # Check result is correct
    assert one + 6 == 7
    # Check file has been written
    assert Path("seven.py").exists()

    # import the new module, intellisense doesn't like this as we are dynamically setting the path in the fixture
    import seven

    # Check the module matches the correct value
    assert seven == 7


def test_multiplcation():
    assert one * 5 == 5
    assert Path("five.py").exists()

    import five

    assert five == 5


def test_subtraction():
    assert one - 5 == -4
    assert Path("minus_four.py").exists()

    import minus_four

    assert minus_four == -4
