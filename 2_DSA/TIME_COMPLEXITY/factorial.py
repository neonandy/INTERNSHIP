from itertools import permutations

def find_all_routes(cities: list):
    # Generate every possible ordering of cities
    # 3 cities → 6 routes
    # 5 cities → 120 routes
    # 10 cities → 3,628,800 routes 💀
    all_possible_routes = list(permutations(cities))    # n! arrangements

    # Check every route — this is brute force Travelling Salesman
    for route in all_possible_routes:                   # Loops n! times
        print(route)                                    # Each route is one arrangement

def generate_permutations(items: list) -> list:
    # Manual recursive version to show WHY it's n!
    if len(items) <= 1:
        return [items]                      # Base case — only one arrangement

    all_arrangements = []

    for i, current_item in enumerate(items):            # Pick each item as first
        remaining_items = items[:i] + items[i+1:]       # Everything except current

        # Recursively get all arrangements of remaining
        # Each level multiplies arrangements by current length
        for sub_arrangement in generate_permutations(remaining_items):
            all_arrangements.append([current_item] + sub_arrangement)

    return all_arrangements

cities = ["Bengaluru", "Mumbai", "Delhi"]
find_all_routes(cities)
# ('Bengaluru', 'Mumbai', 'Delhi')
# ('Bengaluru', 'Delhi', 'Mumbai')
# ('Mumbai', 'Bengaluru', 'Delhi')
# ('Mumbai', 'Delhi', 'Bengaluru')
# ('Delhi', 'Bengaluru', 'Mumbai')
# ('Delhi', 'Mumbai', 'Bengaluru')
# → 3! = 6 total routes



### Complete Growth at a Glance

n = 5:

O(1)      →           1 operation   ✅ Instant
O(log n)  →           2 operations  ✅ Instant
O(n)      →           5 operations  ✅ Fast
O(n log n)→          10 operations  🟡 Fast
O(n²)     →          25 operations  🟠 Okay
O(2ⁿ)     →          32 operations  🔴 Slow
O(n!)     →         120 operations  💀 Avoid