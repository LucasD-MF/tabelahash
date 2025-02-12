class ElementoDaListaSimples:
    def __init__(self, chave=None):
        self.chave = chave #Valor armazenado no nodo [Aulaprática5]
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.head = None # Inicializa a cabeça da lista encadeada como None [Aulaprática5]

    def inserir(self, chave): #[Aulaprática5]
        nodo = ElementoDaListaSimples(chave) # Cria um novo nó com a sigla especificada
        nodo.proximo = self.head #aponta para o próximo nó da lista
        self.head = nodo #novo nodo se torna o head

    def remover(self, chave): #Remove o nodo = sigla da lista encadeada. E ajusta o ponteiro.
        atual = self.head
        anterior = None
        while atual is not None:
            if atual.chave == chave:
                if anterior is None:
                    self.head = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return True
            anterior = atual
            atual = atual.proximo
        return False

    def imprimir(self): #imprimi a lista na tela
        temp = self.head
        while temp:
            print(f'{temp.chave}', end=" -> ")
            temp = temp.proximo
        print("None")

class TabelaHash: # Inicializa uma tabela hash com 10 posições. [Aulaprática5]
    def __init__(self):
        self.tam = 10
        self.h = [ListaEncadeada() for _ in range(self.tam)]

    def hashFuncSigla(self, k): #Calcula o AscII da sigla (a+b)
        k = list(k)
        if ''.join(k) == 'DF': #Adaptação do código da aulaprática5 para DF sempre retornar na posição 7
            return 7
        else:
            return (ord(k[0]) + ord(k[1])) % self.tam

    def inserir(self, chave): #Permite que o usuário insira na uma sigla
        pos = self.hashFuncSigla(chave)
        self.h[pos].inserir(chave)

    def remover(self, chave):  # Calcula a posição na Tabelahash, e chama a função remover da lista encadeada.
        pos = self.hashFuncSigla(chave)
        return self.h[pos].remover(chave)

    def imprimir(self): #impressão de todas as listas encadeadas que estão dentro da tabela hash.
        for i in range(self.tam):
            print(f'{i}:', end=" ")
            self.h[i].imprimir()

# Lista de estados e suas siglas1
estados = [
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
    ("LF", "Lucas Francisco")
]

# Criar instância da tabela hash
geral = TabelaHash()

# Inserir estados na tabela hash
for sigla, nome in estados:
    geral.inserir(sigla)

# Programa Principal para interação com o usuário
while True:
    print('RU: 3767463')
    print('1 - Inserir na SIGLA na tabela')
    print('2 - Remover da SIGLA da tabela')
    print('3 - Listar a tabela')
    print('4 - Sair')
    print('')

    op = int(input('Escolha uma opção: '))
    if op == 1:
        chave = input('Digite a sigla de um estado: ').upper()
        if len(chave) != 2 or not chave.isalpha():
            print('A sigla deve conter exatamente 2 letras.')
            continue
        geral.inserir(chave)

    elif op == 2:
        chave = input('Digite a sigla do estado que deseja remover: ').upper()
        if geral.remover(chave):
            print(f'Sigla {chave} removida com sucesso.')
        else:
            print(f'Sigla {chave} não encontrada na tabela.')

    elif op == 3:
        geral.imprimir()

    elif op == 4:
        print('Encerrando...')
        break

    else:
        print('Opção inválida. Tente novamente.')