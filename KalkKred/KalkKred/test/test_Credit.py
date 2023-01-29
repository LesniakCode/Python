import pytest

from ..credit import Credit

@pytest.fixture
def credit(tmpdir):
    "Provides something"
    return Credit("Pekao", 115000, 10, 0.11)

def test_newCreditAdd(credit):
    """Check initialization"""
    assert(credit.name, 0)
    assert(credit.intrests , 0)
    assert(credit.time, 0)
    assert(credit.overall, 0)

def test_calculationOfMonth(credit):
    value = credit._calcMonth()
    assert(value,0)