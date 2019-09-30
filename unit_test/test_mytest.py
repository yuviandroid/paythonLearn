import unit_test.addition_a as st


def test_calc_add():
    total = st.calc_add(5,6)
    assert total == 11