# Importerar funktionerna för kalkylatorn
import calculator


# Denna testmetod kontrollera att additionsmetoden fungerar som den ska.
def test_add_method():
    assert 1 == calculator.addition(0, 1)
    assert 1 == calculator.addition(1, 0)
    assert 2 == calculator.addition(0, 2)


# Denna metod kontrollerar att subtraktionsmetoden fungerar som den ska.
def test_subtract_method():
    assert -1 == calculator.subtract(0, 1)
    assert -2 == calculator.subtract(0, 2)
    assert 1 == calculator.subtract(1, 0)


# Denna testmetod kontrollera att multiplikationssmetoden fungerar som den ska.
def test_multiply_method():
    assert 0 == calculator.multiply(0, 1)
    assert 1 == calculator.multiply(1, 1)
    assert 4 == calculator.multiply(2, 2)


# Denna metod kontrollerar att subtraktionsmetoden fungerar som den ska.
def test_divide_method():
    assert 0 == calculator.divide(1, 0)
    assert 1 == calculator.divide(2, 2)
    assert 4 == calculator.divide(8, 2)
