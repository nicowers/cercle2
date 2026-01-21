#!/usr/bin/env python3
import sys
import math

def euclidean_distance_formula(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return round(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 2)

def parse_arguments(arg):
    args = arg.split(",")

    if len(args) != 3:
        raise ValueError("Please enter 1 string, in the following format: \"x,y,z\"")
    else:
        try:
            x = int(args[0])
            y = int(args[1])
            z = int(args[2])
            return (x, y, z)
        except ValueError:
            raise ValueError("Please enter 1 string, in the following format: \"x,y,z\"")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        origin = (0, 0, 0)
        p1 = (0, 10, 0)
        p2 = (20, 0, 5)
        p3 = (10, 20, 5)
        value = euclidean_distance_formula(origin, p3)
        print("=== Game Coordinate System ===\n")
        print(f"Position created: {p3}")
        print(f"Distance between {origin} and {p3}: {value}\n")
        print("Please enter 1 string, please input in the following format: \"x,y,z\"")
        sys.exit(1)
    try:
        origin = (0, 0, 0)
        p1 = (0, 10, 0)
        p2 = (20, 0, 5)
        p3 = (10, 20, 5)
        value = euclidean_distance_formula(origin, p3)
        print("=== Game Coordinate System ===\n")
        print(f"Position created: {p3}")
        print(f"Distance between {origin} and {p3}: {value}\n")
        for i in range(1, len(sys.argv)):
            position = parse_arguments(sys.argv[i])
            x, y, z = position
            parse_arguments(sys.argv[i])
            print(f"Parsing coordinates: \"{sys.argv[i]}\"")
            print(f"Parsed position: {position}")
            print(f"Distance between {origin} and {position}: {euclidean_distance_formula(origin, position)}\n")
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{sys.argv[i]}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")
    finally:
        print("Unpacking demonstration:")
        print(f"Player at x={x}, y={y}, z={z}")
        print(f"Coordinates: X={x}, Y={y}, Z={z}")