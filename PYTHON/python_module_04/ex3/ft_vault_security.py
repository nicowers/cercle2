if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    file1 = "classified_data.txt"
    file2 = "security_protocols.txt"
    try:
        with open(file1) as f:
            content = f.read()
        print("Initiating secure vault access...")
        print("Vault connection established with failsafe protocols")
        print("\nSECURE EXTRACTION:")
        print(content)
    except FileNotFoundError:
        print(f"{file1} file does not exist.")
    try:
        with open(file2) as f:
            content = f.read()
        print("\nSECURE PRESERVATION:")
        print(content)
        print("Vault automatically sealed upon completion")
        print("\nAll vault operations completed with maximum security.")
    except FileNotFoundError:
        print(f"{file2} file does not exist.")