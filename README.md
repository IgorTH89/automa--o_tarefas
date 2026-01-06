# Automação de Cadastro de Produtos

Este projeto foi desenvolvido durante a Jornada Python da Hashtag Treinamentos. O objetivo é criar uma automação robótica de processos (RPA) 
que realiza o login em um sistema web e cadastra uma base de dados inteira de produtos de forma automática.

# Sobre o projeto

O projeto consiste em automatizar uma tarefa manual repetitiva: o cadastro de mais de 260 produtos em um sistema web. 
A automação simula as ações humanas de teclado e mouse para preencher campos como código, marca, tipo, categoria e preço, 
reduzindo o tempo de execução e eliminando erros humanos.

# Tecnologias Utilizadas

- Python
- PyAutoGUI
- Pandas
- Time

# Funcionalidades da Automação

1. Acesso ao Sistema: Abre o navegador e entra no link do sistema.
2. Login Automático: Preenche as credenciais de e-mail e senha.
3. Leitura de Dados: Importa uma base de dados .csv contendo as informações dos produtos.
4. Loop de Cadastro: Percorre cada linha da tabela e preenche os campos do formulário automaticamente.
5. Envio de Informações: Clica no botão de enviar e repete o processo até finalizar a lista.

# Como executar

1. Instale as dependencias:
"pip install pyautogui pandas"

2. Ajuste a posição do mouse:
Como a automação utiliza coordenadas da tela, utilize o script auxiliar pegar_posicao.py para mapear os pontos exatos
de clique no seu monitor

3. Prepare a base de dados:
Certifique de que o arquivo "produtos.csv" está na mesma pasta do código.

4. Rode o script principal:
"python main.py"

## ⚠️ Observações
- Pausas: O código utiliza pyautogui.PAUSE para definir um intervalo de segurança entre os comandos e evitar travamentos.
- Customização: A posição dos cliques pode variar dependendo da resolução do seu monitor, sendo necessário o mapeamento prévio.
- Parar o processo antes de finalizar: Mova o seu mouse pro canto superior direito da sua tela.
