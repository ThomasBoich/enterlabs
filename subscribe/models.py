from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class EmailCampaign(models.Model):
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
    def send(self):
        if not self.sent:
            recipients = [s.email for s in Subscriber.objects.filter(is_active=True)]
            send_email(self.subject, self.message, recipients)
            self.sent = True
            self.save()