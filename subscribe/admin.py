from django.contrib import admin

from subscribe.forms import SubscriberForm
from subscribe.models import EmailCampaign


# Register your models here.

@admin.register(EmailCampaign)
class EmailCampaignAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sent')
    actions = ['send_emails']

    def send_emails(self, request, queryset):
        for campaign in queryset:
            campaign.send()
        self.message_user(request, 'Emails sent successfully.')
    send_emails.short_description = 'Send selected email campaigns'
