#O(1) — Constant Time


def get_first_element(items: list):
    # No loop, no searching — direct access by index
    # Doesn't matter if list has 5 items or 5 million
    # Always exactly 1 operation
    return items[0]

def dictionary_lookup(person: dict):
    # Dictionary uses hashing internally
    # Key maps directly to value — no searching needed
    # Always 1 step regardless of dictionary size
    return person["name"]

numbers = [10, 20, 30, 40, 50]
info = {"name": "Nandan", "age": 20}

print(get_first_element(numbers))   # 10  → 1 step
print(dictionary_lookup(info))      # Nandan → 1 step