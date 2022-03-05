filename = 'data/aneks.sql'


aneks = []
with open(filename, encoding='utf-8') as f:
    for line in f:
        if not line.startswith('INSERT'):
            continue

        start = line.find("'")
        end = line.find("'", start+1)

        anek = line[start+1:end]

        anek = anek.replace('\\n', '').lower()

        aneks.append(anek)
        print(anek)





