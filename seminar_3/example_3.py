# настольной игре Скрабл (Scrabble) каждая буква имеет 
# определенную ценность

scrabble = dict()
scrabble [1] = 'A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'
scrabble [2] = 'D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У'
scrabble [3] = 'B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я'
scrabble [4] = 'F', 'H', 'V', 'W', 'Y', 'Й', 'Ы'
scrabble [5] = 'K', 'Ж', 'З', 'Х', 'Ц', 'Ч'
scrabble [8] = 'J', 'X', 'Ш', 'Э', 'Ю'
scrabble [10] = 'Q', 'Z', 'Ф', 'Щ', 'Ъ'

t = input()
text = list(t.upper())
print(sum([k for i in text for (k, v) in scrabble.items() if i in v]))


