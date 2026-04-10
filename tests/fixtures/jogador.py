import pytest
from app.schemas.jogador import Jogador

@pytest.fixture
def jogador_limpo():
    return Jogador(nome="Ash Ketchum")

@pytest.fixture
def jogador_registrado_com_deck(pokemons_mock):
    j = Jogador(nome="Gary Oak")
    j.registro = True
    j.colecao = pokemons_mock[:6]
    j.deck = pokemons_mock[:3]
    return j

@pytest.fixture
def jogador_registrado_sem_deck(pokemons_mock):
    j = Jogador(nome="Misty")
    j.registro = True
    j.colecao = pokemons_mock[:6]
    j.deck = []
    return j

@pytest.fixture
def jogador_adversario(pokemons_mock):
    j = Jogador(nome="Brook")
    j.registro = True
    j.colecao = pokemons_mock[:6]
    j.deck = [pokemons_mock[3], pokemons_mock[4], pokemons_mock[5]] # pedra, corda, papel
    return j
 