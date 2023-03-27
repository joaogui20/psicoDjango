from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        mensagem = "Nome: " + message_name + "\nE-mail: " + message_email + "\nMensagem: " + message
        send_mail(
            'Contato',
            mensagem,
            message_email,
            ['azazazazaisjoao@gmail.com'], # to email
        )    
        
        return render(request, 'contact_us.html', {'message_name': message_name})
    else:
        return render(request, 'contact_us.html', {})

def appointment(request):
    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_message = request.POST['your-message']

        appointment = "Nome: " + your_name + "\nTelefone: " + your_phone + "\nE-mail: " + your_email + "\nEndereço: " + your_address + "\nHorário: " + your_schedule + "\nMensagem: " + your_message
        send_mail(
            'Marcação de um compromisso',
            appointment,
            your_email,
            ['azazazazaisjoao@gmail.com']
        )
        
        return render(request, 'appointment.html', {
            'your_name': your_name,
            'your_phone': your_phone,
            'your_email': your_email,
            'your_address': your_address,
            'your_schedule': your_schedule,
            'your_message': your_message
        })
    else:
        return render(request, 'appointment.html', {})