from django.http import HttpResponse
from django.views.generic import View
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.conf import settings

def render_to_pdf(template_src, context_dict={}): 
    template = get_template(template_src) 
    html = template.render(context_dict) 
    result = BytesIO() 
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result) 
    if not pdf.err: 
      return result.getvalue()
    else:
    	return HttpResponse(result.getvalue(), content_type='application/pdf')

class EmailView(View):
    def get(self, request, *args, **kwargs):
        context = dict()
        email_content = 'core/email-template.html'
        email_template = get_template(email_content).render(context)
        emails = [settings.DEVELOPER_EMAIL, ]
        email = EmailMessage(
            subject='Email Test',
            body=email_template,
            from_email=settings.EMAIL_HOST_USER, 
            to=emails
        )
        email.content_subtype='html'
        email.send()
        return HttpResponse(f'Email Sent at {emails}')

class PDFView(View):
    def get(self, request, *args, **kwargs):
        context = dict()
        pdf = render_to_pdf('core/pdf-template.html', context)
        return HttpResponse(
            pdf, content_type="application/pdf"
        )
        