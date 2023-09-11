import plotly.graph_objects as go


def aqi_calculation(c_low, c_high, i_low, i_high, c):


    aqi = ((i_high - i_low) / (c_high - c_low)) * (c - c_low) + i_low
    return aqi


def ozone_chart(ozone):


    # colors = ["green", "#FECB52", "#FF9900", "#FD3216", "#990099", "rgb(102,17,0)"]
    if ozone <= 0.054:
        AQI = aqi_calculation(0, 0.054, 0, 50, ozone)
        colors = "green"

    elif ozone >= 0.055 and ozone < 0.070:

        AQI = aqi_calculation(0.055, 0.070, 51, 100, ozone)
        colors = "#FECB52"

    elif ozone >= 0.071 and ozone < 0.085:
        AQI = aqi_calculation(0.071, 0.085, 101, 150, ozone)
        colors = "#FF9900"

    elif ozone >= 0.086 and ozone < 0.105:
        AQI = aqi_calculation(0.086, 0.105, 151, 200, ozone)
        colors = "#FD3216"

    elif ozone >= 0.106 and ozone < 0.200:
        AQI = aqi_calculation(0.105, 0.200, 201, 300, ozone)
        colors = "#990099"

    else:
        AQI = aqi_calculation(0.200, 0.600, 301, 500, ozone)
        colors = "rgb(102,17,0)"
    parameters = {'AQI': AQI, 'colors': colors}
    return parameters

def NO2_chart(NO2):


    # colors = ["green", "#FECB52", "#FF9900", "#FD3216", "#990099", "rgb(102,17,0)"]
    if NO2 <= 53:
        AQI = aqi_calculation(0, 53, 0, 50, NO2)
        colors = "green"

    elif NO2 >= 54 and NO2 < 100:

        AQI = aqi_calculation(54, 100, 51, 100, NO2)
        colors = "#FECB52"

    elif NO2 >= 101 and NO2 < 360:
        AQI = aqi_calculation(101, 360, 101, 150, NO2)
        colors = "#FF9900"

    elif NO2 >= 361 and NO2 < 649:
        AQI = aqi_calculation(361, 649, 151, 200, NO2)
        colors = "#FD3216"

    elif NO2 >= 650 and NO2 < 1249:
        AQI = aqi_calculation(650, 1249, 201, 300, NO2)
        colors = "#990099"

    else:
        AQI = aqi_calculation(1249, 2049, 301, 500, NO2)
        colors = "rgb(102,17,0)"
    parameters = {'AQI': AQI, 'colors': colors}
    return parameters

def CO_chart(CO):

    if CO <= 4.4:
        AQI = aqi_calculation(0, 4.4, 0, 50, CO)
        colors = "green"

    elif CO >= 4.5 and CO < 9.4:

        AQI = aqi_calculation(4.5, 9.4, 51, 100, CO)
        colors = "#FECB52"

    elif CO >= 9.5 and CO < 12.4:
        AQI = aqi_calculation(9.5, 12.4, 101, 150, CO)
        colors = "#FF9900"

    elif CO >= 12.5 and CO < 15.4:
        AQI = aqi_calculation(12.5, 15.4, 151, 200, CO)
        colors = "#FD3216"

    elif CO >= 15.5 and CO < 30.4:
        AQI = aqi_calculation(15.5, 30.4, 201, 300, CO)
        colors = "#990099"

    else:
        AQI = aqi_calculation(30.5, 50.4, 301, 500, CO)
        colors = "rgb(102,17,0)"
    parameters = {'AQI': AQI, 'colors': colors}
    return parameters

def SO2_chart(SO2):

    if SO2 <= 35:
        AQI = aqi_calculation(0, 35, 0, 50, SO2)
        colors = "green"

    elif SO2 >= 36 and SO2 < 75:

        AQI = aqi_calculation(36, 75, 51, 100, SO2)
        colors = "#FECB52"

    elif SO2 >= 76 and SO2 < 185:
        AQI = aqi_calculation(76, 185, 101, 150, SO2)
        colors = "#FF9900"

    elif SO2 >= 186 and SO2 < 304:
        AQI = aqi_calculation(186, 304, 151, 200, SO2)
        colors = "#FD3216"

    elif SO2 >= 305 and SO2 < 604:
        AQI = aqi_calculation(305, 604, 201, 300, SO2)
        colors = "#990099"

    else:
        AQI = aqi_calculation(605, 1004, 301, 500, SO2)
        colors = "rgb(102,17,0)"
    parameters = {'AQI': AQI, 'colors': colors}
    return parameters

def pm25_chart(PM25):


    # colors = ["green", "#FECB52", "#FF9900", "#FD3216", "#990099", "rgb(102,17,0)"]
    if PM25 <= 12:
        AQI = aqi_calculation(0, 12, 0, 50, PM25)
        colors = "green"

    elif PM25 >= 12.1 and PM25 < 35.4:

        AQI = aqi_calculation(12.1, 35.4, 51, 100, PM25)
        colors = "#FECB52"

    elif PM25 >= 35.5 and PM25 < 55.4:
        AQI = aqi_calculation(35.5, 55.4, 101, 150, PM25)
        colors = "#FF9900"

    elif PM25 >= 55.5 and PM25 < 150.4:
        AQI = aqi_calculation(55.5, 150.4, 151, 200, PM25)
        colors = "#FD3216"

    elif PM25 >= 150.5 and PM25 < 250.4:
        AQI = aqi_calculation(150.5, 250.4, 201, 300, PM25)
        colors = "#990099"

    else:
        AQI = aqi_calculation(250.5, 500.4, 301, 500, PM25)
        colors = "rgb(102,17,0)"
    parameters = {'AQI': AQI, 'colors': colors}
    return parameters


def pm10_chart(pm10):


    # colors = ["green", "#FECB52", "#FF9900", "#FD3216", "#990099", "rgb(102,17,0)"]
    if pm10 <= 54:
        AQI = aqi_calculation(0, 54, 0, 50, pm10)
        colors = "green"

    elif pm10 >= 55 and pm10 < 154:

        AQI = aqi_calculation(55, 154, 51, 100, pm10)
        colors = "#FECB52"

    elif pm10 >= 155 and pm10 < 254:
        AQI = aqi_calculation(155, 254, 101, 150, pm10)
        colors = "#FF9900"

    elif pm10 >= 255 and pm10 < 354:
        AQI = aqi_calculation(255, 354, 151, 200, pm10)
        colors = "#FD3216"

    elif pm10 >= 355 and pm10 < 424:
        AQI = aqi_calculation(355, 424, 201, 300, pm10)
        colors = "#990099"

    else:
        AQI = aqi_calculation(425, 604, 301, 500, pm10)
        colors = "rgb(102,17,0)"
    parameters = {'AQI': AQI, 'colors': colors}
    return parameters

def arc_figure(aqi, color, title, previous):

    fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=aqi,
        mode="gauge+number+delta",
        title={'text': title},
        delta={'reference': previous},
        gauge={'axis': {'range': [None, 500]},  # }))
               'bar': {'color': color}}))
    #

    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title={
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
        })
    fig_html = fig.to_html()
    return fig_html


