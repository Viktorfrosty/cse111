from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    """Verify that the make_full_name function works correctly.
    Parameters: none
    Return: nothing
    """
    full_name = make_full_name("Sally", "Brown")
    assert isinstance(full_name, str), "prefix function must return a string"

    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Jane", "Doe") == "Doe; Jane"
    assert make_full_name("Bob", "Smith") == "Smith; Bob"
    assert make_full_name("Taylor", "Jackson") == "Jackson; Taylor"
    assert make_full_name("", "") == "; "

def test_extract_family_name():
    """Verify that the extract_family_name function works correctly.
    Parameters: none
    Return: nothing
    """
    family_name = extract_family_name("Brown; Sally")
    assert isinstance(family_name, str), "prefix function must return a string"
    
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Doe; Jane") == "Doe"
    assert extract_family_name("Smith; Bob") == "Smith"
    assert extract_family_name("Jackson; Taylor") == "Jackson"
    assert extract_family_name("; ") == ""

def test_extract_given_name():
    """Verify that the extract_given_name function works correctly.
    Parameters: none
    Return: nothing
    """
    given_name = extract_given_name("Brown; Sally")
    assert isinstance(given_name, str), "prefix function must return a string"
    
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Doe; Jane") == "Jane"
    assert extract_given_name("Smith; Bob") == "Bob"
    assert extract_given_name("Jackson; Taylor") == "Taylor"
    assert extract_given_name("; ") == ""

"""Call the main function that is part of pytest so that the
computer will execute the test functions in this file."""
pytest.main(["-v", "--tb=line", "-rN", __file__])