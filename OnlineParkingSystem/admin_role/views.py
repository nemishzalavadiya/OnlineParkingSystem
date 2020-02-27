from django.shortcuts import render
from Landlord.models import Land_detail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView,ListView
from django.http import HttpResponseRedirect
from User.views import myuser_login_required


class UserListView(ListView):
    model = Land_detail
    template_name = 'list.html' 
    context_object_name = 'users' 
    paginate_by = 10
    queryset = Land_detail.objects.all().order_by('no_of_spot')
    
class UserShortedView(ListView):
    id='lattitude'
    model = Land_detail
    template_name = 'list.html'  
    context_object_name = 'users' 
    paginate_by = 10
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

        
