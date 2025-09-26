from django.shortcuts import render
from django.http import HttpResponse

def student_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        age = request.POST.get("age")
        print("Student Data:", name, email, age)  # Console me print hoga
        return HttpResponse("Form submitted! Check console for data.")
    return render(request, "register/student_form.html")

# Create your views here.
