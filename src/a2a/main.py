import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")

def main():
    print("Welcome to agent2agent project!")
    print(f"OPENAI_API_KEY set: {bool(API_KEY)}")

if __name__ == "__main__":
    main() 