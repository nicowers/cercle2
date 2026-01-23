#!/usr/bin/env python3
import time

def event(nbr_event):
    players = ("alice", "bob", "charlie", "david", "ethann", "faustin")
    events = ("killed monster",
            "found treasure",
            "leveled up",
            "killed monster",
            "killed monster",
            "killed monster",
            "killed monster",
            "killed monster",
            "leveled up",
            "killed monster",
            "killed monster",
            "killed monster",
            "killed monster"
            )
    player_lvl = [5, 12, 8, 7, 3, 1]
    for i in range(nbr_event):
        index = (i % len(players))
        event_index = (i % len(events))
        if events[event_index]== "leveled up":
            player_lvl[index] += 1
        yield {
            "id" : i + 1,
            "player_level" : player_lvl[index],
            "player" : players[index],
            "event" : events[event_index]
            }

def stream_analytics(nbr_event, display=3):
    high_level_players = treasure_events = level_up_events = 0
    print(f"\nProcessing {nbr_event} game events...\n")
    for i, events in enumerate(event(nbr_event)):
        if events["event"] == "found treasure":
            treasure_events += 1
        if events["player_level"] >= 10:
            high_level_players += 1
        if events["event"] == "leveled up":
            level_up_events += 1
        if i < display :
            print(f"Event {events['id']}: Player {events['player']} (level {events['player_level']}) killed monster")
    else:
        print("...")
    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {nbr_event}")
    print(f"High-level players (10+): {high_level_players}")
    print(f"Treasure events: {treasure_events}")
    print(f"Level-up events: {level_up_events}")
    print("\nMemory usage: Constant (streaming)")


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime(n):
    count = 0
    number = 2

    while count < n:
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
        if is_prime:
            yield number
            count += 1
        number += 1

if __name__ == "__main__":
    n = 1000
    print("=== Game Data Stream Processor ===")
    start = time.time()
    stream_analytics(n)
    end = time.time()
    print(f"Processing time: {end - start:.6f} seconds")
    print("\n=== Generator Demonstration ===")
    prime_len = 5
    prime_list = []
    prime_number = prime(10)
    for i in range(prime_len):
        prime_list.append(next(prime_number))
    prime_str = ", ".join(map(str, prime_list))
    fibo_list = []
    fibo_len = 10
    fib = fibonacci()
    for i in range(fibo_len):
        fibo_list.append(next(fib))
    fibo_str = ", ".join(map(str, fibo_list))
    print(f"Fibonacci sequence (first {fibo_len}): {fibo_str}")
    print(f"Prime numbers (first {prime_len}): {prime_str}")
