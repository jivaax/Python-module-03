import sys

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    inventory: dict[str, int] = {}
    for arg in sys.argv[1:]:
        parts = arg.split(":")
        if len(parts) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        item, quantity = parts
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            quantity_int = int(quantity)
        except ValueError as e:
            print(f"Quantity error for '{item}': {e}")
            continue
        inventory[item] = quantity_int

    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")

    highest_quantity = None
    most_abundant_item = None
    lowest_quantity = None
    least_abundant_item = None

    for item, item_quantity in inventory.items():
        print(f"Item {item} represents "
              f"{(item_quantity / total if total != 0 else 0):.1%}")

        if highest_quantity is None or item_quantity > highest_quantity:
            highest_quantity = item_quantity
            most_abundant_item = item

        if lowest_quantity is None or item_quantity < lowest_quantity:
            lowest_quantity = item_quantity
            least_abundant_item = item

    if inventory:
        print(f"Item most abundant: {most_abundant_item} "
              f"with quantity {highest_quantity}")
        print(f"Item least abundant: {least_abundant_item} "
              f"with quantity {lowest_quantity}")
    else:
        print("Inventory is empty - no items to compare")
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")
