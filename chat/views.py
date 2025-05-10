from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def room(request, room):
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': request.user.username,
        'room': room,
        'room_details': room_details
    })

@login_required
def checkview(request):
    if request.method == 'POST':
        step = request.POST.get('step', '1')
        room = request.POST.get('room_name', '')

        if step == '1':
            # Step 1: Check if room exists and show appropriate form
            if Room.objects.filter(name=room).exists():
                return render(request, 'home.html', {
                    'room_name': room,
                    'show_password': True,
                    'step': 2
                })
            else:
                return render(request, 'home.html', {
                    'room_name': room,
                    'show_set_password': True,
                    'step': 2
                })
        elif step == '2':
            # Step 2: Handle password logic
            if Room.objects.filter(name=room).exists():
                # Joining existing room
                password = request.POST.get('password', '')
                room_obj = Room.objects.get(name=room)
                if room_obj.password == password:
                    return redirect('/'+room+'/')
                else:
                    return render(request, 'home.html', {
                        'room_name': room,
                        'show_password': True,
                        'step': 2,
                        'error': 'Incorrect password for this room.'
                    })
            else:
                # Creating new room
                password = request.POST.get('password', '')
                confirm_password = request.POST.get('confirm_password', '')
                if not password:
                    return render(request, 'home.html', {
                        'room_name': room,
                        'show_set_password': True,
                        'step': 2,
                        'error': 'Password cannot be empty.'
                    })
                if password != confirm_password:
                    return render(request, 'home.html', {
                        'room_name': room,
                        'show_set_password': True,
                        'step': 2,
                        'error': 'Passwords do not match.'
                    })
                new_room = Room.objects.create(name=room, password=password)
                new_room.save()
                return redirect('/'+room+'/')
    return redirect('/')

@login_required
def send(request):
    message = request.POST['message']
    username = request.user.username
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

@login_required
def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})