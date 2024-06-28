import sys
import cowsay

if len(sys.argv) == 2:
    cowsay.("Hello, " + sys.argv[1])

