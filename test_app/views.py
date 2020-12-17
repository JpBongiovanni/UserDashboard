from django.shortcuts import render, HttpResponse, redirect
from registration_app.models import User

def admin_dashboard(request):
    context = {
        "user": User.objects.get(id = request.session['user_id']),
        "users": User.objects.all()
    }
    return render(request, "test_index.html", context)


