# ⚽ FIFA 2023 Dataset Explorer

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)

> 🚀 **Uma aplicação web interativa para explorar e analisar dados oficiais do FIFA 2023**

## 📊 Sobre o Projeto

O **FIFA 2023 Dataset Explorer** é uma aplicação web desenvolvida em Streamlit que permite explorar de forma interativa e visual um conjunto de dados abrangente sobre jogadores de futebol profissionais de 2023.

### 🎯 Características Principais

- **📈 Dashboard Interativo**: Interface moderna e responsiva para análise de dados
- **👥 Análise de Jogadores**: Perfis detalhados com estatísticas completas
- **🏟️ Análise de Clubes**: Visão geral das equipes e seus elencos
- **🔍 Filtros Avançados**: Busca e filtragem por clube, posição e estatísticas
- **📱 Design Responsivo**: Funciona perfeitamente em desktop e mobile

## 🚀 Funcionalidades

### 🏠 Página Inicial

- Visão geral do dataset com mais de **17.000 registros**
- Estatísticas gerais dos jogadores
- Filtros por contrato ativo e valor de mercado
- Ordenação por Overall (classificação geral)

### 👤 Análise de Jogadores

- **Perfil Completo**: Foto, nome, clube e posição
- **Estatísticas Físicas**: Idade, altura e peso
- **Métricas de Jogo**: Overall com barra de progresso visual
- **Informações Financeiras**: Valor de mercado, salário semanal e cláusula de rescisão
- **Filtros**: Seleção por clube e jogador específico

### 🏆 Análise de Clubes

- **Logo e Nome**: Identificação visual do clube
- **Tabela de Jogadores**: Estatísticas organizadas em colunas
- **Métricas Visuais**: Barras de progresso para Overall e salários
- **Colunas Configuráveis**: Dados organizados de forma clara e intuitiva

## 🛠️ Tecnologias Utilizadas

- **Streamlit** - Framework para aplicações web em Python
- **Pandas** - Manipulação e análise de dados
- **PIL (Pillow)** - Processamento de imagens
- **Requests** - Requisições HTTP para imagens

## 📦 Instalação e Uso

### Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)

### 🔧 Instalação

1. **Clone o repositório**

```bash
git clone https://github.com/seu-usuario/streamlit-fifa-dataset.git
cd streamlit-fifa-dataset
```

2. **Instale as dependências**

```bash
pip install -r requirements.txt
```

3. **Execute a aplicação**

```bash
streamlit run 1_home.py
```

4. **Acesse no navegador**

## 📁 Estrutura do Projeto

```
streamlit-fifa-dataset/
├── 1_home.py              # Página principal
├── pages/
│   ├── 2_players.py       # Análise de jogadores
│   └── 3_teams.py         # Análise de clubes
├── dataset/
│   └── CLEAN_FIFA23_official_data.csv  # Dataset principal
├── requirements.txt        # Dependências
└── README.md              # Este arquivo
```

## 📊 Dataset

O projeto utiliza o **FIFA 2023 Official Dataset** que contém:

- **17.000+ registros** de jogadores profissionais
- **Atributos demográficos**: Idade, nacionalidade, posição
- **Características físicas**: Altura, peso, preferência de pé
- **Estatísticas de jogo**: Overall, habilidades específicas
- **Informações contratuais**: Clube, salário, cláusula de rescisão
- **Dados de mercado**: Valor atual e histórico

## 👨‍💻 Autor

**Thiago Cunha**

## 🙏 Agradecimentos

- **EA Sports** pelo dataset oficial do FIFA 2023
- **Streamlit** pela excelente plataforma de desenvolvimento
- **Comunidade Python** pelo suporte e bibliotecas
