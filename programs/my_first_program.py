from nada_dsl import *

def nada_main():
    hackerone = Party(name="HackerOne")  # party 0
    hackertwo = Party(name="HackerTwo")  # party 1

    hackerone_dj_skills = SecretInteger(Input(name="hackerone_dj_skills", party=hackerone))
    hackertwo_dj_skills = SecretInteger(Input(name="hackertwo_dj_skills", party=hackertwo))
    hackerone_spice_tolerance = SecretInteger(Input(name="hackerone_spice_tolerance", party=hackerone))
    hackertwo_spice_tolerance = SecretInteger(Input(name="hackertwo_spice_tolerance", party=hackertwo))

    # Determine who has better DJ skills
    dj_battle_result = (
        (hackerone_dj_skills > hackertwo_dj_skills).if_else(
            Integer(0),  # HackerOne wins the DJ battle
            Integer(1)   # HackerTwo wins the DJ battle
        )
    )

    # Determine who has better spice tolerance
    spice_battle_result = (
        (hackerone_spice_tolerance > hackertwo_spice_tolerance).if_else(
            Integer(0),  # HackerOne wins the spice battle
            Integer(1)   # HackerTwo wins the spice battle
        )
    )

    # Determine the overall winner based on DJ skills and spice tolerance
    overall_winner = (
        (dj_battle_result == spice_battle_result).if_else(
            dj_battle_result,  # If they match, that's the overall winner
            Integer(2)         # Otherwise, it's a tie
        )
    )

    out = Output(overall_winner, "overall_winner", hackerone)

    return [out]

