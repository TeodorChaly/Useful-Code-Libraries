import sys

# Run next command in cmd:
# python argument_parsing.py check.txt Hello_world!
# In this directory file with name check.txt will appear with Hello_world! inside

filename = sys.argv[1]  # First argument
text = sys.argv[2]  # Second argument

with open(filename, "w+") as f:
    f.write(text)
