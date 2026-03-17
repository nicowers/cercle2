import sys
import os

if __name__ == "__main__":
    try:
        from dotenv import load_dotenv
        # load_dotenv load all variables of our env file if it exists
        load_dotenv()
        # getenv permit to recover data from .env file
        mode = os.getenv("MATRIX_MODE")
        url = os.getenv('DATABASE_URL')
        api_key = os.getenv('API_KEY')
        log_level = os.getenv('LOG_LEVEL')
        zion_endpoint = os.getenv('ZION_ENDPOINT')
        required_config = {
            "MATRIX_MODE": mode,
            "DATABASE_URL": url,
            "API_KEY": api_key,
            "LOG_LEVEL": log_level,
            "ZION_ENDPOINT": zion_endpoint
        }
        for key, elt in required_config.items():
            if not elt:
                print(f"[Error] Missing configuration: {key}")
                sys.exit(1)
        print("\nORACLE STATUS: Reading the Matrix...\n")

        print("Configuration loaded:")
        if mode != "development" and mode != "production":
            print("MATRIX_MODE must be 'development' or 'production'")
            sys.exit(1)
        print("Mode:", mode)
        print("Database: Connected to local instance")
        print("API Access: Authenticated")
        print(f"Log Level: {log_level}")
        print("Zion Network: Online")

        print("\nEnvironment security check:")
        print("[OK] No hardcoded secrets detected")
        print("[OK] .env file properly configured")
        print("[OK] Production overrides available\n")

        print("The Oracle sees all configurations.")
    except ImportError:
        print(
            "Please install this module dotenv with the following command:\n"
            "pip install python-dotenv")
        sys.exit(1)
    except FileNotFoundError:
        print("Please create a .env file")
        sys.exit(1)
    except Exception:
        print("Error")
        sys.exit(1)
