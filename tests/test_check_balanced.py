import pytest

from balancing_brackets import check_balanced


@pytest.mark.parametrize('brackets, expected', [
    ('(((([{}]))))', 'Сбалансированно'),
    ('[([])((([[[]]])))]{()}', 'Сбалансированно'),
    ('{{[()]}}', 'Сбалансированно'),
    ('}{}', 'Несбалансированно'),
    ('{{[(])]}}', 'Несбалансированно'),
    ('[[{())}]', 'Несбалансированно')
])
def test_main(brackets, expected):
    assert check_balanced(brackets) == expected
