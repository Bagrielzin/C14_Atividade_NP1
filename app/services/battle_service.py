from app.schemas.jogador import Jogador
from app.utils.constants import FRAQUEZAS

def quem_ganha(move1: str, move2: str) -> int:
    """Retorna 1 para move1, 2 para move2, 0 para empate."""
    if move2 in FRAQUEZAS.get(move1, []):
        return 2
    elif move1 in FRAQUEZAS.get(move2, []):
        return 1
    return 0

def batalha(jogador1: Jogador, jogador2: Jogador) -> str:
    """Realiza uma batalha entre dois jogadores usando seus decks."""
    if not isinstance(jogador1, Jogador) or not isinstance(jogador2, Jogador):
        raise TypeError("batalha exige dois objetos Jogador.")
    
    if not jogador1.registro or not jogador2.registro:
        raise ValueError("Ambos os jogadores devem estar registrados.")
    
    if not jogador1.deck or not jogador2.deck:
        raise ValueError("Ambos os jogadores devem ter pelo menos três pokemons no deck.")
    
    vitorias_j1 = 0
    vitorias_j2 = 0
    rodadas = []
    
    for i in range(3):
        if vitorias_j1 == 2 or vitorias_j2 == 2:
            break
        else:
            p1 = jogador1.deck[i]
            p2 = jogador2.deck[i]
            resultado = quem_ganha(p1.move, p2.move)
            if resultado == 1:
                vitorias_j1 += 1
                rodadas.append("==============================================")
                rodadas.append(f"Rodada {i+1}: {jogador1.nome} ({p1.name}, {p1.move}) vence {jogador2.nome} ({p2.name}, {p2.move})")
            elif resultado == 2:
                vitorias_j2 += 1
                rodadas.append("==============================================")
                rodadas.append(f"Rodada {i+1}: {jogador2.nome} ({p2.name}, {p2.move}) vence {jogador1.nome} ({p1.name}, {p1.move})")
            else:
                rodadas.append("==============================================")
                rodadas.append(f"Rodada {i+1}: Empate entre ({p1.name}, {p1.move}) e ({p2.name}, {p2.move})")
    
    # Resultado final
    if vitorias_j1 > vitorias_j2:
        vencedor = f"{jogador1.nome} vence a batalha!"
    elif vitorias_j2 > vitorias_j1:
        vencedor = f"{jogador2.nome} vence a batalha!"
    else:
        vencedor = "Batalha empatada!"

    rodadas.append("==============================================")
    
    # Montar string de resultado
    resultado = "\n".join(rodadas) + f"\n{vencedor}"
    return resultado