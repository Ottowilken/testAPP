import hashlib
from .models import User
from django.shortcuts import render_to_response
from django.conf import settings
from django.core.mail import send_mail
from django.template.context_processors import csrf
from django.utils.crypto import random
from .forms import RegisterForm, LoginForm

__author__ = 'Otto'


def customer_register_view(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            obj = form.save()
            id = obj.id
            request.session['user_id']=id
            request.session['first_name']=form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            random_string = str(random.random()).encode('utf8')
            salt = hashlib.sha1(random_string).hexdigest()[:5]
            salted = (salt + email).encode('utf8')
            activation_key = hashlib.sha1(salted).hexdigest()
            save_it = form.save(commit=False)
            save_it.save()
            subject = 'Account confirmation'
            message = "Hey %s, thanks for signing up. To activate your account, click this link within 48hours  \
            http://127.0.0.1:8000/customer_details/user_login/%s" % (first_name, activation_key)
            from_email = settings.EMAIL_HOST_USER
            to_list = [save_it.email]
            send_mail(subject, message, from_email, to_list, fail_silently=False)
            return render_to_response('activate.html')

    args = {}
    args.update(csrf(request))

    args['form'] = RegisterForm()
    print('4')
    return render_to_response('user_registration.html', args)


def activate_view(request):
    return render_to_response('activate.html')


def index(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('index.html', c)


def user_login_view(request, activation_key):
    c = {}
    c.update(csrf(request))
    return render_to_response('user_login.html', c)


def authenticate_view(request):
    form = LoginForm(request.POST)
    user_obj=User.objects.filter(email=request.POST.get('email'), password=request.POST.get('password'))
    if user_obj.count():
        request.session['user_id']=user_obj[0].id
        request.session['first_name']=user_obj[0].first_name
        message = "You are successfully registered, Have sent you an email to verify your account!"
        return render_to_response("authenticated_landing_page.html", {'form': form, 'message': message})

    else:
        message = "You have entered a wrong email or password!"
        return render_to_response("user_login.html", {'form': form, 'message': message})


def loggedin_view(request):
    return render_to_response('authenticated_landing_page.html')


def logout_view(request):
    del request.session['user_id']
    del request.session['first_name']
    request.session.modified=True
    return render_to_response('user_login.html')

