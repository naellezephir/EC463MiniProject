from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixin import LoginRequiredMixin
from .models import Rooms

# Create your views here.
def index(request):
	my_dict = {'insert_me': "coming from first app thing"}
	return render(request,'temp_app/index.html', context=my_dict)

class RoomByUserListView(LoginRequiredMixin, generic.ListView):
	model = Rooms
	template_name = 'index.html'
	paginate_by = 5

	def get_queryset(self):
		return Rooms.objects.filter(user_name = self.request.username)

