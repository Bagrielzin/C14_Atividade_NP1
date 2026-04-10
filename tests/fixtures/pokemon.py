# tests/fixtures/pokemon.py
import pytest
from app.schemas.pokemon import Pokemon

@pytest.fixture
def pokemons_mock():
    return [
        Pokemon(id=1, original_name="Bulbasaur", name="Bulbasaur", move="tesoura", description="..."),
        Pokemon(id=2, original_name="Squirtle", name="Squirtle", move="agua", description="..."),
        Pokemon(id=3, original_name="Charmander", name="Charmander", move="fogo", description="..."),
        Pokemon(id=4, original_name="Geodude", name="Geodude", move="pedra", description="..."),
        Pokemon(id=5, original_name="Pikachu", name="Pikachu", move="corda", description="..."),
        Pokemon(id=6, original_name="Mew", name="Mew", move="papel", description="..."),
        Pokemon(id=7, original_name="Snorlax", name="Snorlax", move="pedra", description="...")
    ]

@pytest.fixture
def tesoura_pokemon():
    return Pokemon(
        id=6,
        original_name="Charizard",
        name="Charizard",
        move="tesoura",
        description="Spits fire that is hot enough to melt boulders. Known to cause forest fires unintentionally."
    )

@pytest.fixture
def fogo_pokemon():
    return Pokemon(
        id=25,
        original_name="Pikachu",
        name="Pikachu",
        move="fogo",
        description="When several of these Pokémon gather, their electricity could build and cause lightning storms."
    )

@pytest.fixture
def agua_pokemon():
    return Pokemon(
        id=150,
        original_name="Mewtwo",
        name="Mewtwo",
        move="agua",
        description="It was created by a scientist after years of horrific gene splicing and DNA engineering experiments."
    )

@pytest.fixture
def pedra_pokemon():
    return Pokemon(
        id=2,
        original_name="Ivysaur",
        name="Ivysaur",
        move="pedra",
        description="When the bulb on its back grows large, it appears to lose the ability to stand on its hind legs."
    )

@pytest.fixture
def papel_pokemon():
    return Pokemon(
        id=228,
        original_name="Houndour",
        name="Houndour",
        move="papel",
        description="It hunts in packs. It communicates with its pack using howls."
    )

@pytest.fixture
def corda_pokemon():
    return Pokemon(
        id=236,
        original_name="Tyrogue",
        name="Tyrogue",
        move="corda"
    )

@pytest.fixture
def valid_pokemon_list(tesoura_pokemon, fogo_pokemon, agua_pokemon, pedra_pokemon, papel_pokemon, corda_pokemon):
    """Retorna uma lista com exatamente 3 pokemons válidos."""
    return [
        Pokemon(pokemon=tesoura_pokemon),
        Pokemon(pokemon=fogo_pokemon),
        Pokemon(pokemon=agua_pokemon),
        Pokemon(pokemon=pedra_pokemon),
        Pokemon(pokemon=papel_pokemon),
        Pokemon(pokemon=corda_pokemon)
    ]