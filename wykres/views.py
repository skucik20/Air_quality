from django.shortcuts import render
import plotly.express as px
import plotly.graph_objects as go
from wykres.models import CO2, NO2, Location, PM10, PM25
from wykres.forms import DateForm

from wykres.static.wykres.arc_chart import aqi_calculation, pm25_chart, arc_figure, ozone_chart , NO2_chart, CO_chart, SO2_chart, pm10_chart
# Create your views here.


def dashboard(request):

    pm25 = list(PM10.objects.values('average'))[-1]
    pm25 = pm25['average']
    pm25_previous = list(PM10.objects.values('average'))[-2]
    pm25_previous = pm25_previous['average']
    pm10 = list(PM10.objects.values('average'))[-1]
    pm10 = pm10['average']
    pm10_previous = list(PM10.objects.values('average'))[-2]
    pm10_previous = pm10_previous['average']
    ozone = 0 # 0.06
    ozone_previous = 0 #0.1
    co = 0 #10
    co_previous = 0 #9
    so2 = 0 #300
    so2_previous = 0 #350
    # no2 = list(NO2.objects.values('average'))[-1]
    # no2 = no2['average']
    no2 = 0 #160
    no2_previous = 0 #list(NO2.objects.values('average'))[-2]
    no2_previous = 0 #no2_previous['average']


    dashboard_1 = arc_figure(NO2_chart(no2)['AQI'], NO2_chart(no2)['colors'], "NO2 AQI", NO2_chart(no2_previous)['AQI'])
    dashboard_2 = arc_figure(ozone_chart(ozone)['AQI'], ozone_chart(ozone)['colors'], "O3 AQI", ozone_chart(ozone_previous)['AQI'])
    dashboard_3 = arc_figure(CO_chart(co)['AQI'], pm25_chart(co)['colors'], "CO AQI", CO_chart(co_previous)['AQI'])
    dashboard_4 = arc_figure(SO2_chart(so2)['AQI'], SO2_chart(so2)['colors'], "SO2 AQI", SO2_chart(so2_previous)['AQI'])
    dashboard_5 = arc_figure(pm25_chart(pm25)['AQI'], pm25_chart(pm25)['colors'], "PM2.5 AQI", pm25_chart(pm25_previous)['AQI'])
    dashboard_6 = arc_figure(pm10_chart(pm10)['AQI'], pm10_chart(pm10)['colors'], "PM10 AQI", pm10_chart(pm10_previous)['AQI'])


    context = {'dashboard_1': dashboard_1, 'dashboard_2': dashboard_2, 'dashboard_3': dashboard_3, 'dashboard_4': dashboard_4, 'dashboard_5': dashboard_5, 'dashboard_6': dashboard_6}
    return render(request, 'wykres/dashboard.html', context)


def lista(request):

    co2 = list(CO2.objects.values('average'))[-1]
    no2 = list(NO2.objects.values('average'))[-1]
    pm10 = list(PM10.objects.values('average'))[-1]
    pm25 = list(PM25.objects.values('average'))[-1]

    context = {'co2': co2['average'],
               'no2': no2['average'],
               'pm10': pm10['average'],
               'pm25': pm25['average']}
    return render(request, 'wykres/lista.html', context)


def map(request):

    stations = list(Location.objects.values('latitude', 'longitude'))
    context = {'stations': stations}
    return render(request, 'wykres/home.html', context)


def chart(request):

    start = request.GET.get('start')
    end = request.GET.get('end')

    co2 = CO2.objects.all()
    if start:
        co2 = co2.filter(date__gte=start)
    if end:
        co2 = co2.filter(date__lte=end)

    fig = px.line(
        x=[c.date for c in co2],
        y=[c.average for c in co2],
        title="CO2 PPM",
        labels={'x': 'Date', 'y': 'CO2 PPM'}
    )


    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title={
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
    })

    chart = fig.to_html()
    context = {'chart': chart, 'form': DateForm()}
    return render(request, 'wykres/chart.html', context)
    #return render(request, 'wykres/dashboard.html', context)
#
def chart_pm10(request):

    start = request.GET.get('start')
    end = request.GET.get('end')

    pm10 = PM10.objects.all()
    if start:
        pm10 = pm10.filter(date__gte=start)
    if end:
        pm10 = pm10.filter(date__lte=end)

    fig = px.line(
        x=[c.date for c in pm10],
        y=[c.average for c in pm10],
        title="PM10 [µg/m<sup>3</sup>]",
        labels={'x': 'Data', 'y': 'PM10 [µg/m<sup>3</sup>]'}
    )


    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title={
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
    })

    chart = fig.to_html()
    context = {'chart_pm10': chart, 'form': DateForm()}
    return render(request, 'wykres/chart_pm10.html', context)
    # context_1 = {'chart_pm10': chart_1, 'form': DateForm()}
    # return render(request, 'chart_pm10.html', context_1)

#
def chart_no2(request):

    start = request.GET.get('start')
    end = request.GET.get('end')

    no2 = NO2.objects.all()
    if start:
        no2 = no2.filter(date__gte=start)
    if end:
        no2 = no2.filter(date__lte=end)

    fig = px.line(
        x=[c.date for c in no2],
        y=[c.average for c in no2],
        title="NO2 PPM",
        labels={'x': 'Data', 'y': 'NO2 PPM'}
    )


    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title={
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
    })

    chart = fig.to_html()
    context = {'chart_no2': chart, 'form': DateForm()}
    return render(request, 'wykres/chart_no2.html', context)
    # context_1 = {'chart_pm10': chart_1, 'form': DateForm()}
    # return render(request, 'chart_pm10.html', context_1)

def chart_pm25(request):

    start = request.GET.get('start')
    end = request.GET.get('end')

    pm25 = PM25.objects.all()
    if start:
        pm25 = pm25.filter(date__gte=start)
    if end:
        pm25 = pm25.filter(date__lte=end)

    fig = px.line(
        x=[c.date for c in pm25],
        y=[c.average for c in pm25],
        title="PM2.5 [µg/m<sup>3</sup>]",
        labels={'x': 'Data', 'y': 'PM25 [µg/m<sup>3</sup>]'}
    )


    fig.update_layout(
        template='plotly_dark',
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        title={
            'font_size': 24,
            'xanchor': 'center',
            'x': 0.5
    })

    chart = fig.to_html()
    context = {'chart_pm25': chart, 'form': DateForm()}
    return render(request, 'wykres/chart_pm25.html', context)
    # context_1 = {'chart_pm10': chart_1, 'form': DateForm()}
    # return render(request, 'chart_pm10.html', context_1)