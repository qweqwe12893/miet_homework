f = open('article_rus.txt')

letters= dict([ ('а', 0), ('б', 0), ('в', 0), ('г', 0), ('д', 0), ('е', 0), ('ё', 0), 
                ('ж', 0), ('з', 0), ('и', 0), ('й', 0), ('к', 0), ('л', 0), ('м', 0), 
                ('н', 0), ('о', 0), ('п', 0), ('р', 0), ('с', 0), ('т', 0), ('у', 0), 
                ('ф', 0), ('х', 0), ('ц', 0), ('ш', 0), ('щ', 0), ('ъ', 0), ('ы', 0), 
                ('ь', 0), ('э', 0), ('ю', 0), ('я', 0) ])

count = 0
for i in f.readlines():
    i = i.lower()
    
    for j in i:
        if j in letters:
            letters[j] += 1
            count += 1

letters = [(key, value) for key, value in letters.items()]
letters = sorted(letters, key=lambda x: x[1], reverse=True)


res  = open('article_rus_solve.txt', 'w')
for i in letters:
    res.write(f"""{i[0]}: {i[1]/count} \n""")
