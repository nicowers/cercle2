if __name__ == "__main__":
    file = "new_discovery.txt"
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    try:
        f = open(file, "w")
        print(f"Initializing new storage unit: {file}")
        print("Storage unit created successfully...")
        print("\nInscribing preservation data...")
        f.write("[ENTRY 001] New quantum algorithm discovered\n")
        f.write("[ENTRY 002] Efficiency increased by 347%\n")
        f.write("[ENTRY 003] Archived by Data Archivist trainee")
        f = open(file)
        content = f.read()
        print(content)
        print("\nData inscription complete. Storage unit sealed.")
        print(f"Archive {file} ready for long-term preservation.")
    except FileNotFoundError:
        print(f"{file} file does not exist.")
    finally:
        f.close()
