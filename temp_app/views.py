from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixin import LoginRequiredMixin
from django.views import generic
from .models import Rooms
from .forms import RoomForm

# Create your views here.
def index(request):
	my_dict = {'insert_me': "coming from first app thing"}
	return render(request,'temp_app/index.html', context=my_dict)

class RoomListView(LoginRequiredMixin, generic.ListView):
	model = Rooms
	context_object_name = "room_list"
	template_name = 'index.html'
	paginate_by = 5

	def get_queryset(self):
		return Rooms.objects.filter(user_name = self.request.username)

def add_room(request):
	if request.method == 'POST':
		form = RoomForm()
		if form.is_valid():
			room = form.save(commit=False)
			room.nickname = request.save
			room.user_name = request.user
			room.save()
			return redirect('index', pk = room.pk)
	else:
		form = RoomForm()
	return render(request, 'temp_app/add_room.html', {'form':form})