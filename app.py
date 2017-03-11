from flask import Flask, render_template
from urllib.request import urlopen
from datetime import datetime, timedelta
import json

app = Flask(__name__)


@app.route('/chart/index')
def index():
    return render_template('index.html')


def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


@app.route('/chart/<site><int:days>')
def detail(site='MY1', days=1, chartID='chart_ID', chart_type='line', chart_height=550, chart_width=800):
    start_time = (datetime.now() - timedelta(days)).strftime("%d %b %Y")
    tomorrow = (datetime.now() + timedelta(1)).strftime("%d %b %Y")
    url = 'http://api.erg.kcl.ac.uk/AirQuality/Data/Site/SiteCode={0}/StartDate={1}/EndDate={2}/Json'.format(site,
                                                                         start_time, tomorrow).replace(' ', '%20')
    resp = urlopen(url)
    data = json.loads(resp.read().decode(resp.info().get_param('charset') or 'utf-8'))
    array = data['AirQualityData']['Data']
    pm1 = [d['@Value'] if d['@Value'] == '' else float(d['@Value']) for d in array if d['@SpeciesCode'] == 'PM10'][
          days * -24:]
    pm2 = [d['@Value'] if d['@Value'] == '' else float(d['@Value']) for d in array if d['@SpeciesCode'] == 'FINE'][
          days * -24:]
    no2 = [d['@Value'] if d['@Value'] == '' else float(d['@Value']) for d in array if d['@SpeciesCode'] == 'NO2'][
          days * -24:]
    hours = list(map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S").strftime('%H:%M'), ([d['@MeasurementDateGMT']
                                                                                              for d in array])))
    info_url = 'http://api.erg.kcl.ac.uk/AirQuality/Daily/MonitoringIndex/Latest/SiteCode={}/json'.format(site)
    info_resp = urlopen(info_url)
    info_data = json.loads(info_resp.read().decode(info_resp.info().get_param('charset') or 'utf-8'))
    info_array = info_data['DailyAirQualityIndex']["LocalAuthority"]["Site"]
    site_name = info_array.get('@SiteName')
    site_type = info_array.get('@SiteType')
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, "width": chart_width}
    series = [{"name": 'PM10', "data": pm1}, {"name": 'PM2.5', "data": pm2},
              {"name": 'Nitrogen Dioxide', "data": no2}]
    title = {"text": 'Recent air pollution levels:   ' + (custom_strftime('%B {S}, %Y', datetime.now()))}
    xaxis = {"categories": hours[days * -24:]}
    yaxis = {"title": {"text": 'Concentration (ug/m3)'}}
    return render_template('detail.html', site_name=site_name, site_type=site_type, chartID=chartID, chart=chart,
                           series=series, title=title, xAxis=xaxis,
                           yAxis=yaxis)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)
