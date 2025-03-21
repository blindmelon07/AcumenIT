from pathlib import Path


file = Path("hello.txt")
# file.unlink()
file.unlink(missing_ok=True)
