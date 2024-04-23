#import from modules and files
import pytest
from tempfile import mktemp
from os import path
import io
import sys
from firebase_centralized_data_reader import file_reader, retrieve_specific_info, get_general_info

def test_file_reader():
    """Verify that the file_reader function works correctly.
    Parameters: none
    Return: nothing
    """
    
    # Dictionary Key Index
    ID_INDEX = 0
    
    # Verify that the file_reader function uses its filename
    # parameter by doing the following:
    # 1. Get a filename for a file that doesn't exist.
    # 2. Call the file_reader function with the filename.
    # 3. Verify that the open function inside the file_reader
    #    function raises a FileNotFoundError.
    filename = mktemp(dir=".", prefix="not", suffix=".csv")
    with pytest.raises(FileNotFoundError):
        file_reader(filename, ID_INDEX)
        pytest.fail("file_reader function must use its filename parameter")
    
    # Call the file_reader function and store the returned dictionary in a variable named products_dict.
    # Please use the provided CSV file for the evaluation.
    filename = path.join(path.dirname(__file__), "emergency_reg.csv")
    regs_dict = file_reader(filename, ID_INDEX)

    # Verify that the file_reader function returns a dictionary.
    assert isinstance(regs_dict, dict), \
        "file_reader function must return a dictionary:" \
        f" expected a dictionary but found a {type(regs_dict)}"

    # Verify that the registers dictionry contains exactly 100 entries.
    length = len(regs_dict)
    exp_len = 100
    assert length == exp_len, \
        "register dictionary has too" \
        f" {'few' if length < exp_len else 'many'} entries:" \
        f" expected {exp_len} but found {length}"

def test_retrieve_specific_info():
    # Redirect stdout to a buffer
    sys.stdout = io.StringIO()

    regs_dict = {"1": ["value1", "value2", "value3","value4", "value5", "value6","value7", "value8", "value9","value10", "value11", "value12","value13", "value14", "value15","value16", "value17", "value18","value19", "value20", "value21","value22", "value23", "value24", "value25", "value26","value27", "value28", "value29", "value30", "value31","value32", "value33", "value34", "value35", "value36"]}
    key = "2"
    retrieve_specific_info(regs_dict, key)
    
    # Get output and restore stdout
    output = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    
    assert "\n Register not found" in output

    # Redirect stdout to a buffer again for the second test
    sys.stdout = io.StringIO()

    key = "1"
    retrieve_specific_info(regs_dict, key)

    # Get output and restore stdout
    output = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__

    assert "\nCall Number: 1" in output

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])