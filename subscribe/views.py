from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SubscriberForm

class SubscribeView(CreateView):
    form_class = SubscriberForm
    success_url = reverse_lazy('subscribe')

    def form_valid(self, form):
        response = super().form_valid(form)
        # добавляем логику отправки подтверждения подписки на email
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        # добавляем логику обработки ошибок
        return response

def subscribe(request):
    form = SubscriberForm()
    return render(request, 'subscribe.html', {'form': form})

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_email(subject, message, recipient_list):
    from_email = 'noreply@yourdomain.com'
    html_content = render_to_string('email_template.html', {'message': message})
    msg = EmailMultiAlternatives(subject, message, from_email, recipient_list)
    msg.attach_alternative(html_content, "text/html")
    msg.send()