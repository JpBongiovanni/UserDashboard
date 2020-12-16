from django.shortcuts import render, HttpResponse, redirect

def admin_dashboard(request):
    return render(request, "test_index.html")


