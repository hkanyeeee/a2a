import os
from src.a2a.main import main

def test_main(capsys):
    os.environ["OPENAI_API_KEY"] = "test_key"
    main()
    captured = capsys.readouterr()
    assert "Welcome to agent2agent project!" in captured.out
    assert "OPENAI_API_KEY set: True" in captured.out 