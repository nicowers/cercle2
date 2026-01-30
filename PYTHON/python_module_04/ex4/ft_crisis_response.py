if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")
    files = {"file1": "lost_archive.txt",
             "file2": "classified_vault.txt",
             "file3": "standard_archive.txt"}
    for file in files:
        try:
            with open(files[file]) as f:
                f.read()
                print("ROUTINE ACCESS: ", end="")
                print(f"Attempting access to '{files[file]}'...")
                print("SUCCESS: Archive recovered - ")
                print("``Knowledge preserved for humanity''")
                print("STATUS: Normal operations resumed")
        except FileNotFoundError:
            print(f"CRISIS ALERT: Attempting access to '{files[file]}'...")
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable\n")
        except PermissionError:
            print(f"CRISIS ALERT: Attempting access to '{files[file]}'...")
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained\n")
        except Exception:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
    print("\nAll crisis scenarios handled successfully. Archives secure.")
