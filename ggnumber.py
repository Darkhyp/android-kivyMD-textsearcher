separator = ['', ' ', '"', '_', '?', '!', ':', ';', '.', ',', '«', '\u201c', '(', '»', '\u201d', ')', '\n']
def count_occurences_in_text(word: str, text: str) -> int:
    """
    Return the number of occurrences of the passed word (case insensitive) in text
    """

    text = text.lower()
    word = word.lower()
    N = len(word)  # length of a searching word

    w_count = 0  # number of occurrences
    pos = 0  # starting position of text
    while True:
        n = text.find(word, pos)   # index of first occurrence
        if n >= 0:
            pos = n + N
            if (text[n-1:n] in separator or text[n-2:n].__eq__("''")) and (text[pos:pos+1] in separator or text[pos:pos+2].__eq__("''")):
                w_count += 1
        else:
            break

    return w_count


def get_python_constant(var):
    return str(globals()[var])
    
PHRASE_FOR_SEARCH = "sugar"

SAMPLE_TEXT_FOR_BENCH = """
A Suggestion Box Entry from Bob Carter

Dear Anonymous,

I'm not quite sure I understand the concept of this 'Anonymous' Suggestion Box. If no one reads what we write, then how will anything ever
change?

But in the spirit of good will, I've decided to offer my two cents, and hopefully Kevin won't steal it! (ha, ha). I would really like to
see more varieties of coffee in the coffee machine in the break room. 'Milk and sugar', 'black with sugar', 'extra sugar' and 'cream and su
gar' don't offer much diversity. Also, the selection of drinks seems heavily weighted in favor of 'sugar'. What if we don't want any suga
r?

But all this is beside the point because I quite like sugar, to be honest. In fact, that's my second suggestion: more sugar in the office.
Cakes, candy, insulin, aspartame... I'm not picky. I'll take it by mouth or inject it intravenously, if I have to.

Also, if someone could please fix the lock on the men's room stall, that would be helpful. Yesterday I was doing my business when Icarus ne
arly climbed into my lap.

So, have a great day!

Anonymously,
 Bob Carter
"""



