from django.core.mail import send_mail
from real_estate.settings.development import DEFAULT_FROM_EMAIL
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .models import Enquiry


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def send_enquiry_email(request):
    data = request.data

    try:
        subject = data['subject']
        message = data['message']
        name = data['name']
        email = data['email']
        from_email = data['email']
        recipient_list = [DEFAULT_FROM_EMAIL]

        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        enquiry = Enquiry(name=name, email=email, Subject=subject, message=message)
        enquiry.save()

        return Response({'success': 'Enquiry successfully submitted.'})

    except:
        return Response({'fail': 'Enquiry not submitted. Please try again'})
