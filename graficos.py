import plotly.express as px


import plotly.express as px


def bar_plot(df, x, y, x_title, y_title, title, barmode='group', color=None):
    fig = px.bar(
        data_frame=df,
        x=x,
        y=y,
        color=color,

    )

    fig.update_layout(
        barmode=barmode,
        font=dict(color="white"),
        xaxis=dict(
            title=dict(
                text=x_title,
                font=dict(size=16, family='Arial', color='White')
            ),
            gridcolor="#2E2E2E"
        ),
        yaxis=dict(
            title=dict(
                text=y_title,
                font=dict(size=16, family='Arial', color='White')
            ),
            gridcolor="#2E2E2E"
        ),
        title=dict(
            text=title,
            xanchor="center",
            x=0.5,
            font=dict(size=20, family='Arial', color='White')
        ),
        legend=dict(
            title_font=dict(color="white"),
            font=dict(color="white")
        ),
        margin=dict(l=40, r=40, t=60, b=40)
    )

    # Só aplica cor única se o parâmetro 'color' não for usado
    if not color:
        fig.update_traces(
            marker=dict(
                color="#56479C",
                line=dict(color="#D3CDEF", width=2)
            ),
            selector=dict(type="bar")
        )

    return fig


def polar_chart(data, theta, r, title):
    fig = px.line_polar(
        data,
        theta='Workout_Type',
        r='Value',
        color='Metric',
        line_close=True,
        markers=True,
        color_discrete_map={
            'Calories_Burned': '#56479C',
            'Avg_BPM': '#D3CDEF',
            'Reps': '#D3CDEF'
        }
    )

    fig.update_traces(
        marker=dict(
            size=6,
            line=dict(color="#1E1E1E", width=1)
        ),
        selector=dict(mode='lines+markers')
    )

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="white"),
        legend=dict(
            title_font=dict(color="white"),
            font=dict(color="white")
        ),
        # margin=dict(l=50, r=50, t=50, b=50),
        polar=dict(
            bgcolor="rgba(0,0,0,0)",  # fundo polar transparente
            radialaxis=dict(
                gridcolor="#D3CDEF",
                linecolor="#D3CDEF",
                tickfont=dict(color="white"),
                visible=True,
                range=[0, data['Value'].max()*1.1]
            ),
            angularaxis=dict(
                gridcolor="#D3CDEF",
                linecolor="#D3CDEF",
                tickfont=dict(color="white")
            )
        ),
        title=dict(
            text=title,
            xanchor="center",
            x=0.5,
            font=dict(size=20, family='Arial', color='White')
        ),
    )

    return fig

def pie_chart(df, names, values, title):
    custom_colors = ['#3E206D', '#56479C', '#7A68C5', '#A084CA', '#C6B1E1', '#D3CDEF']
    fig = px.pie(df, names=names, values=values, title=title, color_discrete_sequence=custom_colors, labels={names: names, values: values})
    return fig