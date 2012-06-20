# Create your views here.
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from core.forms import ContactForm


def home(request):
    return render(request, 'core/home.html')


class DataContact(object):
    def __init__(self, name=None, email=None, message=None):
        self.name = name
        self.email = email
        self.message = message


def contact(request):
    success = False
    context = {}
    name, email, message = None, None, None
    contact_sent = request.session.get('contact_sent', False)

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if request.session.test_cookie_worked():
            print 'WORKED'
        else:
            print 'DOES NOT WORK'

        if contact_form.is_valid():
            success = True
            data_contact = DataContact()
            data_contact.name = contact_form.cleaned_data['name']
            data_contact.email = contact_form.cleaned_data['email']
            data_contact.message = contact_form.cleaned_data['message']
            request.session['data_contact'] = data_contact

            name = request.session['data_contact'].name
            email = request.session['data_contact'].email
            message = request.session['data_contact'].message

            print data_contact.name
            print data_contact.email
            print data_contact.message

            request.session['contact_sent'] = True

    else:
        contact_form = ContactForm()

    context = {
        'success': success,
        'contact_sent': contact_sent,
        'contact_form': contact_form,
        'name': name,
        'email': email,
        'message': message,
    }

    request.session.set_test_cookie()

    return render(request, 'core/contact.html', context)


def data_contact_clear(request):
    data_contact = request.session['data_contact']
    print data_contact.name
    print data_contact.email
    print data_contact.message

    data_contact = DataContact()
    print data_contact.name
    print data_contact.email
    print data_contact.message

    return redirect(reverse('core:contact'))


def contact_sent_clear(request):
    if 'contact_sent' in request.session:
        del request.session['contact_sent']
    
    return redirect(reverse('core:contact'))
