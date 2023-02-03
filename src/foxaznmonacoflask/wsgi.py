from dataclasses import dataclass, field
from itertools import chain
from flask import Flask, render_template, request, url_for, redirect

from foxaznmonaco.build_report import build_report
from foxaznmonaco.print_report import _repr_time_delta

"""
http://localhost:5000/report shows common statistics
http://localhost:5000/report/drivers/  shows a list of driver's names and codes. 

The code should be a link to info about drivers
http://localhost:5000/report/drivers/?driver_id=SVF shows info about a driver

Also, each route could get the order parameter
http://localhost:5000/report/drivers/?order=desc
"""

app = Flask(__name__)
app.jinja_env.globals.update(my_func=_repr_time_delta)


@dataclass(slots=True)
class SortingFlag:
    sort_reversed: bool
    text: str = field(init=False)
    icon: str = field(init=False)

    def __post_init__(self):
        self.text = 'Descending' if self.sort_reversed else 'Ascending'
        self.icon = '\u2193' if self.sort_reversed else '\u2191'  # '↓ ↑' symbols


def _parse_sort_args(args) -> SortingFlag:
    return SortingFlag(True) if args.get('order') == 'desc' else SortingFlag(False)


@app.route('/')
def index():
    return redirect('/report/')


@app.route('/report/', methods=['GET'])
def report():
    # http://localhost:5000/report   (shows common statistics)
    page_title = 'RACE REPORT'
    flag = _parse_sort_args(request.args)
    good_list = sorted(report.good, reverse=flag.sort_reversed, key=lambda drv: drv.position)
    erro_list = sorted(report.erro, reverse=flag.sort_reversed, key=lambda drv: drv.full_name)
    return render_template('report.html', good_list=good_list, erro_list=erro_list, page_title=page_title, flag=flag)


@app.route('/report/drivers/', methods=['GET'])
def report_drivers():
    # http://localhost:5000/report/drivers/    (shows a list of driver's names and codes)

    all_drivers = chain(report.good, report.erro)
    if 'driver_id' in request.args.keys():
        driver_id = request.args['driver_id']
        driver, *_ = [driver for driver in all_drivers if driver.id == driver_id]
        img_path = url_for('static', filename=f'drivers/{driver.id}.png')
        flag = _parse_sort_args(request.args)
        page_title = f'Driver Profile: {driver.full_name}'
        return render_template('driver_profile.html', driver=driver, img_path=img_path, page_title=page_title, flag=flag)

    page_title = 'DRIVERS'
    flag = _parse_sort_args(request.args)
    list_by_id = sorted(all_drivers, reverse=flag.sort_reversed, key=lambda drv: drv.id)
    return render_template('report_drivers.html', data_list=list_by_id, page_title=page_title, flag=flag)


if __name__ == '__main__':
    report = build_report(path='..\..\data')
    app.run(debug=True)
else:
    report = build_report(path='../../data')
