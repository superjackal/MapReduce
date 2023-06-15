import sys
for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        # # For Word Count
        # print(f'{word}\t{1}')

        # For Character Count
        characters = [*word]
        for character in characters:
            print(f'{character}\t{1}')

# Use "type new.txt | python mapper.py | python reducer.py" in cmd
