# Integrantes do grupo:

Ester Pereira Sousa: https://github.com/esterpsousa/gestao_de_vendas_imobiliarias

Mateus Alves Gouveia: https://github.com/MateusDB/gestao-vendas-imobiliarias

Leticia Medina:

Guilherme França Alves: https://github.com/Guifranca222/gestao_de_vendas_imobiliarias

Gustavo Figueiredo Soares: https://github.com/gustavofigueired07/gestao_vendas

Bruno Leonardo Silveira: https://github.com/silveiro21/gestao-vendas-imobiliarias

# Leitor de Mensagens do WhatsApp

Este projeto é uma ferramenta de automação em Python desenvolvida para capturar mensagens do WhatsApp Web de um contato ou grupo específico e exportar essas informações para uma planilha Excel.

## Bibliotecas Utilizadas

O projeto faz uso das seguintes bibliotecas principais:

- **Selenium**: Utilizada para a automação web. O Selenium permite controlar o navegador Google Chrome programaticamente, simulando a interação humana com a interface do WhatsApp Web.
- **Webdriver Manager**: Facilita o gerenciamento do driver do navegador. Ele baixa e configura automaticamente o ChromeDriver compatível com a versão do Google Chrome instalada na máquina, evitando problemas de compatibilidade e atualizações manuais.
- **OpenPyXL**: Responsável pela leitura e gravação de dados em arquivos do Excel (.xlsx). Após a extração das mensagens, esta biblioteca é utilizada para estruturar e salvar as informações na planilha para fácil visualização e armazenamento.

## Como Clonar e Executar em Outra Máquina

Siga o passo a passo abaixo para configurar o ambiente e executar o script em um novo computador.

### 1. Pré-requisitos

Certifique-se de ter instalado em sua máquina:
- Python 3.8 ou superior
- Git
- Navegador Google Chrome

### 2. Clonar o Repositório

Abra o terminal ou prompt de comando e execute o seguinte comando para clonar o repositório na sua máquina:

```bash
git clone https://github.com/Guifranca222/gestao_de_vendas_imobiliarias.git
cd <NOME_DA_PASTA_DO_REPOSITORIO>
```
*Observação: Substitua as tag `<NOME_DA_PASTA_DO_REPOSITORIO>` pelo nome da pasta criada após o clone.*

### 3. Criar e Ativar um Ambiente Virtual (Recomendado)

Para evitar conflitos com outras dependências instaladas globalmente no sistema, crie e ative um ambiente virtual:

**No Windows:**
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

**No Linux ou macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Instalar as Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias que estão listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 5. Executar o Projeto

Após a instalação bem-sucedida das bibliotecas, você pode rodar o arquivo principal. Pelo terminal, dentro do diretório do projeto, execute:

```bash
python main.py
```

### Primeiros Passos na Execução:

1. Na primeira execução, o script abrirá uma janela do Chrome. Você precisará fazer o login no WhatsApp Web escaneando o QR Code com o seu celular.
2. A sessão de login será armazenada em um diretório local (`chrome_profile`), de forma que nas execuções subsequentes você não precisará ler o QR Code novamente.
3. O terminal solicitará que você informe o nome exato do contato ou grupo do qual as mensagens serão extraídas.
4. O robô vai aguardar a interface carregar, ler as mensagens do chat selecionado e, ao finalizar, gravará todos os dados estruturados em um arquivo `.xlsx` (Excel) na mesma pasta do projeto.

