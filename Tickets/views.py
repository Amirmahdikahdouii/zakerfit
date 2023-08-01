from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import AnonymousUsersQuestion, UserQuestion, UserQuestionReply
from .forms import AnonymousUsersQuestionForm, UserQuestionForm
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


class CreateUserQuestionView(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy("Accounts:login")
    form_class = UserQuestionForm
    template_name = "Tickets/add_user_question.html"
    model = UserQuestion
    success_url = reverse_lazy("Tickets:user_tickets")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = context['form']
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "سوال شما با موفقیت ثبت شد، به زودی توسط مربیان بررسی و پاسخ داده میشود")
        response = super().form_valid(form)
        return response


class UserTicketsView(LoginRequiredMixin, ListView):
    model = UserQuestion
    template_name = "Tickets/user_tickets.html"
    context_object_name = "questions"
    paginate_by = 12

    def get_queryset(self):
        return self.model.objects.filter(user_id=self.request.user.id).order_by("-created_at")
