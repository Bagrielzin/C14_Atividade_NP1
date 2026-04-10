# tests/unit/services/test_jogador.py
import pytest
from unittest.mock import patch, mock_open, MagicMock
from app.services.player_service import *
from app.schemas.jogador import Jogador


# ========================
# CENÁRIOS DE FLUXO NORMAL
# ========================
@patch("app.services.player_service.get_all_pokemons")
def test_registra_jogador_aleatorio(mock_get_all, jogador_limpo, pokemons_mock):
    """Testa registrar jogador sem IDs passados (escolhe aleatório)"""
    mock_get_all.return_value = pokemons_mock
    jogador = registra_jogador(jogador_limpo)
    
    assert jogador.registro is True
    assert len(jogador.colecao) == 6

@patch("app.services.player_service.get_all_pokemons")
def test_registra_jogador_ids_especificos(mock_get_all, jogador_limpo, pokemons_mock):
    """Testa registrar jogador passando IDs exatos"""
    mock_get_all.return_value = pokemons_mock
    ids = [1, 2, 3, 4, 5, 6]
    jogador = registra_jogador(jogador_limpo, pokemon_ids=ids)
    
    assert jogador.registro is True
    assert [p.id for p in jogador.colecao] == ids

def test_get_jogador_info(jogador_registrado_com_deck):
    """Testa se a informação do jogador retorna no formato correto"""
    info = get_jogador_info(jogador_registrado_com_deck)
    assert "Jogador: Gary Oak" in info
    assert "Deck (3 pokemons):" in info
    assert "Coleção (6 pokemons):" in info

def test_delete_jogador_sem_deck(jogador_registrado_sem_deck):
    """Testa se deletar o jogador sem deck limpa todos os dados"""
    delete_jogador(jogador_registrado_sem_deck)
    assert jogador_registrado_sem_deck.registro is False
    assert jogador_registrado_sem_deck.nome == ""
    assert len(jogador_registrado_sem_deck.deck) == 0
    assert len(jogador_registrado_sem_deck.colecao) == 0

def test_delete_jogador_com_deck(jogador_registrado_com_deck):
    """Testa se deletar o jogador com deck limpa todos os dados"""
    delete_jogador(jogador_registrado_com_deck)
    assert jogador_registrado_com_deck.registro is False
    assert jogador_registrado_com_deck.nome == ""
    assert len(jogador_registrado_com_deck.deck) == 0
    assert len(jogador_registrado_com_deck.colecao) == 0

def test_montar_deck_ids_informados(jogador_registrado_sem_deck):
    """Testa montar deck passando os IDs como parâmetro"""
    ids_desejados = [4, 5, 6]
    jogador = montar_deck(jogador_registrado_sem_deck, pokemon_ids=ids_desejados)
    assert len(jogador.deck) == 3
    assert [p.id for p in jogador.deck] == ids_desejados

@patch('builtins.input', return_value="1, 2, 3")
def test_montar_deck_via_input(mock_input, jogador_registrado_sem_deck):
    """Testa montar deck via digitação do usuário (input mockado)"""
    jogador = montar_deck(jogador_registrado_sem_deck, pokemon_ids=None)
    assert len(jogador.deck) == 3
    assert [p.id for p in jogador.deck] == [1, 2, 3]

# ====================
# CENÁRIOS DE EXTENSÃO
# ====================
def test_registra_jogador_tipo_invalido():
    """Tenta registrar passando algo que não é um Jogador"""
    with pytest.raises(TypeError, match="registra_jogador exige um objeto Jogador"):
        registra_jogador("Faker")

def test_registra_jogador_ja_registrado(jogador_registrado_sem_deck):
    """Tenta registrar um jogador que já possui registro"""
    with pytest.raises(ValueError, match="já está registrado"):
        registra_jogador(jogador_registrado_sem_deck)

