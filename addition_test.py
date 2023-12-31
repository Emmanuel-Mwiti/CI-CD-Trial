from add_two_numbers import add_numbers

def test_addition():
    result = add_numbers(5, 3)
    assert result == 8, "Test case 1 failed"

    result = add_numbers(-2, -7)
    assert result == -9, "Test case 2 failed"

    result = add_numbers(10, -4)
    assert result == 6, "Test case 3 failed"

    result = add_numbers(3.5, 1.5)
    assert result == 5.0, "Test case 4 failed"

if __name__ == "__main":
    test_addition()
    print("All tests passed.")
