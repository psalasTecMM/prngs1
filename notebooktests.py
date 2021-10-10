from testbook import testbook


# import your python notebook before each function as
# @testbook('./alumno/[nombre_archivo].ipynb', execute=True)

def test_mid_square(tb):
    mid_square = tb.ref("mid_square")
    r1 = mid_square(3, 5735)
    assert r1 == [0.8902, 0.2456, 0.319]
    assert len(r1) == 3
    r2 = mid_square(3, 1000)
    assert r2 == [0.0, 0.0, 0.0]
    assert len(r2) == 3
    r3 = mid_square(3, 675248)
    assert r3 == [0.959861, 0.333139, 0.981593]
    assert len(r3) == 3


def test_mid_product(tb):
    mid_product = tb.ref("mid_product")
    r1 = mid_product(3, 5015, 5734)
    assert r1 == [0.756, 0.349, 0.3844]
    assert len(r1) == 3


def test_constant_multiplier(tb):
    constant_multiplier = tb.ref("constant_multiplier")
    r1 = constant_multiplier(3, 6965, 9803)
    assert r1 == [0.2778, 0.3487, 0.2869]
    assert len(r1) == 3


def test_get_middle_number(tb):
    get_middle_numbers = tb.ref("get_middle_numbers")
    assert get_middle_numbers(4, 30976) == 3097
    assert get_middle_numbers(4, 6031936) == 319
    assert get_middle_numbers(4, 28756010) == 7560
