import streamlit as st
from page1 import ler_base
from graficos import bar_plot, polar_chart, pie_chart


def show():
    st.set_page_config(
        page_title="Dashboard Performance Fisica",
        page_icon="📊",
        layout="wide",  # 👈 faz a página ocupar toda a largura
    )
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
            <h3>Dietas</h3>
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

    matriz_genero = (df['Gender'] == genero_selecionado)

    idade = st.sidebar.slider(
        "Selecione a faixa de idade:",
        min_value=int(df['Age'].min()),
        max_value=int(df['Age'].max()),
        value=(int(df['Age'].min()), int(df['Age'].max())),
    )
    matriz_idade = (df['Age'] >= idade[0]) & (df['Age'] <= idade[1])

    if not genero_selecionado:
        calorias_por_dieta = df[matriz_idade].groupby(
            'diet_type')['Calories'].mean().reset_index(name='Qtd. Calorias')
    else:
        calorias_por_dieta = df[matriz_idade & matriz_genero].groupby(
            'diet_type')['Calories'].mean().reset_index(name='Qtd. Calorias')

    col_1, col_2 = st.columns(
        2, border=True, vertical_alignment='center', gap='large')

    with col_1:
        st.plotly_chart(bar_plot(calorias_por_dieta, x='diet_type', y='Qtd. Calorias',
                                 title='Calorias Médias x Tipo Dieta', x_title='Tipo Dieta', y_title='Calorias Médias'),
                        config={'scrollZoom': False}
                        )
    tipo_dieta = st.sidebar.segmented_control(
        'Selecione o tipo de dieta para ver os nutrientes:',
        options=df['diet_type'].unique(),
        width='stretch',
    )
    with col_2:

        if tipo_dieta:
            matriz_dieta = (df['diet_type'] == tipo_dieta)
        else:
            matriz_dieta = df['diet_type'].notnull()
        if not genero_selecionado:
            nutrientes = df[matriz_idade & matriz_dieta].groupby(
                'diet_type').agg(
                    Carbs=('Carbs', 'mean'),
                    Proteins=('Proteins', 'mean'),
                    Fats=('Fats', 'mean'),
                    sugar_g=('sugar_g', 'mean'),
                    sodium_mg=('sodium_mg', 'mean'),
                    cholesterol_mg=('cholesterol_mg', 'mean')
            )
        else:
            nutrientes = df[matriz_idade & matriz_genero & matriz_genero & matriz_dieta].groupby(
                'diet_type').agg(
                    Carbs=('Carbs', 'mean'),
                    Proteins=('Proteins', 'mean'),
                    Fats=('Fats', 'mean'),
                    sugar_g=('sugar_g', 'mean'),
                    sodium_mg=('sodium_mg', 'mean'),
                    cholesterol_mg=('cholesterol_mg', 'mean')
            )
        nutrientes = nutrientes.rename(columns={
            'sodium_mg': 'sodium_g',
            'cholesterol_mg': 'cholesterol_g'
        })
        nutrientes = nutrientes.reset_index().melt(id_vars='diet_type',
                                                   var_name='Nutriente', value_name='Value')
        nutrientes['Value'] = nutrientes.apply(lambda x: x['Value'] / 1000 if x['Nutriente'] in [
                                               'sodium_g', 'cholesterol_g'] else x['Value'], axis=1)

        if tipo_dieta:
            st.plotly_chart(bar_plot(nutrientes, x='Nutriente', y='Value',
                                     title='Nutrientes x Tipo Dieta', x_title='Tipo Dieta', y_title='Porções'),
                            config={'scrollZoom': True}
                            )
        else:
            st.plotly_chart(bar_plot(nutrientes, x='Nutriente', y='Value',
                                     title='Nutrientes x Tipo Dieta', x_title='Tipo Dieta', y_title='Porções', barmode='stack', color='diet_type'),
                            config={'scrollZoom': True}
                            )
    col_1, col_2 = st.columns(
        2, border=True, vertical_alignment='center', gap='large')

    with col_2:

        nutrientes_v2 = nutrientes.groupby('Nutriente').agg(
            Value=('Value', 'mean')
        ).reset_index()

        nutrientes_v2['Value%'] = nutrientes_v2.apply(
            lambda x: x['Value'] / nutrientes_v2['Value'].sum() * 100, axis=1)

        st.plotly_chart(
            pie_chart(nutrientes_v2, names='Nutriente', values='Value%',
                      title='Distribuição Percentual dos Nutrientes')
        )
    with col_1:
        st.header('Tabela de Nutrientes')
        st.dataframe(nutrientes)
