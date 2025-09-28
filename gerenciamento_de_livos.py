import matplotlib.pyplot as plt
from collections import defaultdict

class Livro:
    def __init__(self, titulo, autor, genero, quantidade_disponivel):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade_disponivel = quantidade_disponivel
    
    def __str__(self):
        return f"'{self.titulo}' por {self.autor} | Gênero: {self.genero} | Disponível: {self.quantidade_disponivel}"

# Lista para armazenar os livros
livros = []

def cadastrar_livro():
    """Função para cadastrar um novo livro"""
    print("\n=== CADASTRAR NOVO LIVRO ===")
    titulo = input("Título do livro: ")
    autor = input("Autor: ")
    genero = input("Gênero: ")
    
    while True:
        try:
            quantidade = int(input("Quantidade disponível: "))
            if quantidade < 0:
                print("A quantidade não pode ser negativa!")
                continue
            break
        except ValueError:
            print("Por favor, digite um número válido!")
    
    novo_livro = Livro(titulo, autor, genero, quantidade)
    livros.append(novo_livro)
    print(f"Livro '{titulo}' cadastrado com sucesso!")

def listar_livros():
    """Função para listar todos os livros"""
    print("\n=== LISTA DE LIVROS ===")
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    
    for i, livro in enumerate(livros, 1):
        print(f"{i}. {livro}")

def buscar_livro_por_titulo():
    """Função para buscar livro pelo título"""
    print("\n=== BUSCAR LIVRO ===")
    if not livros:
        print("Nenhum livro cadastrado.")
        return
    
    termo_busca = input("Digite o título ou parte do título: ").lower()
    encontrados = []
    
    for livro in livros:
        if termo_busca in livro.titulo.lower():
            encontrados.append(livro)
    
    if encontrados:
        print(f"\nLivros encontrados ({len(encontrados)}):")
        for i, livro in enumerate(encontrados, 1):
            print(f"{i}. {livro}")
    else:
        print("Nenhum livro encontrado com esse título.")

def gerar_grafico_generos():
    """Função para gerar gráfico de livros por gênero"""
    print("\n=== GRÁFICO POR GÊNERO ===")
    if not livros:
        print("Nenhum livro cadastrado para gerar gráfico.")
        return
    
    # Contar livros por gênero
    contador_generos = defaultdict(int)
    for livro in livros:
        contador_generos[livro.genero] += 1
    
    # Preparar dados para o gráfico
    generos = list(contador_generos.keys())
    quantidades = list(contador_generos.values())
    
    # Criar o gráfico
    plt.figure(figsize=(10, 6))
    plt.bar(generos, quantidades, color='skyblue')
    plt.title('Quantidade de Livros por Gênero')
    plt.xlabel('Gêneros')
    plt.ylabel('Quantidade de Livros')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Adicionar valores nas barras
    for i, valor in enumerate(quantidades):
        plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom')
    
    plt.show()
    print("Gráfico gerado com sucesso!")

def menu_principal():
    """Função do menu principal"""
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
        print("="*50)
        print("1. Cadastrar novo livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro por título")
        print("4. Gerar gráfico por gênero")
        print("5. Sair")
        print("="*50)
        
        opcao = input("Escolha uma opção (1-5): ")
        
        if opcao == '1':
            cadastrar_livro()
        elif opcao == '2':
            listar_livros()
        elif opcao == '3':
            buscar_livro_por_titulo()
        elif opcao == '4':
            gerar_grafico_generos()
        elif opcao == '5':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção entre 1 e 5.")

# Adicionar alguns livros de exemplo
def adicionar_livros_exemplo():
    """Função para adicionar alguns livros de exemplo"""
    exemplos = [
        ("Dom Casmurro", "Machado de Assis", "Romance", 5),
        ("1984", "George Orwell", "Ficção Científica", 3),
        ("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 4),
        ("Orgulho e Preconceito", "Jane Austen", "Romance", 2),
        ("Fundação", "Isaac Asimov", "Ficção Científica", 3),
        ("Harry Potter", "J.K. Rowling", "Fantasia", 6)
    ]
    
    for titulo, autor, genero, quantidade in exemplos:
        livros.append(Livro(titulo, autor, genero, quantidade))

if __name__ == "__main__":
    # Adicionar alguns livros de exemplo
    adicionar_livros_exemplo()
    print("Sistema de Gerenciamento de Biblioteca iniciado!")
    print("Alguns livros de exemplo foram adicionados.")
    menu_principal()