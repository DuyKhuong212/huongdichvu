from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from test.models import FormApply
from django.core.mail import EmailMessage
# Create your views here.

class SiteLogin(LoginView):
    template_name = 'login1.html'

def gethome(request):
    return render(request, "content.html")
@login_required
def getAward(request):
    return render(request, "client/award.html")
def getApprove(request):
    return render(request, "admin/approve.html")


def deleteForm(request,id, email):

    if request.user.is_superuser:
        FormApply.objects.filter(id=id).delete()
        mail_subject = 'Phe duyet don dang ky giai thuong'
        message = "chuc ban may man lan sau"
        send_email = EmailMessage(mail_subject, message, to=[email])
        send_email.send()
        return redirect('approve')
# def getEmailForm(request,id):
#     if request.user.email
def testSendMail(request,id,email):

    if request.user.is_superuser:
        FormApply.objects.filter(id=id).update(status=1)
        mail_subject = 'Phe duyet don dang ky giai thuong'
        # fomApply=FormApply(request.POST)
        # email=fomApply['email'].value()
        # email='nguyenduykhuong0201t@gmail.com'
        message = "chuc mung ban da duoc phe duyet giai thuong roi"
        send_email = EmailMessage(mail_subject, message, to=[email])
        send_email.send()
        return redirect('approve')