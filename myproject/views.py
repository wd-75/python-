
#start my function 
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages

from shop.models import Student

def services(request):
    return HttpResponse("Welcome to the services page!")


import random 
random_data = random.randint(100, 1000)





from shop.models import Student 
#student list 
def student_list(request):
    Students = Student.objects.filter(verified=True) 
    list(Students)
    print(Students)
    context ={'students': Students}
    return render(request, "student_list.html", context)

from shop.models import Product
def product_list(request):
    products = Product.objects.filter(verified=True)
    list(products)
    print(products)
    context = {'products': products}
    return render(request, "product_list.html", context)








def home(request):
    return HttpResponse(f"Random Number is {random_data}")


def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")


def shop(request):
    context ={
        "products": product_list,
        "title": "मेरो पसलम",
        "header": "मेरो पसलमा स्वागत छ",
        "description": "यहाँ तपाईंले विभिन्न प्रकारका उत्पादनहरू पाउन सक्नुहुन्छ। रमाइलो किनमेल गर्नुहोस्!",
        
    }

    return render(request, "contact.html", context)



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return redirect('contact')
    return render(request, "contact.html")
