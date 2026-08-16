import pytest

from src.module import foo


def test_foo_1():
    assert foo(1,2) == 3
    assert foo(0,0) == 0


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (-1, -2, -3),
        (-5, 5, 0),
        (2**62, 2**62, 2**63),
    ],
)
def test_foo_integers(a, b, expected):
    assert foo(a, b) == expected


def test_foo_floats():
    assert foo(1.5, 2.25) == pytest.approx(3.75)
    assert foo(1, 0.5) == pytest.approx(1.5)


def test_foo_is_commutative():
    assert foo(3, 7) == foo(7, 3)


def test_foo_concatenates_sequences():
    assert foo("ab", "cd") == "abcd"
    assert foo([1], [2, 3]) == [1, 2, 3]
    assert foo((1,), (2,)) == (1, 2)


def test_foo_does_not_mutate_list_arguments():
    a = [1]
    b = [2]
    foo(a, b)
    assert a == [1]
    assert b == [2]


def test_foo_rejects_mismatched_types():
    with pytest.raises(TypeError):
        foo(1, "a")
    with pytest.raises(TypeError):
        foo(None, None)
