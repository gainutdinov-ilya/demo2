from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, CreateView

from application.forms import UserCreationForm
from application.models import Order


def index(request):
    return render(request, template_name='application/index.html')


class CreateOrderView(LoginRequiredMixin, CreateView):
    model = Order
    success_url = '/'
    template_name = 'application/create_order.html'

    fields = [
        'max_price',
        'photo',
        'description',
        'category',
    ]

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super(CreateOrderView, self).form_valid(form)

    def form_invalid(self, form):
        return super(CreateOrderView, self).form_invalid(form)


class RegisterView(FormView):
    form_class = UserCreationForm

    success_url = '/login'

    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterView, self).form_invalid(form)
