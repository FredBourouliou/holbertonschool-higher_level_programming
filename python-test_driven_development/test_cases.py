#!/usr/bin/python3
from 101_lazy_matrix_mul import lazy_matrix_mul

def test_case(test_name, m_a, m_b):
    print(f"\nTest: {test_name}")
    try:
        result = lazy_matrix_mul(m_a, m_b)
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Test 1: String as second matrix
test_case("String as second matrix",
          [[5, 6], [7, 8]], "Holberton")

# Test 2: Empty inner list in first matrix
test_case("Empty inner list in first matrix",
          [[]], [[5, 6], [7, 8]])

# Test 3: Empty inner list in second matrix
test_case("Empty inner list in second matrix",
          [[5, 6], [7, 8]], [[]])

# Test 4: String in first matrix
test_case("String in first matrix",
          [[5, "6"], [7, 8]], [[5, 6], [7, 8]])

# Test 5: String in second matrix
test_case("String in second matrix",
          [[5, 6], [7, 8]], [[5, "6"], [7, 8]])

# Test 6: Incompatible shapes (different row sizes in first matrix)
test_case("Incompatible shapes (different row sizes)",
          [[5, 6, 10], [7, 8]], [[5, 6], [7, 8]])

# Test 7: Incompatible shapes (different row sizes in second matrix)
test_case("Incompatible shapes (different row sizes)",
          [[5, 6], [7, 8]], [[5, 6, 1], [7, 8]]) 