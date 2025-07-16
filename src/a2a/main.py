import os

try:
    from dotenv import load_dotenv
except ModuleNotFoundError:  # pragma: no cover - fallback for environments without python-dotenv
    def load_dotenv(*args, **kwargs):
        """Fallback no-op when python-dotenv is unavailable."""
        return False

load_dotenv()

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    print("Welcome to agent2agent project!")
    print(f"OPENAI_API_KEY set: {bool(api_key)}")

if __name__ == "__main__":
    main() 