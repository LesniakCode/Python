''' dunder - __ 
- running module as script __name__ has value __main__ 
    and we can use it to call funcitons
- in python interpreter it will be imported without action 
    wait to be used

Sphinx can create HTML doc from Python docstrings

cmd line arguments - 
    sys.argv[0] - python file name 
    sys.argv[1] and other - passed arguments
'''
import sys
from urllib.request import urlopen


def fetch_word(url):
    """Fetch a list of words from a URL
    
    Args:
        url: The URL of a UTF-8 text document.

    Returns:
        A list of strings containing the words from
        the document   
    """
    story = urlopen(url)

    story_words = []

    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)

    story.close()
    return story_words


def print_items(items):
    for item in items:
        print (item)


def main(url):
    
    words = fetch_word(url)
    print_items(words)

print(__name__)
if __name__ == '__main__':
    main(sys.argv[1])