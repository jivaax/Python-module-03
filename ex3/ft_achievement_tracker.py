import random

LIST_OF_ACHIEVEMENTS = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Speed Runner",
    "Survivor",
    "Sharp Mind",
    "Treasure Hunter",
    "First Steps",
    "Unstoppable"
]


def gen_player_achievements() -> set[str]:

    number_of_achievements = random.randint(len(LIST_OF_ACHIEVEMENTS) // 2,
                                            len(LIST_OF_ACHIEVEMENTS) * 2 // 3)
    achievements = random.sample(LIST_OF_ACHIEVEMENTS, number_of_achievements)

    return set(achievements)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
    all_achievements = set(LIST_OF_ACHIEVEMENTS)
    alice = gen_player_achievements()
    bob = gen_player_achievements()
    charlie = gen_player_achievements()
    dylan = gen_player_achievements()
    all_distinct_achievements = alice.union(bob).union(charlie).union(dylan)
    common_achievements = alice.intersection(bob, charlie, dylan)
    only_alice_achievements = alice.difference(bob, charlie, dylan)
    only_bob_achievements = bob.difference(alice, charlie, dylan)
    only_charlie_achievements = charlie.difference(alice, bob, dylan)
    only_dylan_achievements = dylan.difference(alice, bob, charlie)
    alice_missing_achievements = all_achievements.difference(alice)
    bob_missing_achievements = all_achievements.difference(bob)
    charlie_missing_achievements = all_achievements.difference(charlie)
    dylan_missing_achievements = all_achievements.difference(dylan)

    print(f"Player Alice: {alice}")
    print(f"Player Bob: {bob}")
    print(f"Player Charlie: {charlie}")
    print(f"Player Dylan: {dylan}")
    print(f"\nAll distinct achievements: {all_distinct_achievements}")
    print(f"\nCommon achievements: {common_achievements}")
    print(f"\nOnly Alice has: {only_alice_achievements}")
    print(f"Only Bob has: {only_bob_achievements}")
    print(f"Only Charlie has: {only_charlie_achievements}")
    print(f"Only Dylan has: {only_dylan_achievements}")
    print(f"\nAlice is missing: {alice_missing_achievements}")
    print(f"Bob is missing: {bob_missing_achievements}")
    print(f"Charlie is missing: {charlie_missing_achievements}")
    print(f"Dylan is missing: {dylan_missing_achievements}")
