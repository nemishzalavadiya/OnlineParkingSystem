from django.shortcuts import render
from Landlord.models import Land_detail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView,ListView
from django.http import HttpResponseRedirect

class UserListView(ListView):
    model = Land_detail
    template_name = 'list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'users'  # Default: object_list
    paginate_by = 10
    queryset = Land_detail.objects.all().order_by('no_of_spot')  # Default: Model.objects.all()

class UserShortedView(ListView):
    id='lattitude'
    model = Land_detail
    template_name = 'list.html'  
    context_object_name = 'users' 
    paginate_by = 10
    queryset = Land_detail.objects.filter(verified=0)
    def get_queryset(self):
        order_by = self.request.GET.get('id') or 'lattitude'
        qs = super(UserShortedView, self).get_queryset()
        return qs.order_by(order_by)

def UserApproved(request):
    if request.method == 'POST':
        landid = request.POST.get('landid')
        landdetail = Land_detail.objects.get(landid=landid)
        landdetail.verified = 1
        landdetail.save()
        return HttpResponseRedirect('/admin_role/newLandList')

        
