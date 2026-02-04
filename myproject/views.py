
#start my function 
from django.shortcuts import HttpResponse, render, redirect
from django.contrib import messages

def services(request):
    return HttpResponse("Welcome to the services page!")


import random 
random_data = random.randint(100, 1000)

def home(request):
    return HttpResponse(f"Random Number is {random_data}")


def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")


def shop(request):
    product_list = [
    {
    "name": "Wireless Headphones",
    "price": "$49.99",
    "in_stock": True,
    "description": "High-quality wireless headphones with noise isolation.",
    "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Running Shoes",
    "price": "$79.99",
    "in_stock": True,
    "description": "Lightweight and comfortable running shoes for daily workouts.",
    "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Smart Watch",
    "price": "$99.99",
    "in_stock": False,
    "description": "Track your fitness, heart rate, and daily activities.",
    "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Backpack",
    "price": "$39.99",
    "in_stock": True,
    "description": "Durable backpack suitable for travel, college, or office use.",
    "image_url": "https://th.bing.com/th/id/OIP.WpxXdXIJyIFwa6sIbBUJMQHaHa?w=182&h=183&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3"
    },
    {
    "name": "Sunglasses",
    "price": "$19.99",
    "in_stock": True,
    "description": "Stylish UV-protected sunglasses for outdoor wear.",
    "image_url": "https://images.unsplash.com/photo-1511499767150-a48a237f0083?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Bluetooth Speaker",
    "price": "$59.99",
    "in_stock": True,
    "description": "Portable Bluetooth speaker with deep bass and clear sound.",
    "image_url": "https://m.media-amazon.com/images/I/81KehT0f84L.jpg"
    },
    {
    "name": "DSLR Camera",
    "price": "$499.99",
    "in_stock": True,
    "description": "Capture stunning photos with professional-level clarity.",
    "image_url": "https://tse3.mm.bing.net/th/id/OIP.2ewPvAlmOFp9wmJjHt3lVwHaHa?rs=1&pid=ImgDetMain&o=7&rm=3"
    },
    {
    "name": "Office Chair",
    "price": "$129.99",
    "in_stock": False,
    "description": "Ergonomic chair designed for long working hours.",
    "image_url": "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Coffee Mug",
    "price": "$9.99",
    "in_stock": True,
    "description": "Minimal ceramic mug perfect for coffee or tea.",
    "image_url": "https://images.unsplash.com/photo-1517685352821-92cf88aee5a5?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Laptop Stand",
    "price": "$24.99",
    "in_stock": False,
    "description": "Adjustable aluminum stand for better laptop ergonomics.",
    "image_url": "https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Wireless Mouse",
    "price": "$14.99",
    "in_stock": True,
    "description": "Smooth and responsive wireless mouse with ergonomic design.",
    "image_url": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Mechanical Keyboard",
    "price": "$59.99",
    "in_stock": True,
    "description": "RGB backlit mechanical keyboard with tactile switches.",
    "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "USB-C Hub",
    "price": "$29.99",
    "in_stock": False,
    "description": "Multi-port USB-C hub with HDMI, USB, and SD card slots.",
    "image_url": "https://images.unsplash.com/photo-1615750185825-fc85c6aba8b1?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Noise Cancelling Headphones",
    "price": "$89.99",
    "in_stock": False,
    "description": "Over-ear headphones with active noise cancellation.",
    "image_url": "https://images.unsplash.com/photo-1583394838336-acd977736f90?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Smartphone Tripod",
    "price": "$19.99",
    "in_stock": True,
    "description": "Flexible tripod for smartphones and small cameras.",
    "image_url": "https://images.unsplash.com/photo-1526170375885-4d8ecf77b99f?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Portable SSD",
    "price": "$99.99",
    "in_stock": True,
    "description": "High-speed portable SSD for fast data transfer.",
    "image_url": "https://images.unsplash.com/photo-1628557118391-56cd62c9f2cb?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Webcam HD",
    "price": "$39.99",
    "in_stock": False,
    "description": "1080p HD webcam for online meetings and streaming.",
    "image_url": "https://images.unsplash.com/photo-1580894908360-7bdfc3a66e35?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Bluetooth Speaker",
    "price": "$34.99",
    "in_stock": True,
    "description": "Compact Bluetooth speaker with powerful bass.",
    "image_url": "https://images.unsplash.com/photo-1585386959984-a4155224a1ad?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Wireless Charger",
    "price": "$22.99",
    "in_stock": False,
    "description": "Fast wireless charging pad for smartphones.",
    "image_url": "https://images.unsplash.com/photo-1618410320607-dbb2c4a9db6b?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Laptop Backpack",
    "price": "$49.99",
    "in_stock": True,
    "description": "Water-resistant backpack with padded laptop compartment.",
    "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "MacBook Air M1",
    "price": "$899.99",
    "in_stock": True,
    "description": "Lightweight laptop with Apple M1 chip and long battery life.",
    "image_url": "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Dell XPS 13",
    "price": "$999.99",
    "in_stock": False,
    "description": "Premium Ultrabook with InfinityEdge display.",
    "image_url": "https://images.unsplash.com/photo-1593642634315-48f5414c3ad9?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "HP Pavilion Laptop",
    "price": "$649.99",
    "in_stock": True,
    "description": "Powerful everyday laptop for work and study.",
    "image_url": "https://images.unsplash.com/photo-1587614382346-ac8c9b2f0c68?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Lenovo ThinkPad X1",
    "price": "$1099.99",
    "in_stock": True,
    "description": "Business-class laptop with durable build.",
    "image_url": "https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Asus ROG Gaming Laptop",
    "price": "$1299.99",
    "in_stock": True,
    "description": "High-performance gaming laptop with RGB keyboard.",
    "image_url": "https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Acer Aspire 5",
    "price": "$579.99",
    "in_stock": True,
    "description": "Affordable laptop with solid performance.",
    "image_url": "https://images.unsplash.com/photo-1588702547923-7093a6c3ba33?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Microsoft Surface Laptop",
    "price": "$999.99",
    "in_stock": False,
    "description": "Sleek design with high-resolution touchscreen.",
    "image_url": "https://images.unsplash.com/photo-1611078489935-0cb964de46d6?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Samsung Galaxy Book",
    "price": "$749.99",
    "in_stock": True,
    "description": "Slim laptop optimized for Samsung ecosystem.",
    "image_url": "https://images.unsplash.com/photo-1593642702821-c8da6771f0c6?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "iPhone 14",
    "price": "$799.99",
    "in_stock": True,
    "description": "Apple smartphone with advanced camera system.",
    "image_url": "https://images.unsplash.com/photo-1661961112951-f2bfd72e0d3c?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "iPhone 13",
    "price": "$699.99",
    "in_stock": False,
    "description": "Powerful iPhone with A15 Bionic chip.",
    "image_url": "https://images.unsplash.com/photo-1632661674596-df8be070a5c5?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Samsung Galaxy S23",
    "price": "$749.99",
    "in_stock": False,
    "description": "Flagship Android phone with stunning display.",
    "image_url": "https://images.unsplash.com/photo-1678911820864-e2c567c655d7?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Samsung Galaxy A54",
    "price": "$399.99",
    "in_stock": True,
    "description": "Mid-range smartphone with premium features.",
    "image_url": "https://images.unsplash.com/photo-1605787020600-b9ebd5df1d07?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "OnePlus 11",
    "price": "$699.99",
    "in_stock": False,
    "description": "Fast and smooth performance with AMOLED display.",
    "image_url": "https://images.unsplash.com/photo-1616348436168-de43ad0db179?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Google Pixel 7",
    "price": "$599.99",
    "in_stock": True,
    "description": "Clean Android experience with excellent camera.",
    "image_url": "https://images.unsplash.com/photo-1665003996020-dc0f9c0aeb5a?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Xiaomi Redmi Note 12",
    "price": "$249.99",
    "in_stock": True,
    "description": "Budget-friendly phone with big display.",
    "image_url": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Realme GT Neo",
    "price": "$329.99",
    "in_stock": True,
    "description": "Performance-focused smartphone at affordable price.",
    "image_url": "https://images.unsplash.com/photo-1621330396173-e41b1cafd17f?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Oppo Reno 8",
    "price": "$449.99",
    "in_stock": True,
    "description": "Stylish smartphone with fast charging.",
    "image_url": "https://images.unsplash.com/photo-1604671368394-2240d0b1bb6c?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Vivo V27",
    "price": "$379.99",
    "in_stock": True,
    "description": "Camera-focused smartphone with sleek design.",
    "image_url": "https://images.unsplash.com/photo-1580910051074-7a9c2f41d1db?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Motorola Edge 40",
    "price": "$499.99",
    "in_stock": True,
    "description": "Curved display phone with clean Android UI.",
    "image_url": "https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?auto=format&fit=crop&w=600&q=80"
    },
    {
    "name": "Nokia G60",
    "price": "$299.99",
    "in_stock": True,
    "description": "Reliable smartphone with strong build quality.",
    "image_url": "https://images.unsplash.com/photo-1605236453806-6ff36851218e?auto=format&fit=crop&w=600&q=80"
    },
    ]

    # return HttpResponse(f"<h1>Welcome to the shop page! </h1><P>Enjoy your shopping.</P> <h2> products <h2>{product_list}")
    # return render(request, "index.html", {})

    context ={
        "products": product_list,
        "title": "मेरो पसलम",
        "header": "मेरो पसलमा स्वागत छ",
        "description": "यहाँ तपाईंले विभिन्न प्रकारका उत्पादनहरू पाउन सक्नुहुन्छ। रमाइलो किनमेल गर्नुहोस्!",
        
    }

    return render(request, "index.html", context)



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        messages.success(request, 'Thank you for contacting us! We will get back to you soon.')
        return redirect('contact')
    return render(request, "contact.html")