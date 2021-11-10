from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("Joshua", "Davey") == "Davey; Joshua"
    assert make_full_name("Bae", "Day") == "Day; Bae"
    assert make_full_name("Greg", "Baitly") == "Baitly; Greg"
    assert make_full_name(";") == ", "

#def test_extract_family_name():
#    assert extract_family_name("Joshua", "Davey") == "Joshua"
#     assert extract_family_name("Lu") == "Ludwig"
#     assert extract_family_name("Esquelda") == "Ludwig"
#     assert extract_family_name("Vandygriff") == "Ludwig"

# def test_extract_given_name():
#     assert extract_given_name("Joshua") == "Joshua"
#     assert extract_given_name("Travis") == "Joshua"
#     assert extract_given_name("Jogn") == "Joshua"
#     assert extract_given_name("") == "Joshua"


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])