@patch("app.services.pokemon_service.get_all_pokemons")
def test_registra_jogador_ids_nao_lista(mock_get_all, jogador_limpo, pokemons_mock):
    """Tenta registrar passando pokemon_ids com tipo incorreto (string)"""
    mock_get_all.return_value = pokemons_mock
    with pytest.raises(TypeError, match="pokemon_ids deve ser uma lista"):
        registra_jogador(jogador_limpo, pokemon_ids="1, 2, 3, 4, 5, 6")

@patch("app.services.pokemon_service.get_all_pokemons")
def test_registra_jogador_quantidade_ids_errada(mock_get_all, jogador_limpo, pokemons_mock):
    """Tenta registrar com menos/mais de 6 IDs"""
    mock_get_all.return_value = pokemons_mock
    with pytest.raises(ValueError, match="exatamente 6 IDs"):
        registra_jogador(jogador_limpo, pokemon_ids=[1, 2, 3])

@patch("app.services.pokemon_service.get_all_pokemons")
def test_registra_jogador_id_nao_existente(mock_get_all, jogador_limpo, pokemons_mock):
    """Tenta registrar com um ID de pokemon que não existe no banco"""
    mock_get_all.return_value = pokemons_mock
    with pytest.raises(ValueError, match="não existe"):
        registra_jogador(jogador_limpo, pokemon_ids=[1, 2, 3, 4, 5, 999])

def test_get_jogador_info_nao_registrado(jogador_limpo):
    """Tenta obter info de um jogador sem registro"""
    with pytest.raises(ValueError, match="não está registrado"):
        get_jogador_info(jogador_limpo)

def test_get_jogador_tipo_invalido():
    """Tenta obter info de um jogador tipo inválido"""
    with pytest.raises(TypeError, match="get_jogador_info exige um objeto Jogador."):
        get_jogador_info("Faker")

def test_delete_jogador_nao_registrado(jogador_limpo):
    """Tenta deletar um jogador não registrado"""
    with pytest.raises(ValueError, match="não está registrado"):
        delete_jogador(jogador_limpo)

def test_delete_jogador_tipo_invalido():
    """Tenta deletar um jogador tipo inválido"""
    with pytest.raises(TypeError, match="delete_jogador exige um objeto Jogador."):
        delete_jogador("Faker")

def test_montar_deck_id_ausente_na_colecao(jogador_registrado_com_deck):
    """Tenta montar um deck com pokemons que ele não possui na coleção"""
    with pytest.raises(ValueError, match="não encontrado na coleção"):
        montar_deck(jogador_registrado_com_deck, pokemon_ids=[1, 2, 99])

@patch('builtins.input', side_effect=["a, b, c", "1, 2, 3"])
def test_montar_deck_input_invalido_depois_valido(mock_input, jogador_registrado_com_deck):
    """Testa a resiliência do input (usuário digita letras, o while pede de novo até digitar certo)"""
    # O mock_input vai soltar 'a, b, c' (gera except ValueError) e depois '1, 2, 3' (passa).
    jogador = montar_deck(jogador_registrado_com_deck, pokemon_ids=None)
    assert len(jogador.deck) == 3
    assert [p.id for p in jogador.deck] == [1, 2, 3]

def test_montar_deck_objeto_tipo_invalido():
    """Tenta montar um deck sem o objeto jogador que ele não possui na coleção"""
    with pytest.raises(TypeError, match="adicionar_ao_deck exige um objeto Jogador."):
        montar_deck("Faker", pokemon_ids=[1, 2, 99])

def test_montar_deck_jogador_limpo(jogador_limpo):
    """Tenta montar um deck jogador sem registro"""
    with pytest.raises(ValueError, match="Jogador 'Ash Ketchum' não está registrado."):
        montar_deck(jogador_limpo, pokemon_ids=[1, 2, 99])

def test_montar_deck_diferente_de_tres_ids(jogador_registrado_sem_deck):
    """Tenta montar deck com menos de três ids"""
    with pytest.raises(ValueError, match="pokemon_ids deve ser uma lista com exatamente 3 IDs."):
        montar_deck(jogador_registrado_sem_deck, pokemon_ids=[1, 2, 3, 4])