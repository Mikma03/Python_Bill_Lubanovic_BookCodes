import yaml
with open('wiersze.yaml', 'rt') as fin:
    text = fin.read()
    data = yaml.load(text)
    print(data['wiersze'][1]['tytul'])
