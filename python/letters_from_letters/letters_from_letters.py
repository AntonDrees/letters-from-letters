"""Letters from letters."""

MAP = {
    'A': ('''
        A
   A A  
  AAAAA  
 A     A'''
    ),
}


def letter(char):
    """Derive letter from char."""
    return MAP.get(char)


if __name__ == '__main__':
    import sys
    for char in sys.argv[1:]:
        mapping = letter(char) or '?'
        display = '\n'.join(mapping).replace(' ', '_')
        print(f"{char} :-> {display}")
    
