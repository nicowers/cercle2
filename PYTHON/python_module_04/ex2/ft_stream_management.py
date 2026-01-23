import sys

if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
    print("Input Stream active. Enter archivist ID: ", end="")
    sys.stdout.flush()
    name = sys.stdin.readline().split("\n")[0]
    print("Input Stream active. Enter status report: ", end="")
    sys.stdout.flush()
    status = sys.stdin.readline().split("\n")[0]
    sys.stdout.write(f"\n[STANDARD] Archive status from {name}: {status}\n")
    sys.stderr.write("[ALERT] System diagnostic: Communication channels verified\n")
    sys.stdout.write("[STANDARD] Data transmission complete\n")
    print("\nThree-channel communication test successful.")