from d_peak import find_2d_peak


def test_find_2d_peak():
    # GIVEN

    a = [
        [1, 0],
        [7, 3],
    ]
    a_peak_expected = [1, 0]

    b = [
        [1, 5, 3],
        [10, 2, 4],
        [7, 8, 2],
    ]
    b_peak_expected = [2, 1]

    c = [
        [1, 5, 3, 0, 13],
        [10, 2, 4, 3, 1],
        [7, 8, 2, 6, 7],
        [22, 2, 5, 12, 17],
        [20, 4, 1, 2, 1],
    ]
    c_peak_expected = [3, 4]

    # WHEN

    a_result = find_2d_peak(a)
    b_result = find_2d_peak(b)
    c_result = find_2d_peak(c)

    # THEN

    assert a_result == a_peak_expected
    assert b_result == b_peak_expected
    assert c_result == c_peak_expected
