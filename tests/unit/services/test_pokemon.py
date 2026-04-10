# tests/unit/services/test_pokemon.py
import pytest
from unittest.mock import patch, mock_open, MagicMock
from app.services.pokemon_service import get_all_pokemons

@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 1, "original_name": "Bulbasaur", "name": "Bulbasaur", "move": "tesoura", "description": "Seed"}]')
def test_get_all_pokemons_sucesso(mock_file):
    """11. Testa leitura do arquivo de pokemons com sucesso"""
    pokemons = get_all_pokemons()
    assert len(pokemons) == 1
    assert pokemons[0].name == "Bulbasaur"

@patch("builtins.open", side_effect=FileNotFoundError)
def test_get_all_pokemons_arquivo_nao_encontrado(mock_file):
    """12. Garante que se o json não existir, retorna lista vazia (conforme sua implementação)"""
    pokemons = get_all_pokemons()
    assert pokemons == []