import sys
# This import prompt will go read everything from v20_sayings.py. If main() is read it will run the whole file
# main() cannot be used unconditionally
from v20_sayings import hello

if len(sys.argv) == 2:
    hello(sys.argv[1])
