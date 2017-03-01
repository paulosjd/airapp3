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
    # can replace [-24:] in pm1, pm2, no2 and axis assignments to [-n:] to have user input specify n
    site = 'MY1'
    today = datetime.now().strftime("%d %b %Y")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%d %b %Y")
    tomorrow = (datetime.now() - timedelta(days=-1)).strftime("%d %b %Y")
    url = 'http://api.erg.kcl.ac.uk/AirQuality/Data/Site/SiteCode={0}/StartDate={1}/EndDate={2}/Json'.format(site,
           yesterday, tomorrow).replace(' ', '%20')
    resp = urlopen(url)
    data = json.loads(resp.read().decode(resp.info().get_param('charset') or 'utf-8'))
    array = data['AirQualityData']['Data']
    #try/except for badrequest?
    pm1 = [d['@Value'] if d['@Value'] == '' else float(d['@Value']) for d in array if d['@SpeciesCode'] == 'PM10'][-24:]
    pm2 = [d['@Value'] if d['@Value'] == '' else float(d['@Value']) for d in array if d['@SpeciesCode'] == 'FINE'][-24:]
    no2 = [d['@Value'] if d['@Value'] == '' else float(d['@Value']) for d in array if d['@SpeciesCode'] == 'NO2'][-24:]
    hours = list(map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S").strftime('%H:%M'), ([d['@MeasurementDateGMT']
            for d in array])))
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, }
    series = [{"name": 'PM10', "data": pm1}, {"name": 'PM2.5', "data": pm2},
              {"name": 'Nitrogen Dioxide', "data": no2}]
    title = {"text": str(site + tomorrow)}
    xaxis = {"categories": hours[-24:]}
    yaxis = {"title": {"text": 'Concentration (ug/m3)'}}
    return render_template('detail.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xaxis,
                           yAxis=yaxis)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)

