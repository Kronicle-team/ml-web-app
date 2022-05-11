"""
<!-- /***************************************************************
*Title: awesome-streamlit
*Author: Marc Skov Madsen
*Date: 9 October 2019
*Availability: https://github.com/MarcSkovMadsen/awesome-streamlit/blob/master/tests/test_platform.py (Accessed 11 May 2022)
****************************************************************/  -->
"""

"""General tests of the platform"""
import platform
import sys


def test_64bit():
    """We test that Python is running as 64 bit and not 32 bit."""
    assert platform.architecture()[0] == "64bit"


def test_python_version():
    """We test that Python is the correct version"""
    major, minor, _, _, _ = sys.version_info
    assert (major, minor) == (3, 8)