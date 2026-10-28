import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        print("Enter new coordinates as floats in format 'x,y,z': ", end="")
        coords_input = input()
        coords = coords_input.split(",")
        converted_coords = []
        valid = True

        if len(coords) != 3:
            print("Invalid syntax")
            continue
        for coord in coords:
            try:
                converted_coords.append(float(coord))
            except ValueError as e:
                print(f"Error on parameter '{coord}': {e}")
                valid = False
                break
        if not valid:
            continue
        x, y, z = converted_coords
        return x, y, z


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    x1, y1, z1 = get_player_pos()
    print(f"Got a first tuple: ({x1}, {y1}, {z1})")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    print(f"Distance to center: {math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2):.4f}")

    print("\nGet a second set of coordinates")
    x2, y2, z2 = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2):.4f}")
