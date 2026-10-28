import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    gamers = ["Alice", "Bob", "Charlie", "David"]
    actions = ["move", "run", "sleep", "grab", "swim", "release", "eat"]

    while True:
        gamer = random.choice(gamers)
        action = random.choice(actions)
        yield (gamer, action)


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while event_list:
        event = random.choice(event_list)
        event_list.remove(event)
        yield event


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    events = gen_event()
    for i in range(1000):
        print(f"Event {i}: {next(events)}")
    event_list = []
    for _ in range(10):
        event_list.append(next(events))
    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
