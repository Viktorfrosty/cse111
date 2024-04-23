# from address import extract_city, extract_state, extract_zipcode
# import pytest

# def test_extract_city():
#     city = extract_city("525 S Center St, Rexburg, ID 83460")
#     assert isinstance(city, str)

#     assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"

# def test_extract_state():
#     state = extract_state("525 S Center St, Rexburg, ID 83460")
#     assert isinstance(state, str)

#     assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"

# def test_extract_zipcode_str():
#     zipcode = extract_zipcode("525 S Center St, Rexburg, ID 83460")
#     assert isinstance(zipcode, str)

#     assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"

# def test_extract_zipcode_int():
#     zipcode = extract_zipcode("525 S Center St, Rexburg, ID 83460")
#     assert isinstance(zipcode, int)

#     assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == 83460

# """Call the main function that is part of pytest so that the
# computer will execute the test functions in this file."""
# pytest.main(["-v", "--tb=line", "-rN", __file__])


# [10:29] Cheung, Esther
from address import extract_city, extract_state, extract_zipcode
import pytest


def test_extract_city():

    city = extract_city("525 S Center St, Rexburg, ID 83460")

    assert isinstance(city, str)

    # Call the make_full_name function and verify that it returns a correct result.

    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"

 

 

def test_extract_state():

    state = extract_state("525 S Center St, Rexburg, ID 83460")

    assert isinstance(state, str)

    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"

 

 

def test_extract_zipcode():

    zipcode = extract_zipcode("525 S Center St, Rexburg, ID 83460")

    assert isinstance(zipcode, str)

    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"

 

 

# Call the main function that is part of pytest so that the

# computer will execute the test functions in this file.

pytest.main(["-v", "--tb=line", "-rN", __file__])