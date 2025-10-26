Dashboard Interativo Multipaginado com Streamlit e Plotly

Este projeto é um conceito de dashboard interativo multipaginado desenvolvido para demonstrar o poder e a facilidade do Streamlit e Plotly na criação de visualizações de dados interativas e esteticamente agradáveis.

⚠️ Este projeto é apenas um conceito para demonstração e aprendizado. Não contém dados reais de colaboradores ou modelos preditivos funcionais.

Funcionalidades

Dashboards interativos e multipaginados

Filtros dinâmicos para explorar diferentes métricas

Gráficos customizados com Plotly (barras, radar, empilhados, etc.)

Suporte a tema escuro e paletas de cores personalizadas

Cache inteligente para otimizar performance

Estrutura modular, permitindo fácil expansão para novos filtros e gráficos

Tecnologias Utilizadas

Python

Streamlit
 — framework web para dashboards interativos

Plotly
 — visualizações gráficas interativas

Pandas
 — manipulação de dados

Estrutura do Projeto
dashboard-project/
│
├─ app.py                # Arquivo principal do Streamlit
├─ pages/                # Páginas do dashboard
│   ├─ page1.py
│   └─ dieta.py
├─ utils.py              # Funções auxiliares (carregamento de dados, filtros)
├─ data/                 # Base de dados (ex: CSVs de exemplo)
└─ README.md

Como Rodar

Clone o repositório:

git clone https://github.com/seu-usuario/dashboard-project.git
cd dashboard-project


Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Instale as dependências:

pip install -r requirements.txt


Execute o app:

streamlit run app.py

Possíveis Extensões

Integração com dados reais de People Analytics, como indicadores de colaboradores, engajamento e performance

Conexão com modelos preditivos, como probabilidade de turnover

Adição de gráficos mais complexos e visualizações avançadas

Implementação de dashboards responsivos para diferentes dispositivos

Contato

Desenvolvido por Kaique Silva
LinkedIn: https://www.linkedin.com/in/kaique-silva