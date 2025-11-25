🤖 Desafio de Automação Digital: Gestão de Peças, Qualidade e Armazenamento

📋 Sobre o Projeto

Este programa foi desenvolvido como parte da disciplina de Algoritmos e Lógica de Programação do curso de Graduação em Inteligência Artificial e Automações Digitais.

O objetivo é prototipar uma solução de automação digital para uma empresa industrial, substituindo a inspeção manual de peças por um sistema lógico e automático de controle de qualidade e gestão de inventário.

O sistema oferece um menu completo com as seguintes opções totalmente funcionais:

1. Cadastrar nova peça: Recebe dados (ID, Peso, Cor, Comprimento) e realiza a inspeção de qualidade.

2. Lista de peças aprovadas/reprovadas: Exibe todas as peças cadastradas e seus respectivos status.

3. Remover peça cadastrada: Permite excluir uma peça do sistema através do seu ID.

4. Listar caixas fechadas: Exibe o status do inventário e a contagem de caixas.

5. Gerar relatório final: Consolida todas as métricas de produção e motivos de reprovação.

📐 Critérios de Qualidade (Regras de Aprovação)
O sistema avalia cada peça com base nos seguintes parâmetros fixos:

Peso: Deve estar entre 95g e 105g.
Cor: Deve ser Azul ou Verde.
Comprimento: Deve estar entre 10cm e 20cm.

📦 Lógica de Armazenamento
As peças aprovadas são armazenadas em uma caixa_atual.

A capacidade máxima de cada caixa é de 10 peças.

Ao atingir 10 peças, a caixa é fechada e armazenada em caixas_fechadas, e uma nova caixa_atual é iniciada.

🚀 Como Rodar o Programa (Passo a Passo)
Para executar o sistema localmente, você precisa ter o Python instalado na sua máquina.

1. Clonar o Repositório
Abra o seu terminal (CMD, PowerShell ou Git Bash) e navegue até o diretório onde deseja salvar o projeto.

2. Executar o Script
Navegue até a pasta do projeto (onde está o arquivo .py) e execute o script Python.

📝 Exemplos de Entradas e Saídas
Aqui está um exemplo de uma sessão de uso no terminal, demonstrando o cadastro de uma peça aprovada e uma reprovada.

Ação 1: Cadastrar Peça Aprovada

Opção do Menu: 1

Entradas: ID: 1, Peso: 100, Cor: azul, Comprimento: 15

Resultado: 👉 Peça 1 - Status: Aprovada 👈

Ação do Sistema: Peça adicionada à caixa_atual.

Ação 2: Cadastrar Peça Reprovada

Opção do Menu: 1

Entradas: ID: 2, Peso: 90, Cor: verde, Comprimento: 12

Resultado: 👉 Peça 2 - Status: Reprovada (Peso fora do limite...) 👈

Ação do Sistema: Peça contabilizada, mas não adicionada à caixa.

Ação 3: Gerar Relatório Final

Opção do Menu: 5

Resultado: Total de peças aprovadas: 1, Total de peças reprovadas: 1, Motivos: Por peso: 1.

