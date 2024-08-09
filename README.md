# Hamming Code Error Correction 

This Python module provides functions for calculating Hamming codes, including redundant bit calculation, parity bit positioning, and error detection. Hamming codes are a popular method for error detection and correction in data transmission.

## Features

- **Calculate Redundant Bits:** Determine the number of redundant bits required for a given data length.
- **Position Redundant Bits:** Place redundant bits in their appropriate positions within the data.
- **Calculate Parity Bits:** Calculate the parity bits based on the redundant bits and the original data.
- **Detect Errors:** Detect and identify errors in transmitted data.

## Installation

To use this module, simply clone the repository and import the functions in your Python script:

```bash
git clone https://github.com/DJStompZone/hammingec.git
cd hammingec
```

## Usage Example

Here’s an end-to-end example of how to use the module to calculate Hamming codes and detect errors:

```python
from hammingec.hamming_code import calc_redundant_bits, pos_redundant_bits, calc_parity_bits, detect_error

# Step 1: Enter the data to be transmitted
data = '1011001'

# Step 2: Calculate the number of redundant bits required
r = calc_redundant_bits(len(data))
print(f"Number of redundant bits (r): {r}")

# Step 3: Determine the positions of redundant bits
data_with_redundant_bits = pos_redundant_bits(data, r)
print(f"Data with redundant bits positioned: {data_with_redundant_bits}")

# Step 4: Calculate the parity bits
data_with_parity_bits = calc_parity_bits(data_with_redundant_bits, r)
print(f"Data with parity bits: {data_with_parity_bits}")

# Step 5: Simulate an error in transmission (flipping a bit)
transmitted_data = '11101001110'  # Introduce an error in the 10th bit
print(f"Transmitted data with error: {transmitted_data}")

# Step 6: Detect the error
error_position = detect_error(transmitted_data, r)
if error_position == 0:
    print("There is no error in the received message.")
else:
    print(f"Error detected at position: {error_position} from the left (1-indexed)")
```

### Expected Output

Running the above example should produce the following output:

```plaintext
Number of redundant bits (r): 4
Data with redundant bits positioned: 10101000100
Data with parity bits: 10101001110
Transmitted data with error: 11101001110
Error detected at position: 10 from the left (1-indexed)
```

## Running Tests

This module includes test cases that can be run using `pytest`. To run the tests, simply execute:

```bash
pytest
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.
