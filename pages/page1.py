import streamlit as st
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from graficos import bar_plot, polar_chart



@st.cache_data
def ler_base():
    df = pd.read_csv('./data/Final_data.csv',)
    return df

def show():
    st.set_page_config(
        page_title="Dashboard Performance Fisica",
        page_icon="📊",
        layout="wide",  # 👈 faz a página ocupar toda a largura
    )

    st.markdown("""
        <style>
        div[data-testid="stHorizontalBlock"] > div:nth-child(1) {
            border: 2px solid #FFFFFF;
            padding: 10px;
            border-radius: 5px;
        }
        div[data-testid="stHorizontalBlock"] > div:nth-child(2) {
            border: 2px solid #FFFFFF;
            padding: 10px;
            border-radius: 5px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.sidebar.title('Filtros')



    df = ler_base()

    st.markdown(
        """
        <div style="text-align: center;">
            <h1>Dashboard | Life Style Data</h1>
            <a href='https://www.kaggle.com/datasets/jockeroika/life-style-data?resource=download'>Link Base no Kaggle </a>
            </br>
            <a href='https://www.linkedin.com/in/kaique-sousa-b66951248/'>Meu Linkedin</a>
        </div>
        """,
        unsafe_allow_html=True
    )


    st.divider()

    st.markdown(
        """
        <div style="text-align: center;">
            <h3>Desempenho e Frequências dos Treinos</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    genero_selecionado = st.sidebar.selectbox(
        "Selecione o Gênero:",
        options=df['Gender'].unique(),
        placeholder="Filtro por Genero",
        width='stretch',
        index=None,
        accept_new_options=True
    )
    idade = st.sidebar.slider(
        "Selecione a faixa de idade:",
        min_value=int(df['Age'].min()),
        max_value=int(df['Age'].max()),
        value=(int(df['Age'].min()), int(df['Age'].max())),
    )
    matriz_idade = (df['Age'] >= idade[0]) & (df['Age'] <=idade[1])
    
    if not genero_selecionado:
        qtd_exercicios = df[matriz_idade].groupby(['Workout_Type']).size().reset_index(name='Counts')
    else:
        qtd_exercicios = df[(df['Gender'] == genero_selecionado) & matriz_idade].groupby('Workout_Type').size().reset_index(name='Counts')
        
    col_1 , col_2 = st.columns(2, border=True, vertical_alignment='center', gap='large')



    with col_1:
    
        if genero_selecionado:
            titulo = f'Frequencia x Tipo de Exercicio | {genero_selecionado}' 
        else:
            titulo = 'Frequencia x Tipo de Exercicio'
        
        st.plotly_chart(
            bar_plot(qtd_exercicios, x='Workout_Type', y='Counts', x_title='Tipo de Exercicio', y_title='Qtd', title=titulo), config = {'scrollZoom': False}
        )

    if not genero_selecionado:
        media_calorias = df[matriz_idade].groupby(['Workout_Type'])['Calories_Burned'].mean().reset_index() 
    else:
        media_calorias = df[(df['Gender'] == genero_selecionado) & matriz_idade].groupby(['Workout_Type'])['Calories_Burned'].mean().reset_index()   

    with col_2:
        
        if genero_selecionado:
            titulo = f'Média da Queima de Calorias por Exercicio | {genero_selecionado}' 
        else:
            titulo = 'Média da Queima de Calorias por Exercicio'
        st.plotly_chart(
            bar_plot(media_calorias, x='Workout_Type', y='Calories_Burned', x_title='Tipo de Exercicio', y_title='Qtd. Calorias', title=titulo), config = {'scrollZoom': False}
        )


    col_3 , col_4 = st.columns(2, border=True, vertical_alignment='center', gap='large')


    # Supondo que você já fez o agrupamento

    if not genero_selecionado:
        polar_chart_data = df[matriz_idade].groupby('Workout_Type').agg(
            Calories_Burned=('Calories_Burned', 'mean'),
            Avg_BPM=('Avg_BPM', 'mean'),
            Reps=('Reps', 'mean')
        ).reset_index()

        # Transformando para long-form
        polar_chart_data = polar_chart_data.melt(
            id_vars='Workout_Type',
            value_vars=['Calories_Burned', 'Avg_BPM', 'Reps'],
            var_name='Metric',
            value_name='Value'
        )
    else:
        polar_chart_data = df[(df['Gender']== genero_selecionado)  & matriz_idade].groupby('Workout_Type').agg(
            Calories_Burned=('Calories_Burned', 'mean'),
            Avg_BPM=('Avg_BPM', 'mean'),
            Reps=('Reps', 'mean')
        ).reset_index()

        # Transformando para long-form
        polar_chart_data = polar_chart_data.melt(
            id_vars='Workout_Type',
            value_vars=['Calories_Burned', 'Avg_BPM', 'Reps'],
            var_name='Metric',
            value_name='Value'
        )


    with col_3:
        st.plotly_chart(polar_chart(polar_chart_data, theta='Workout_Type', r='Value', title='Tipos de Exercicio x Métricas'))

    if not genero_selecionado:
        musculo_mais_exercitado = df[matriz_idade].groupby(['Type of Muscle']).size().reset_index(name='Counts') 
    else:
        musculo_mais_exercitado = df[(df['Gender'] == genero_selecionado) & matriz_idade].groupby(['Type of Muscle']).size().reset_index(name='Counts')   
        
    with col_4:
        st.plotly_chart(bar_plot(musculo_mais_exercitado, x='Type of Muscle', y='Counts', x_title='Tipo de Musculo', y_title='Vezes Exercitado', title='Tipo de Musculo mais Exercitado'))
        
