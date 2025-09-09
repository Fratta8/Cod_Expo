import os

# Cores
RESET    = "\033[0m"
VERDE    = "\033[92m"
VERMELHO = "\033[91m"
AMARELO  = "\033[93m"
AZUL     = "\033[94m"
NEGRITO  = "\033[1m"

# Listas
livro = []
autor = []
ano = []
aluguel = []

# Função para salvar em arquivo
def salvar_livros_txt():
    with open("livros.txt ", "w", encoding="utf-8") as arquivo:
        for i in range(len(livro)):
            linha = f"{livro[i]} - {autor[i]} - {ano[i]} {aluguel[i]}\n"
            arquivo.write(linha)

# Função para carregar do arquivo
def carregar_livros_txt():
    if not os.path.exists("livros.txt"):
        return
    with open("livros.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().rsplit(" - ", 2)
            if len(partes) == 3:
                nome_livro, nome_autor, restante = partes
                try:
                    ano_info, status = restante.rsplit(" ", 1)
                    livro.append(nome_livro)
                    autor.append(nome_autor)
                    ano.append(int(ano_info))
                    aluguel.append(status)
                except ValueError:
                    continue

# Limpa terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Input de nome de livro
def nome_livro():
    while True:
        try:
            nome = input("Digite o nome do livro: ").strip 
            nome = nome.strip()
            if nome.replace(" ", "").isalpha():
                print(f"{VERDE}✅ Livro '{nome}' adicionado com sucesso.{RESET}")
                return nome
            else:
                print(f"{VERMELHO}❌ Use apenas letras e espaços.{RESET}")
        except Exception as e:
            print(f"{VERMELHO}❌ Erro: {e}{RESET}")

# Input de nome do autor
def nome_escritor():
    while True:
        try:
            nome_autor = input("Digite o nome do autor: ")
            nome_autor = nome_autor.strip()
            if nome_autor.replace(" ", "").isalpha():
                print(f"{VERDE}✅ Autor '{nome_autor}' adicionado com sucesso.{RESET}")
                return nome_autor
            else:
                print(f"{VERMELHO}❌ Use apenas letras e espaços.{RESET}")
        except Exception as e:
            print(f"{VERMELHO}❌ Erro: {e}{RESET}")

# Input do ano
def ano_lancamento():
    while True:
        try:
            ano_livro = int(input("Digite o ano de lançamento: "))
            if 1800 <= ano_livro <= 2025:
                return ano_livro
            else:
                print(f"{VERMELHO}❌ Ano inválido.{RESET}")
        except ValueError:
            print(f"{VERMELHO}❌ Digite um número válido.{RESET}")

# Adicionar livro
def adicionar_livro():
    nome = nome_livro()
    escritor = nome_escritor()
    ano_publicacao = ano_lancamento()
    status = "(DISPONÍVEL) "

    livro.append(nome)
    autor.append(escritor)
    ano.append(ano_publicacao)
    aluguel.append(status)

    salvar_livros_txt()
    limpar_tela()
    print(f"{VERDE}{NEGRITO}✅ Livro adicionado:{RESET}")
    print(f"{AZUL}📘 {nome} - ✍️  {escritor} - 📅 {ano_publicacao} {status}{RESET}")

# Emojis numéricos
def numero_para_emoji(numero):
    emojis = ['0️⃣', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣']
    return ' '.join(emojis[int(digito)] for digito in str(numero))

# Listar livros
def listar_livro():
    if not livro:
        print(f"{AMARELO}⚠️ Nenhum livro cadastrado.{RESET}")
    else:
        limpar_tela()
        print(f"{AZUL}{NEGRITO}📚 LIVROS:{RESET}")
        for i in range(len(livro)):
            numero_emoji = numero_para_emoji(i + 1)
            print(f"{AZUL}{numero_emoji}   {livro[i]} - Autor: {autor[i]} - Ano: {ano[i]} - {aluguel[i]}{RESET}")

# Menu para escolher campo a alterar
def menu_alterar_campo(indice):
    while True:
        print(f"\n{AZUL}{NEGRITO}✏️  O que deseja alterar?{RESET}")
        print(f"1️⃣  Nome do livro")
        print(f"2️⃣  Nome do autor")
        print(f"3️⃣  Ano de lançamento")
        print(f"4️⃣  Alterar tudo")
        print(f"0️⃣  Cancelar")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            novo_nome = nome_livro()
            livro[indice] = novo_nome
            print(f"{VERDE}✅ Nome do livro alterado!{RESET}")
            break
        elif escolha == "2":
            novo_autor = nome_escritor()
            autor[indice] = novo_autor
            print(f"{VERDE}✅ Nome do autor alterado!{RESET}")
            break
        elif escolha == "3":
            novo_ano = ano_lancamento()
            ano[indice] = novo_ano
            print(f"{VERDE}✅ Ano de lançamento alterado!{RESET}")
            break
        elif escolha == "4":
            novo_nome = nome_livro()
            novo_autor = nome_escritor()
            novo_ano = ano_lancamento()
            livro[indice] = novo_nome
            autor[indice] = novo_autor
            ano[indice] = novo_ano
            print(f"{VERDE}✅ Todos os campos alterados!{RESET}")
            break
        elif escolha == "0":
            print(f"{AMARELO}⚠️ Alteração cancelada.{RESET}")
            break
        else:
            print(f"{VERMELHO}❌ Opção inválida. Tente novamente.{RESET}")

# Alterar livro (modificado para usar menu_alterar_campo)
def alterar_livro():
    if not livro:
        print(f"{AMARELO}⚠️  Nenhum livro para alterar.{RESET}")
    else:
        try:
            listar_livro()
            alterar = int(input("Número do livro para alterar: ")) - 1
            if 0 <= alterar < len(livro):
                print(f"{AZUL}📘 Atual: {livro[alterar]} - ✍️  {autor[alterar]} - 📅 {ano[alterar]}{RESET}")
                menu_alterar_campo(alterar)
                aluguel[alterar] = "(DISPONÍVEL) "
                salvar_livros_txt()
            else:
                print(f"{VERMELHO}❌ Posição inválida.{RESET}")
        except ValueError:
            print(f"{VERMELHO}❌ Número inválido.{RESET}")

# Alugar livro
def alugar():
    if not livro:
        print(f"{AMARELO}⚠️  Nenhum livro cadastrado.{RESET}")
    else:
        try:
            listar_livro()
            op = int(input("Número do livro para alugar: ")) - 1
            if 0 <= op < len(livro):
                if aluguel[op] == "(INDISPONÍVEL) ":
                    print(f"{AMARELO}⚠️  Já está alugado.{RESET}")
                else:
                    aluguel[op] = "(INDISPONÍVEL)"
                    salvar_livros_txt()
                    print(f"{VERDE}📦   Aluguel de '{livro[op]}' feito com sucesso.{RESET}")
            else:
                print(f"{VERMELHO}❌  Posição inválida.{RESET}")
        except ValueError:
            print(f"{VERMELHO}❌  Número inválido.{RESET}")

# Devolver livro
def devolver():
    if not livro:
        print(f"{AMARELO}⚠️  Nenhum livro cadastrado.{RESET}")
    else:
        try:
            listar_livro()
            posicao = int(input("Número do livro para devolver: ")) - 1
            if 0 <= posicao < len(livro):
                if aluguel[posicao] == "(INDISPONÍVEL)":
                    aluguel[posicao] = "(DISPONÍVEL)"
                    salvar_livros_txt()
                    print(f"{VERDE}✅  Livro '{livro[posicao]}' devolvido.{RESET}")
                else:
                    print(f"{AMARELO}⚠️   Livro já disponível.{RESET}")
            else:
                print(f"{VERMELHO}❌ Posição inválida.{RESET}")
        except ValueError:
            print(f"{VERMELHO}❌ Número inválido.{RESET}")

# Deletar livro
def deletar_livro():
    if not livro:
        print(f"{AMARELO}⚠️  Nenhum livro cadastrado.{RESET}")
    else:
        try:
            listar_livro()
            posicao = int(input("Número do livro para deletar: ")) - 1
            if 0 <= posicao < len(livro):
                print(f"{VERDE}🗑️  Livro '{livro[posicao]}' deletado.{RESET}")
                del livro[posicao]
                del autor[posicao]
                del ano[posicao]
                del aluguel[posicao]
                salvar_livros_txt()
            else:
                print(f"{VERMELHO}❌ Posição inválida.{RESET}")
        except ValueError:
            print(f"{VERMELHO}❌ Número inválido.{RESET}")

# Popular livros de exemplo
def popular_livros_exemplo():
    if livro:
        print(f"{AMARELO}⚠️ Já existem livros cadastrados. Exclua-os antes de popular novamente.{RESET}")
        return

    livros_exemplo = [
        ("Dom Quixote", "Miguel de Cervantes", 1605),
        ("1984", "George Orwell", 1949),
        ("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943),
        ("Cem Anos de Solidão", "Gabriel García Márquez", 1967),
        ("A Revolução dos Bichos", "George Orwell", 1945),
        ("Orgulho e Preconceito", "Jane Austen", 1813),
        ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954),
        ("Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997),
        ("O Hobbit", "J.R.R. Tolkien", 1937),
        ("A Metamorfose", "Franz Kafka", 1915)
    ]

    for nome, autor_nome, ano_pub in livros_exemplo:
        livro.append(nome)
        autor.append(autor_nome)
        ano.append(ano_pub)
        aluguel.append("(DISPONÍVEL)")

    salvar_livros_txt()
    print(f"{VERDE}✅ Livros de exemplo adicionados com sucesso!{RESET}")

# Exibe menu principal
def exibir_menu():
    print(f"{AZUL}{NEGRITO}╔════════════════════════════╗")
    print("║     📚 MENU DA BIBLIOTECA  ║")
    print("╚════════════════════════════╝")
    print("1️⃣  Adicionar livros")
    print("2️⃣  Listar livros")
    print("3️⃣  Alterar livros")
    print("4️⃣  Deletar livros")
    print("5️⃣  Alugar livro")
    print("6️⃣  Devolver livro")
    print("7️⃣  Popular livros")
    print("0️⃣  Sair")
    print(f"══════════════════════════════{RESET}")

# Loop principal
def main():
    try:
        limpar_tela()
        exibir_menu()
        opcao = int(input("Escolha uma opção: "))
        limpar_tela()
        match opcao:
            case 1: adicionar_livro()
            case 2: listar_livro()
            case 3: alterar_livro()
            case 4: deletar_livro()
            case 5: alugar()
            case 6: devolver()
            case 7: popular_livros_exemplo()
            case 0:
                print(f"{AMARELO}{NEGRITO}👋  Encerrando o sistema...{RESET}")
                return False
            case _: print(f"{VERMELHO}❌ Opção inválida.{RESET}")
    except ValueError:
        limpar_tela()
        print(f"{VERMELHO}❌ Digite uma opção válida.{RESET}")
    return True

# Executa
if __name__ == "__main__":
    carregar_livros_txt()
    while main():
        
        input(f"\n{AZUL}Pressione Enter para continuar...{RESET}")
