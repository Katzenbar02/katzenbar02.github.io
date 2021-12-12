"""Verify that the make_full_name, extract_family_name, and
extract_given_name functions work correctly.
"""
from Final import *
from Final import add_grade_points, add_credits, compute_GPA, compute_percentile 
import pytest


def test_add_grade_points():
    """Verify that the add_grade_points function returns correct results.
    Parameters: none
    Return: nothing
    """
    assert add_grade_points() == 16.0


def test_add_credits():
    """Verify that the add_credits function returns correct results.
    Parameters: none
    Return: nothing
    """
    assert add_credits() == 1


def test_compute_GPA():
    """Verify that the compute_GPA function returns correct results.
    Parameters: none
    Return: nothing
    """
    assert compute_GPA(4.0, 1) == 4.00
    assert compute_GPA(40, 14) == 2.86
    assert compute_GPA(30.3, 10) == 3.03
    assert compute_GPA(18.4, 6) == 3.07
    assert compute_GPA(17.0, 8) == 2.12
    assert compute_GPA(15.8, 9) == 1.76
    assert compute_GPA(0, 12) == 0.00
    assert compute_GPA(51.3, 14) == 3.66



def test_compute_percentile():
    """Verify that the compute_percentile function returns correct results.
    Parameters: none
    Return: nothing
    """
    assert compute_percentile(4) == "95th percentile"
    assert compute_percentile(3.5) == "90th percentile"
    assert compute_percentile(3) == "85th percentile"
    assert compute_percentile(2.5) == "80th percentile"
    assert compute_percentile(2) == "75th percentile"
    assert compute_percentile(1.5) == "70th percentile"
    assert compute_percentile(1) == "65th percentile"
    assert compute_percentile(0) == "Below 65th percentile"



# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])
