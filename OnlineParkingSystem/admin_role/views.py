from django.shortcuts import render
from Landlord.models import Land_detail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView,ListView

class UserListView(ListView):
    model = Land_detail
    template_name = 'list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'users'  # Default: object_list
    paginate_by = 10
    queryset = Land_detail.objects.all().order_by('no_of_spot')  # Default: Model.objects.all()

class UserShortedView(ListView):
    id='lattitude'
    model = Land_detail
    template_name = 'list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'users'  # Default: object_list
    paginate_by = 10
    # def get_context_data(self, **kwargs):
    #     cls.id=self.kwargs['id']
    #     return self.kwargs['id']
    # queryset = Land_detail.objects.all().order_by(id)
    # def get_queryset(self):
    #     print(self.request.GET.get('request_data'))
    #     return Land_detail.objects.all().order_by(self.request.GET.get('request_data'))
    def get_queryset(self):
        order_by = self.request.GET.get('id') or 'lattitude'
        qs = super(UserShortedView, self).get_queryset()
        return qs.order_by(order_by)
