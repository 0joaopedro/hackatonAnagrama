class Node(object):
    def __init__(self, letra='', final=False, tamanho=0):
        self.letra = letra
        self.final = final
        self.tamanho = tamanho
        self.children = {}
    def add(self, letras):
        node = self
        for index, letra in enumerate(letras):
            if letra not in node.children:
                node.children[letra] = Node(letra, index==len(letras)-1, index+1)
            node = node.children[letra]
    def anagrama(self, letras):
        escopo = {}
        for letra in letras:
            escopo[letra] = escopo.get(letra, 0) + 1
        tamanho_min = len(letras)
        return self._anagrama(escopo, [], self, tamanho_min)
    def _anagrama(self, escopo, path, root, tamanho_min):
        if self.final:
            palavra = ''.join(path)
            length = len(palavra.replace(' ', ''))
            if length >= tamanho_min:
                yield palavra
            path.append(' ')
            for palavra in root._anagrama(escopo, path, root, tamanho_min):
                yield palavra
            path.pop()
        for letra, node in self.children.items():
            c = escopo.get(letra, 0)
            if c == 0:
                continue
            escopo[letra] = c - 1
            path.append(letra)
            for palavra in node._anagrama(escopo, path, root, tamanho_min):
                yield palavra
            path.pop()
            escopo[letra] = c

def carrega_arquivo(path):
    retorno = Node()
    for linha in open(path, 'r'):
        palavra = linha.strip().lower()
        retorno.add(palavra)
    return retorno

def main():
    print ('Carregando lista.')
    palavras = carrega_arquivo('palavras.txt')
    while True:
        letras = input('Digite as palavras: ')
        letras = letras.lower()
        letras = letras.replace(' ', '')
        if not letras:
            break
        c = 0
        for palavra in palavras.anagrama(letras):
            print (palavra)
            c += 1
        print(('%d resultados.' % c))

if __name__ == '__main__':
    main()