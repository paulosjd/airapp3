from flask import render_template, Blueprint
from datetime import datetime, timedelta
import requests


def get_json_url(site, days):
    start = (datetime.now() - timedelta(days)).strftime("%d %b %Y")
    tomorrow = (datetime.now() + timedelta(1)).strftime("%d %b %Y")
    url = 'http://api.erg.kcl.ac.uk/AirQuality/Data/Site/SiteCode={0}/StartDate={1}/EndDate={2}/Json'.format(                              
        site, start, tomorrow).replace(' ', '%20')
    return url


def get_json(site, days):
    url = get_json_url(site, days)
    resp = requests.get(url)
    data = resp.json()
    array = data['AirQualityData']['Data']
    return array


def get_data(site, days):
    array = get_json(site, days)
    pm1 = [d['@Value'] if d['@Value'] == '' else float(d['@Value']) for d in array if d['@SpeciesCode'] == 'PM10'][
          days * -24:]
    pm2 = [d['@Value'] if d['@Value'] == '' else float(d['@Value']) for d in array if d['@SpeciesCode'] == 'FINE'][
          days * -24:]
    no2 = [d['@Value'] if d['@Value'] == '' else float(d['@Value']) for d in array if d['@SpeciesCode'] == 'NO2'][
          days * -24:]
    hours = list(map(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S").strftime('%H:%M'), ([d['@MeasurementDateGMT']
                 for d in array])))
    return dict(pm1=pm1, pm2=pm2, no2=no2, hours=hours)


def get_metadata_url(site):
    url = 'http://api.erg.kcl.ac.uk/AirQuality/Daily/MonitoringIndex/Latest/SiteCode={}/json'.format(site)
    return url


def get_metadata(site):
    url = get_metadata_url(site)
    resp = requests.get(url)
    data = resp.json()
    info_array = data['DailyAirQualityIndex']["LocalAuthority"]["Site"]
    return dict(site_name=info_array.get('@SiteName'), site_type=info_array.get('@SiteType'))


# chart title formatting
def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')


# chart title formatting
def custom_strftime(format, t):
    return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))


charts_blueprint = Blueprint('charts', __name__)

@charts_blueprint.route('/chart/<site><int:days>')
def make_chart(site='MY1', days=1, chartID='chart_ID', chart_type='line', chart_height=550, chart_width=800):
    data_dict = get_data(site, days)
    metadata_dict = get_metadata(site)
    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height, "width": chart_width}
    series = [{"name": 'PM10', "data": data_dict['pm1']}, {"name": 'PM2.5', "data": data_dict['pm2']},
              {"name": 'Nitrogen Dioxide', "data": data_dict['no2']}]
    title = {"text": 'Recent air pollution levels:   ' + (custom_strftime('%B {S}, %Y', datetime.now()))}
    xaxis = {"categories": data_dict['hours'][days * -24:]}
    yaxis = {"title": {"text": 'Concentration (ug/m3)'}}
    return render_template('detail.html', site_name=metadata_dict['site_name'], site_type=metadata_dict['site_type'],
                           chartID=chartID, chart=chart, series=series, title=title, xAxis=xaxis, yAxis=yaxis)

