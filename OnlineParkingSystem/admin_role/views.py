from django.shortcuts import render
from Landlord.models import Land_detail,Land_record
import seaborn as sns
import matplotlib as mpl
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView,ListView
from django.http import HttpResponseRedirect,HttpResponse
from User.views import myuser_login_required
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import datetime
import numpy as np
import pandas as pd
from django.forms.models import model_to_dict
import io

from matplotlib.patches import Circle
from pandas.plotting import register_matplotlib_converters
import math
class UserListView(ListView):
    model = Land_detail
    template_name = 'list.html' 
    context_object_name = 'users' 
    paginate_by = 5
    queryset = Land_detail.objects.all().order_by('no_of_spot')

class UserShortedView(ListView):
    id='lattitude'
    model = Land_detail
    template_name = 'list.html'  
    context_object_name = 'users' 
    paginate_by = 5
    def get_queryset(self):
        l=['address','description','end_date','langitude', 'lattitude', 'no_of_spot', 'price_per_hour', 'start_date']
        if self.request.GET.get('id') in l:
            order_by = self.request.GET.get('id') or 'lattitude'
        else:
            order_by = 'lattitude'
        qs = super(UserShortedView, self).get_queryset()
        return qs.order_by(order_by)

@myuser_login_required
def UserApproved(request):
    if request.method == 'POST':
        landid = request.POST.get('landid')
        landdetail = Land_detail.objects.get(landid=landid)
        landdetail.verified = 0
        landdetail.save()
        return HttpResponseRedirect('/admin_role/newLandList/',{'title':'User List','login':'True','role':request.session.get('role')})

@myuser_login_required
def change_date(x):
    return x.split('-')[0]

def change_panda(dict_frame):
    frame = pd.DataFrame(dict_frame)
    frame.set_index('start_date',inplace=True)
    frame.sort_index(inplace=True)
    return frame

@myuser_login_required
def getScatterdata(request):
    year_ = datetime.datetime.now().year
    record_data = Land_record.objects.all()
    dictionary_data = [x for x in record_data.values()]
    frame = change_panda(dictionary_data)
    start = datetime.date(year_,1,1)
    end = datetime.date(year_,12,31)
    frame = frame[(frame.index>=start)&(frame.index<=end)]

    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    frame.payment_remaining = frame.payment_remaining.apply(lambda x: 200 if x else 600)
    color = [ x for x in frame.payment_remaining ]
    axis.scatter(frame.index,frame.total_price,s=frame.payment_remaining,c=color,cmap="RdYlGn",alpha=0.8)
    data_set = set(zip(frame.index,frame.total_price))
    data_counts = frame.index.value_counts().to_dict()
    for xy in data_set:
        axis.annotate(data_counts[xy[0]],xy=xy,fontsize=15,color="black",va="bottom",ha="center")
    for tick in axis.get_xticklabels():
        tick.set_rotation(90)
    axis.xaxis.set_major_formatter(mpl.dates.DateFormatter('%b-%d'))
    fig.autofmt_xdate()
    axis.set_xlabel("Dates "+str(year_))
    axis.set_ylabel("Remaining Payment Amounts")
    axis.set_title("Payment History Of Landload "+str(year_))
    axis.tick_params(axis='x', colors='green')
    axis.tick_params(axis='y', colors='green')
    axis.legend([Circle((0,0), fc='r'),Circle((0,0), fc='g')], ["Payment Remaining","Payment Done"],loc='upper right')
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = HttpResponse(output.getvalue())
    response.mimetype = "img/png"
    return response


@myuser_login_required
def getHistdata(request):
    record_data = Land_record.objects.all()

    dictionary_data = [x for x in record_data.values()]
    frame = change_panda(dictionary_data)
    date_frame = frame.index.value_counts().sort_index()
    year_=datetime.datetime.now().year
    date=[]
    range_=[]
    for info in date_frame.iteritems():
        if info[0].year==year_:
            date.append(info[0])
            range_.append(info[1])
    fig = Figure()
    print(date)
    axis = fig.add_subplot(1, 1, 1)
    axis.plot(date,range_)
    #axis.xaxis.set_ticks(frame.index)
    axis.xaxis.set_major_formatter(mpl.dates.DateFormatter('%b-%d'))
    for tick in axis.get_xticklabels():
        tick.set_rotation(90)
    x_lab = "Dates For "+str(year_)
    title =  "User's Use history "+str(year_)
    axis.set_xlabel(x_lab)
    axis.set_ylabel("Number Of Users")
    axis.set_title(title)
    fig.autofmt_xdate()
    axis.tick_params(axis='x', colors='green')
    axis.tick_params(axis='y', colors='green')
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)

    response = HttpResponse(output.getvalue())
    response.mimetype = "img/png"
    return response