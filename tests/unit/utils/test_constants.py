from app.utils.constants import FRAQUEZAS

# ========================
# CENÁRIOS DE FLUXO NORMAL
# ========================
def test_fraquezas_pedra():
    assert "papel" in FRAQUEZAS["pedra"]
    assert "fogo" in FRAQUEZAS["pedra"]
    assert "corda" in FRAQUEZAS["pedra"]

def test_fraquezas_papel():
    assert "tesoura" in FRAQUEZAS["papel"]
    assert "agua" in FRAQUEZAS["papel"]
    assert "fogo" in FRAQUEZAS["papel"]

def test_fraquezas_tesoura():
    assert "pedra" in FRAQUEZAS["tesoura"]
    assert "agua" in FRAQUEZAS["tesoura"]
    assert "fogo" in FRAQUEZAS["tesoura"]

def test_fraquezas_corda():
    assert "tesoura" in FRAQUEZAS["corda"]
    assert "agua" in FRAQUEZAS["corda"]
    assert "fogo" in FRAQUEZAS["corda"]
    assert "papel" in FRAQUEZAS["corda"]

def test_fraquezas_agua():
    assert "pedra" in FRAQUEZAS["agua"]

def test_fraquezas_fogo():
    assert "agua" in FRAQUEZAS["fogo"]