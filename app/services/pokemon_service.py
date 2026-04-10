import json
from pathlib import Path
from app.schemas.pokemon import Pokemon

POKEMONS_FILE = Path(__file__).parent.parent / "data" / "pokemon.json"

def get_all_pokemons() -> list[Pokemon]:
    """Carrega os pokemons do arquivo JSON e retorna objetos Pokemon."""
    try:
        with open(POKEMONS_FILE, encoding="utf-8") as f:
            data = json.load(f)
        return [Pokemon(**p) for p in data]
    except FileNotFoundError:
        return []