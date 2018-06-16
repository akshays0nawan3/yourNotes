from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime
from django.contrib.auth import login, logout, authenticate
from YourNotes.models import User, userNotes

# Create your views here.

def login_view(request):
	if request.session.has_key('username'):
		username = request.session['username']
		return HttpResponseRedirect(reverse('YourNotes:notelist', args=(username,)))
	else:
		return render(request, 'YourNotes/login1.html')

def loginprocess_view(request):
	if request.method == "POST":
		try:
			username = request.POST['username']
			password = request.POST['password']
		
			check_user = User.objects.get(user_name=username)
		except User.DoesNotExist:
			context={
				"error":"Please register yourself:)"
			}
			return render(request, 'YourNotes/login1.html', context)                            
		else:
			if check_user.user_password == password:
				#return HttpResponse("Successfully logged in:)");					#call showlist_view()
				#showlist_view(request, username);
				request.session['username'] = username
				return HttpResponseRedirect(reverse('YourNotes:notelist', args=(username,)))
			else:
				context={
					"error":"Please provide valid credentials!"
				}
				return render(request, 'YourNotes/login1.html', context)	
			#user = authenticate(request, username=username, password=password)
		#if user:
		#	login(request, user)
		#	return HttpResponse("Successfully logged in:)");
		#else:
		#	context={
		#		"error":"Please provide valid credentials!"
		#	}
		#	return render(request, 'YourNotes/login1.html', context)	
	else:
		return render(request, 'YourNotes/login1.html')

def logout_view(request):
	pass

def register_view(request):
	return render(request, 'YourNotes/registration.html')

def registerprocess_view(request):
	#return render(request, 'YourNotes/registration.html')
	if request.method == 'POST':
		try:
			username = request.POST['username']
			user_object = User.objects.get(user_name=username)
		except User.DoesNotExist:
			name = request.POST['name']
			password = request.POST['password']
			email = request.POST['email']
			new_user = User(actual_name=name, user_name=username, user_password=password, user_email = email)
			new_user.save()
			#return HttpResponse("Registration successfull:)");                                    #call showlist_view()
			#showlist_view(request, username);
			equest.session['username'] = username
			return HttpResponseRedirect(reverse('YourNotes:notelist', args=(username,)))
		else:
			context={
				"error":"Username allready exist. Please try something else!"
			}
			return render(request, 'YourNotes/registration.html', context)	
	else:
		return render(request, 'YourNotes/registration.html')
	
def showlist_view(request, username):
	#return HttpResponse("Listing your notes shortly..."+" "+username);
	#recent_note = userNotes.objects.filter(usr_name=username)
	user_object = User.objects.get(user_name=username)
	recent_note = user_object.usernotes_set.all()
	context = {
		'note_list':recent_note,
		'username':username,
		'current_date':datetime.date.today
	}
	return render(request, 'YourNotes/note_list.html', context)

def createNote_view(request, username):
	if request.method != 'POST':
		return render(request, 'YourNotes/new_note.html')
	else:
		title = request.POST['title']
		description = request.POST['description']
		due_date = request.POST['due_date']
		importance = request.POST.get('importance')
		if importance == 'on':
			imp = 1
		else:
			imp = 0
		#importance = request.POST['importance']
		q = User.objects.get(user_name=username)
		new_note = q.usernotes_set.create(note_title=title, note_detail=description, due_date=due_date, high_imp=imp)
		return render(request, 'YourNotes/new_note.html')

def deleteNote_view(request, username, title):
	select_user = User.objects.get(user_name=username)
	delete_note = select_user.usernotes_set.get(note_title=title)
	delete_note.delete()
	
	user_object = User.objects.get(user_name=username)
	recent_note = user_object.usernotes_set.all()
	
	context={
		"message":"Note removed successfully:)",
		'note_list':recent_note,
		'username':username,
		'current_date':datetime.date.today
		
	}
	return render(request, 'YourNotes/note_list.html', context)

def updateNote_view(request, username, title):
	user_object = User.objects.get(user_name=username)
	recent_note = user_object.usernotes_set.get(note_title = title)
	#print(recent_note.high_imp)
	#date = recent_note.due_date.strftime("%yyyy-%MM-%dd")
	#parsed_date = datetime.datetime.strptime(str(recent_note.due_date), "%Y-%m-%d")
	context = {
		'recent_note':recent_note,
		'username':username
	}
	return render(request, 'YourNotes/update_note.html', context)

def updateNoteprocess_view(request, username, title):
	if request.method != 'POST':
		return render(request, 'YourNotes/new_note.html')
	else:
		description = request.POST['description']
		due_date = request.POST['due_date']
		importance = request.POST.get('importance')
		status = request.POST.get('status')
		if importance == 'on':
			imp = 1
		else:
			imp = 0
		if status == 'on':
			state = 1
		else:
			state = 0	
		#importance = request.POST['importance']
		q = User.objects.get(user_name=username)
		new_note = q.usernotes_set.get(note_title=title)
		new_note.note_detail = description
		new_note.due_date = due_date
		new_note.high_imp = imp
		new_note.status = state
		new_note.save()
		#return render(request, 'YourNotes/note_list.html')
		return HttpResponseRedirect(reverse('YourNotes:notelist', args=(username,)))

	
def noteDetails_view(request, username, title):
	user_object = User.objects.get(user_name=username)
	recent_note = user_object.usernotes_set.get(note_title = title)
	context = {
		'recent_note':recent_note,
		'username':username
	}
	return render(request, 'YourNotes/note_details.html', context)

def logout_view(request):
	try:
		del request.session['username']
	except:
		pass
	return HttpResponse("<h1>You are logged out.</h1>")




