"""Verify that the make_full_name, extract_family_name, and
extract_given_name functions work correctly.
"""
from final_practice import add_grade_points, add_credits, compute_GPA, compute_percentile 
import pytest


def test_add_grade_points():
    """Verify that the add_grade_points function returns correct results.
    Parameters: none
    Return: nothing
    """
    assert add_grade_points("F","F","F","F","F","F",1, 1, 1, 1, 1, 1) == 0.0
    assert add_grade_points("A","F","B+","F","C","F",2, 3, 1, 4, 2, 0) == 15.3
    assert add_grade_points("A-","B+","B-","F","D","C+",2, 1, 4, 0, 0, 0) == 21.5
    assert add_grade_points("F","A","F","F","F","F",1, 2, 4, 3, 0, 0) == 8.0
    assert add_grade_points("B+","A","A","B","A","A",3, 2, 1, 2, 2, 4) == 51.9
    assert add_grade_points("D","F","C+","F","F","F",1, 2, 1, 0, 0, 0) == 3.3


def test_add_credits():
    """Verify that the add_credits function returns correct results.
    Parameters: none
    Return: nothing
    """
    assert add_credits(3,2,2,1,2,4) == 14
    assert add_credits(1,2,3,4,5,6) == 21
    assert add_credits(3,3,5,0,0,0) == 11
    assert add_credits(2,1,1,2,3,0) == 9
    assert add_credits(1,2,0,0,0,0) == 3
    assert add_credits(5,3,3,4,0,0) == 15


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
