import pytest
from hammingec.hamming_code import calc_redundant_bits, pos_redundant_bits, calc_parity_bits, detect_error


def test_calc_redundant_bits():
    assert calc_redundant_bits(4) == 3
    assert calc_redundant_bits(7) == 4
    assert calc_redundant_bits(11) == 4

def test_pos_redundant_bits():
    data = '1011001'
    r = calc_redundant_bits(len(data))
    result = pos_redundant_bits(data, r)
    assert result == '10101000100'  # Updated expected output

def test_calc_parity_bits():
    data = '1011001'
    r = calc_redundant_bits(len(data))
    arr = pos_redundant_bits(data, r)
    result = calc_parity_bits(arr, r)
    assert result == '10101001110'  # Updated expected output

def test_detect_error():
    error_data = '11101001110'
    r = calc_redundant_bits(len(error_data) - calc_redundant_bits(len('1011001')))
    error_position = detect_error(error_data, r)
    assert error_position == 10  # Updated expected output

if __name__ == "__main__":
    pytest.main()
