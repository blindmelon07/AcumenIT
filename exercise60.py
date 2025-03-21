from pathlib import Path

file = Path("hello.txt")
file.write_text("Hello World!")
file.write_text("good afternoon")

data = "Hello world\nGood afternoon"
file.write_text(data)

