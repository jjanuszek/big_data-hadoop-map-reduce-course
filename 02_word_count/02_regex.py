import re

WORD_RE = re.compile(r'[\w]+')
words = WORD_RE.findall('Duda, lbafą,...,afsadsfdsf')
print(words)