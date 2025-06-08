import time
import sys

def TypeWriter(text, delay = 0.08):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)

TypeWriter("Hello, World!")
