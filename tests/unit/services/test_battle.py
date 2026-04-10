import pytest
from unittest.mock import patch, mock_open, MagicMock
from app.services.battle_service import quem_ganha, batalha

# ========================
# CENÁRIOS DE FLUXO NORMAL
# ========================
def test_quem_ganha_vitoria_jogador_1():
    """Testa se a lógica de fraqueza reconhece vitória do move 1"""
    assert quem_ganha("agua", "fogo") == 1  # Fogo tem fraqueza contra água

def test_quem_ganha_vitoria_jogador_2():
    """Testa se a lógica de fraqueza reconhece vitória do move 2"""
    assert quem_ganha("fogo", "agua") == 2

def test_quem_ganha_empate():
    """Testa se golpes sem fraqueza direta entre si ou iguais dão empate"""
    assert quem_ganha("pedra", "pedra") == 0

def test_batalha_fluxo_normal(jogador_registrado_com_deck, jogador_adversario):
    """Testa a ocorrência de uma batalha inteira"""
    resultado = batalha(jogador_registrado_com_deck, jogador_adversario)
    
    #Verifica o vencedor correto
    assert "Gary Oak vence a batalha!" in resultado
    
    #Verifica as rodadas com os nomes e pokemons exatos que saíram no console
    assert "Brook (Geodude, pedra) vence Gary Oak (Bulbasaur, tesoura)" in resultado
    assert "Gary Oak (Squirtle, agua) vence Brook (Pikachu, corda)" in resultado
    assert "Gary Oak (Charmander, fogo) vence Brook (Mew, papel)" in resultado

# ====================
# CENÁRIOS DE EXTENSÃO
# ====================
def test_batalha_tipo_invalido(jogador_registrado_com_deck):
    """Tenta iniciar batalha com tipo inválido"""
    with pytest.raises(TypeError, match="batalha exige dois objetos Jogador"):
        batalha(jogador_registrado_com_deck, "Faker")

def test_batalha_jogador_nao_registrado(jogador_registrado_com_deck, jogador_limpo):
    """Tenta lutar com alguém não registrado"""
    with pytest.raises(ValueError, match="devem estar registrados"):
        batalha(jogador_registrado_com_deck, jogador_limpo)

def test_batalha_sem_deck(jogador_registrado_com_deck, jogador_registrado_sem_deck):
    """Tenta lutar contra alguém que não possui um deck"""
    with pytest.raises(ValueError, match="pelo menos três pokemons no deck"):
        batalha(jogador_registrado_com_deck, jogador_registrado_sem_deck)