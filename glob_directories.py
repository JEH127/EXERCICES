from pathlib import Path

#path = Path("foo")
# path.mkdir() => create directory
# path.rmdir() => remove directory
path = Path()
for file in path.glob('*'):
    print(file)
