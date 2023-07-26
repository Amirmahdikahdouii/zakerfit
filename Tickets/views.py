from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import AnonymousUsersQuestion
from .forms import AnonymousUsersQuestionForm
from django.urls import reverse_lazy
from django.contrib import messages


class AnonymousUsersQuestionCreateView(CreateView):
    model = AnonymousUsersQuestion
    form_class = AnonymousUsersQuestionForm
    template_name = "Home/index.html"
    success_url = reverse_lazy('Home:home_view')
    template_name_field = "anonymous_ticket_form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anonymous_ticket_form'] = context['form']
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "سوال شما ثبت شد، به زودی با شما تماس می گیریم.")
        return response
