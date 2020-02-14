from django.shortcuts import render,HttpResponse,redirect
from .models import Message
import datetime
# Create your views here.




def home(request):
	if request.method == 'POST':
		name = request.POST['user-name']
		msg = request.POST['message']
		# print(msg)
		time = datetime.datetime.now()
		time = str(time)
		time = time[0:19]
		if name and msg and time :
			m = Message()
			m.name = name
			m.msg = msg
			m.time = time
			m.save()
			return redirect('/')
	return render(request,'home.html')


def PrintMessage(request):
	all_message = Message.objects.all()

	return render(request,'viewer.html',{'all_message':all_message})


