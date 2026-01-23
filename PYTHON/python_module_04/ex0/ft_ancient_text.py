if __name__ == "__main__":
    file = "ancient_fragment.txt"
    try:
        print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
        f = open(file, "r")
        print(f"Accessing Storage Vault: {file}")
        print("Connection established...\n")
        print("RECOVERED DATA:")
        content = f.read()
        print(content)
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print(f"{file} file does not exist.")
    finally:
        f.close()