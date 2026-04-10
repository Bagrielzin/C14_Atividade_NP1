from app.schemas.jogador import Jogador
from app.services.player_service import *
from app.services.battle_service import batalha
from app.services.pokemon_service import get_all_pokemons

ash = Jogador(nome="Ash Ketchum")
gary = Jogador(nome="Gary Oak")

registra_jogador(ash)
montar_deck(ash)

registra_jogador(gary)
montar_deck(gary)

print(batalha(ash, gary))