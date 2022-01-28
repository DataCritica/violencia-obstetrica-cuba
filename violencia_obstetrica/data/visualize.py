import pandas as pd
import plotly.graph_objects as go

def secuelas_bebe(df):
    list_secuelas = ['Parálisis cerebral', 
            'Discapacidad intelectual',
            'Convulsiones',
            'Retardo psicomotor',
            'Epilepsia',
            'Trastornos de comunicación',
            'Alteraciones sensoriales',
            'Muerte']

    fig = go.Figure(data=[
        go.Bar(name='Episiotomía', x=list_secuelas, y=df.iloc[0, 1:9], marker_color='mediumpurple'),
            go.Bar(name='Kristeller', x=list_secuelas, y=df.iloc[1, 1:9], marker_color='teal'),
            go.Bar(name='Dilatación Manual', x=list_secuelas, y=df.iloc[2, 1:9], marker_color='mediumvioletred')
        ])
    # Change the bar mode
    fig.update_layout(
        barmode='stack',
        title='Secuelas más frecuentes en el bebé de acuerdo al procedimiento realizado', 
        xaxis_title='Tipos de secuelas', 
        yaxis_title='Encuestadas',
        )
    return fig

def parto_atencion(df):
    tipo_parto = [
    'Cesárea de urgencia', 
    'Cesárea por fallar inducción del parto', 
    'Cesárea programada', 
    'Parto vaginal'
    ]

    fig = go.Figure(data=[
        go.Bar(name='Alto riesgo', x=tipo_parto, y=df.iloc[0, 1:5]),
        go.Bar(name='Bajo riesgo', x=tipo_parto, y=df.iloc[1, 1:5]),
        go.Bar(name='Otro', x=tipo_parto, y=df.iloc[2, 1:5])  
    ])
    # Change the bar mode
    fig.update_layout(
        barmode='stack', 
        title='Atención materna de acuerdo al tipo de parto', 
        xaxis_title='Tipo de parto', 
        yaxis_title='Encuestadas',
        )
    return fig