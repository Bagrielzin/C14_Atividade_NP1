import random
from schemas.jogador import Jogador
from services.pokemon_service import get_all_pokemons

def registra_jogador(jogador: Jogador, pokemon_ids: list = None) -> Jogador:
    """Registra um jogador e adiciona 6 pokemons na coleção."""
    if not isinstance(jogador, Jogador):
        raise TypeError("registra_jogador exige um objeto Jogador.")

    if jogador.registro:
        raise ValueError(f"Jogador '{jogador.nome}' já está registrado.")

    todas = get_all_pokemons()
    mapa_todas = {p.id: p for p in todas}

    if pokemon_ids is None:
        selecionados = random.sample(todas, min(6, len(todas)))
    else:
        if not isinstance(pokemon_ids, list):
            raise TypeError("pokemon_ids deve ser uma lista de IDs.")
        if len(pokemon_ids) != 6:
            raise ValueError("pokemon_ids deve conter exatamente 6 IDs.")
        selecionados = []
        for pid in pokemon_ids:
            if not isinstance(pid, int):
                raise TypeError("IDs na lista devem ser inteiros.")
            if pid not in mapa_todas:
                raise ValueError(f"ID de pokemon {pid} não existe.")
            selecionados.append(mapa_todas[pid])

    jogador.colecao.extend(selecionados)
    jogador.registro = True
    print(f"Jogador '{jogador.nome}' registrado com sucesso! 6 pokemons aleatórios adicionados à coleção.")

    return jogador

def get_jogador_info(jogador: Jogador) -> dict:
    """Retorna as informações do jogador em formato de dicionário."""
    if not isinstance(jogador, Jogador):
        raise TypeError("get_jogador_info exige um objeto Jogador.")

    if not jogador.registro:
        raise ValueError(f"Jogador '{jogador.nome}' não está registrado.")

    info = []
    info.append(f"Jogador: {jogador.nome}")
    info.append(f"Deck ({len(jogador.deck)} pokemons):")
    for p in jogador.deck:
        info.append(f"  - {p.id} | {p.name} ({p.move})")
    info.append(f"Coleção ({len(jogador.colecao)} pokemons):")
    for p in jogador.colecao:
        info.append(f"  - {p.id} | {p.name} ({p.move})")

    return "\n".join(info)


def delete_jogador(jogador: Jogador) -> None:
    """Deleta um jogador e todas as suas informações (deck e coleção)."""
    if not isinstance(jogador, Jogador):
        raise TypeError("delete_jogador exige um objeto Jogador.")

    if not jogador.registro:
        raise ValueError(f"Jogador '{jogador.nome}' não está registrado. Apenas jogadores registrados podem ser deletados.")

    jogador.deck.clear()
    jogador.colecao.clear()
    jogador.nome = ""
    jogador.registro = False
    print("Jogador deletado com sucesso. Todas as informações foram removidas.")