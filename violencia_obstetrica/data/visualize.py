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