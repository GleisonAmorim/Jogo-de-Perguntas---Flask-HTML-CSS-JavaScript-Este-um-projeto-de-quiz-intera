![image](https://github.com/user-attachments/assets/34b6bc9d-3bf8-4ae8-ae19-75d1e601bc62)

# Jogo de Perguntas - Flask + HTML + CSS + JavaScript

Este é um projeto de quiz interativo de perguntas e respostas.

## 📌 Objetivo do Projeto
O objetivo é testar os conhecimentos do jogador através de perguntas de múltipla escolha. A cada resposta, o jogador ganha ou perde pontos dependendo da dificuldade da fase. A interface não exibe mais o nível de dificuldade, mas a lógica interna continua funcionando.

---

## 🎯 Tecnologias Utilizadas

- Python 3.x
- Flask
- HTML5
- CSS3
- JavaScript (puro)

---

## 📁 Estrutura de Pastas e Arquivos

.
├── app.py                # Backend Flask
├── perguntas.json        # Banco de perguntas
├── templates/
│   └── index.html        # Frontend HTML
├── static/
│   └── style.css         # Estilo do jogo
└── README.md             # Documentação (este arquivo)

---

## 🚀 Como Executar Localmente

Pré-requisitos:
- Python 3.x instalado
- Flask instalado

Passos:

1. Coloque todos os arquivos nas pastas corretas conforme a estrutura acima.

2. Abra o terminal na pasta do projeto.

3. Rode o servidor Flask:

```
python app.py
```

4. Abra o navegador e acesse:

```
http://127.0.0.1:5000/
```

---

## 🕹️ Funcionalidades do Jogo

- Exibição de perguntas com múltiplas opções.
- Contagem de pontos baseada na dificuldade da fase.
- Feedback visual de resposta certa ou errada.
- Sistema de fases (fase sobe a cada acerto).
- Interface simples, com animações de transição.
- As perguntas são carregadas de um arquivo JSON.

---

## 📌 Alterações Recentes

- Removido: Exibição do texto de dificuldade.
- Mantida: A lógica de pontuação por dificuldade.
- Removido: Qualquer uso de GIFs de explosão.

---

## 📋 Como Adicionar Novas Perguntas

Abra o arquivo `perguntas.json` e siga este formato:

```
{
  "facil": [
    {
      "pergunta": "Qual a capital da França?",
      "opcoes": ["Paris", "Londres", "Berlim", "Madrid"],
      "resposta": "Paris"
    }
  ],
  "medio": [],
  "dificil": []
}
```

Adicione as perguntas dentro das categorias correspondentes.

---

## 📈 Possíveis Melhorias Futuras

- Ranking de jogadores.
- Contador de tempo por pergunta.
- Armazenamento de histórico de partidas.
- Banco de dados ao invés de JSON.

---

## ✅ Créditos

Desenvolvido por: [Seu Nome Aqui]
