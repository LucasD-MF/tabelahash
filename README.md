# 📌 Tabela Hash em Python

Este projeto implementa uma **Tabela Hash** em Python utilizando **listas encadeadas** para lidar com colisões. O objetivo é armazenar e manipular siglas de estados brasileiros de forma eficiente.

## 🚀 Funcionalidades
- Inserção de siglas na tabela hash 📝
- Remoção de siglas 🔄
- Impressão da tabela hash 📊
- Interface simples para interação via terminal 🖥️

## 📜 Como funciona?
- A tabela hash tem **10 posições**.
- A função de hash soma os valores ASCII dos caracteres da sigla e faz o **módulo por 10**.
- Caso a sigla seja "DF", ela será armazenada na posição **7** (implementação especial).
- A estrutura interna usa **listas encadeadas** para evitar colisões.

## 🛠️ Como executar?

### 📥 Clonando o repositório
```bash
git clone https://github.com/LucasD-MF/tabelahash.git
cd tabelahash
```

### ▶️ Executando o programa
```bash
python hash.py
```

## 📌 Exemplo de uso
```
1 - Inserir uma sigla na tabela
2 - Remover uma sigla da tabela
3 - Listar a tabela
4 - Sair
```

## 🔧 Tecnologias utilizadas
- Python 🐍

## 📄 Licença
Este projeto é de uso livre para fins acadêmicos e de aprendizado.

---
Criado por **LucasD-MF** 😊

