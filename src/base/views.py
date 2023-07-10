from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# rooms = [
# 	{'id': 1, 'name': 'Let\'s learn Python'},
# 	{'id': 2, 'name': 'Design with me'},
# 	{'id': 3, 'name': 'Frontend Devs'},
# ]


def home(request):
	rooms = Room.objects.all()
	context = {
		'rooms': rooms
	}
	return render(request, 'base/home.html', context)


def room(request, pk):
	# room = None
	# for i in rooms:
	# 	if i['id'] == int(pk):
	# 		room = i
	room = Room.objects.get(id=pk)
	context = {'room': room}
	return render(request, 'base/room.html', context)


def create_room(request):
	form = RoomForm()
	if request.method == 'POST':
		form = RoomForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form': form}
	return render(request, 'base/room_form.html', context)


def update_room(request, pk):
	room = Room.objects.get(id=pk)
	form = RoomForm(instance=room)
	if request.method == 'POST':
		form = RoomForm(request.POST, instance=room)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'form': form}
	return render(request, 'base/room_form.html', context)


def delete_room(request, pk):
	room = Room.objects.get(id=pk)
	if request.method == 'POST':
		room.delete()
		return redirect('home')
	context = {'obj': room}
	return render(request, 'base/delete.html', context)
