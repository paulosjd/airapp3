from flask import Flask, render_template
from urllib.request import urlopen
from datetime import datetime, timedelta
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chart')
def detail(chartID='chart_ID', chart_type='line', chart_height=350):
    # site = request.form['site_choice']
    site = 'MY1'
    today = datetime.now().strftime("%d %b %Y")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%d %b %Y")
    url = 'http://api.erg.kcl.ac.uk/AirQuality/Data/Site/SiteCode={0}/StartDate={1}/EndDate={2}/Json'.format(site,
                                                                                                             yesterday,
                                                                                                             today).replace(
        ' ', '%20')
    # url = 'http://api.erg.kcl.ac.uk/AirQuality/Data/Site/SiteCode=MY1/StartDate=19%20Feb%202017/EndDate=20%20Feb%202017/Json'
    resp = urlopen(url)
    data = json.loads(resp.read().decode(resp.info().get_param('charset') or 'utf-8'))
    array = data['AirQualityData']['Data']
    hours = list(map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S").strftime('%H:%M'), ([d['@MeasurementDateGMT']
                                                                                              for d in array[0:24]])))
    try:
        pm10 = [float(d['@Value']) for d in array if d['@SpeciesCode'] == 'PM10']
    except ValueError:
        pm10 = [''] * 24
    try:
        pm25 = [float(d['@Value']) for d in array if d['@SpeciesCode'] == 'FINE']
    except ValueError:
        pm25 = [''] * 24
    try:
        no2 = [float(d['@Value']) for d in array if d['@SpeciesCode'] == 'NO2']
    except ValueError:
        no2 = [''] * 24
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
    series = [{"name": 'PM10', "data": pm10}, {"name": 'PM2.5', "data": pm25},
              {"name": 'Nitrogen Dioxide', "data": no2}]
    title = {"text": 'My Title'}
    xAxis = {"categories": hours}
    yAxis = {"title": {"text": 'Concentration (ug/m3'}}
    return render_template('detail.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis,
                           yAxis=yAxis)


"""
def index(chartID = 'chart_ID', chart_type = 'line', chart_height = 350): #chart_type = 'bar'
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = [{"name": 'PM10', "data": pm10}, {"name": 'PM2.5', "data": pm25}, {"name": 'Nitrogen Dioxide', "data": no2}]
    title = {"text": 'My Title'}
    xAxis = {"categories": hours}
    yAxis = {"title": {"text": 'Concentration (ug/m3'}}
    return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis,
                           yAxis=yAxis)
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
	title = {"text": 'My Title'}
	xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	yAxis = {"title": {"text": 'yAxis Label'}}
	return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
"""

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)

    # http://localhost:8080/
