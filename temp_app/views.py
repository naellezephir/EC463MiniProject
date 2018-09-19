from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth import logout as auth_logout
from .models import Room
from .forms import RoomForm

# Create your views here.
def index(request):
	return render(request,'temp_app/index.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

class RoomListView(generic.ListView):
	model = Room
	context_object_name = "room_list"
	template_name = 'index.html'
	paginate_by = 5

	def get_queryset(self):
		return Rooms.objects.filter(user_name = self.request.username)

def add_room(request):
	if request.method == 'POST':
		form = RoomForm(request.POST)
		if form.is_valid():
			room = form.save(commit = False)
			room.user_name = request.user
			room.save()
			return redirect('index')
	else:
		form = RoomForm()
	return render(request, 'temp_app/add_room.html', {'form':form})