# Esteira da Análise — BiblioTech

**Estudante:** Ana Vitória Schactae Brandão

## Funcionalidade 1: Cadastrar usuários

- **1.1 Fala do cliente:** "Eu queria que os servidores tivessem acesso a funcionalidades diferentes dos alunos na biblioteca para poder alterar e adicionar livros ao acervo e adiciona, bem como recuperar a senha do cadastro."
- **1.2 História de usuário:** Como biliotecário, quero ter acesso de moderador no sistema, para controlar o acervo e os empréstimos.
- **1.3 Requisito:** RF01 — O sistema deve diferenciar servidores e alunos por meio de tipo de matrícula (SIAP ou RA).
- **1.4 Requisito:** RF02 — O sistema deve permitir que usuários recuperem as senhas.
- **1.5 Caso de uso (RF01):** Aluno → "Identificar leitor" (verbo + objeto)
    Caso de uso (RF01):** Ator Bibliotecário → "Identificar moderador" (verbo + objeto)
    Caso de uso (RF02):** Ator Aluno/Bibliotecário → "Recuperar senha" (verbo + objeto)

## Funcionalidade 2: Feedback após o empréstimo

- **2.1 Fala do cliente:** "Quero poder escrever e armazenar observações após a devolução do livro para apontar possíveis mau usos ou problemas, para que o aluno possa consultá-las depois"
- **2.2 História de usuário:** Como bibliotecário, quero uma aba de feedbacks, para registrar observações sobre o empréstimo.
Como aluno, quero uma aba de feebacks, para consultar as observações das minhas devoluções
- **2.3 Requisito:** RF03 — O sistema deve permitir que um moderador registre suas observações após uma devolução.
- **2.4 Requisito:** RF04 — O sistma deve permitir que um aluno consulte as observações sobre suas devoluções.
- **2.5 Caso de uso (RF03):** Ator Bibliotecário → "Registrar feedback" (verbo + objeto)
- **2.6 Caso de uso (RF04):** Ator Aluno → "Consultar feedback" (verbo + objeto)

## Rastreabilidade

| Elipse no diagrama | Veio do requisito | Que veio da fala |
|---|---|---|
| | RF01 | "Identificar leitor" | 1.3 Requisito:** RF01 — O sistema deve diferenciar servidores e alunos por meio de tipo de matrícula (SIAP ou RA). | 1.1 Fala do cliente: "Eu queria que os servidores tivessem acesso a funcionalidades diferentes dos alunos na biblioteca para poder alterar e adicionar livros ao acervo e adiciona, bem como recuperar a senha do cadastro."
| | RF02 | "Recuperar senha" | 1.4 Requisito:**   RF02 — O sistema deve permitir que usuários recuperem as senhas. | 1.1 Fala do cliente: "Eu queria que os servidores tivessem acesso a funcionalidades diferentes dos alunos na biblioteca para poder alterar e adicionar livros ao acervo e adiciona, bem como recuperar a senha do cadastro." 
| | RF03 | "Registrar feedback" | 2.3 Requisito: RF03 — O sistema deve permitir que um moderador registre suas observações após uma devolução. | 2.1 Fala do cliente: "Quero poder escrever e armazenar observações após a devolução do livro para apontar possíveis mau usos ou problemas, para que o aluno possa consultá-las depois"  
| | RF04 | "Consultar feedback" | 2.4 Requisito: RF04 — O sistema deve permitir que um aluno consulte as observações sobre suas devoluções. | 2.1 Fala do cliente: "Quero poder escrever e armazenar observações após a devolução do livro para apontar possíveis mau usos ou problemas, para que o aluno possa consultá-las depois"
<!-- Nível A: conte o caminho completo de cada funcionalidade,
     da fala do cliente até o que está desenhado no diagrama. -->

## Relacionamento entre casos de uso (nível A)

- Tipo: «include»
- Entre: Identificar leitor / moderador e Validar matrícula
- Por que é esse e não o outro: Porque para identificar o usuário ou moderador precisa-se necessariamente de validar a matrícula (por RA ou SUAP).

- Tipo: «extend»
- Entre: Identificar leitor / moderador e recuperar senha
- Por que é esse e não o outro: Porque a recuperação de senha é opicional, apenas quando o usuário perde seu cadastro.

- Tipo: «include»
- Entre: Registrar feedback e Consultar empréstimo
- Por que é esse e não o outro: Porque para registrar observações na devolução é preciso buscar informações sobre aquele empréstimo específico
## Autoavaliação

**Conceito pretendido:** A

- Conversei sobre esta atividade com: Nath
- Esteira da análise: As duas esteiras seguem a estrutura solicitada, contendo a fala do cliente entre aspas, história no formato "Como/quero/para", RFS numerados e casos de uso com verbo + objeto com atores claros.
- Diagrama e notação: Cumprido. O diagrama possui fronteira "BiblioTech", atores externos, e elipses internas. As associações entre atores e elipses foram ajustadas para linhas simples (sem setas), e as relações de «include» e «extend» utilizam a notação tracejada correta com as justificativas incluídas.
- Rastreabilidade: Funcionalidade 1 (Identificação): O caminho começa na fala do cliente sobre o acesso de diferentes usuários ("Eu queria que os servidores tivessem acesso..."), que gerou a história do bibliotecário e o RF01 (diferenciar por tipo de matrícula). Esse requisito foi implantado no caso de uso "Identificar usuário", que está representado na elipse do diagrama ligado aos atores.
Funcionalidade 2 (Feedback): O caminho tem início na fala do cliente pedindo para registrar e consultar observações após a devolução ("Quero poder escrever e armazenar observações..."), originando a história de usuário e os RF03 e RF04. Eles se transformaram nos casos de uso "Registrar feedback" e "Consultar feedback", em que os nomes estão idênticos tanto na esteira quanto nas elipses desenhadas dentro da fronteira do sistema.
- Organização da entrega: A pasta está estruturada com os quatro arquivos corretos (`esteira-da-analise.md`, `diagrama-casos-de-uso.drawio`, `diagrama-casos-de-uso.png` e o `README.md` servindo como índice), contendo também a explicação da decisão de modelagem mais difícil.