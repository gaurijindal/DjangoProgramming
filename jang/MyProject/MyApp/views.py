from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
# from .forms import SignupForm
# from .models import Signup
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')
def success(request):
    return render(request, 'success.html')

from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()

def password_reset(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        question_1 = request.POST.get('question_1')
        answer_1 = request.POST.get('answer_1')
        question_2 = request.POST.get('question_2')
        answer_2 = request.POST.get('answer_2')
        question_3 = request.POST.get('question_3')
        answer_3 = request.POST.get('answer_3')

        try:
            user = User.objects.get(username=username)
            if (user.security_question_1 == question_1 and user.security_answer_1 == answer_1 and
                    user.security_question_2 == question_2 and user.security_answer_2 == answer_2 and
                    user.security_question_3 == question_3 and user.security_answer_3 == answer_3):
                
                messages.success(request, 'Security questions verified. You can now reset your password.')
                return redirect('password_reset_confirm')
            else:
                messages.error(request, 'Incorrect security question answers.')
        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')

    return render(request, 'password_reset.html')


# Create your views here.

# def hello(request):
#         return HttpResponse("hello")
# def home(request):
#         return HttpResponse("<body style = 'background-color : pink'><h1 style = 'color: red' > Welcome to Home Page </h1></body>")
# def hello(request):
#         return HttpResponse("""Hello I'm here!""")
# def user(request):
#         name="Gauri"
#         return HttpResponse("The Name is: "+name)
# def menuitems(request):
#         items={
#                 'Pizza': 'Costs Rs. 600',
#                 'Burger': 'Costs Rs. 120',
#                 'Noodles': 'Costs Rs. 60'
#         }
#         # return HttpResponse(items)

#         content = '<h1>Menu Items</h1>'
#         for item, description in items.items():
#                 content += f'<li>{item} : {description}</li>'
#         return HttpResponse(content)
# def greeting(request, name):
#         return HttpResponse(f"Hello! {name}, Welcome to our Website. ")
# def menuitem(request,dish):
#         items={
#                 'Pizza': 'Costs Rs. 600',
#                 'Momos': 'Costs Rs. 120',
#                 'Berger': 'Costs Rs. 60'
#         }
#         content = f'The Price of the {dish} is {items[dish]}'
#         return HttpResponse(content)
# def add(request, num1, num2):
#         result = num1 + num2
#         return HttpResponse(f'The sum of {num1} and {num2} numbers is: {result}')
# def greet(request):
#         name = request.GET.get('name')
#         age = request.GET.get('age')
#         return HttpResponse(f'Welcome! {name}, Your age is {age}.')
# def sum(request):
#         a = request.GET.get('a')
#         b = request.GET.get('b')
#         sum = int(a) + int(b)
#         return HttpResponse(f'The sum of the numbers is {sum}.')
# def calculate(request):
#         operation = request.GET.get('operation')
#         p = request.GET.get('p')
#         q = request.GET.get('q')
#         try:
#                p=float(p)
#                q=float(q)
#         except ValueError:
#                return HttpResponse("Enter a Valid number")
#         if(operation == "addition"):
#                 result = int(p) + int(q)
#         elif(operation == "subtraction"):
#                 result = int(p) - int(q)
#         elif(operation == "multiplication"):
#                 result = int(p) * int(q)
#         elif(operation == "division"):
#                 result = int(p) / int(q)
#         else:
#                 return HttpResponse(f'Enter a valid operation.')
        
#         return HttpResponse((f'The result of {operation} for {p} and {q} is {result}'))

# def user_profile(request,username):
#     return HttpResponse(f'Username is {username}')

# def items(request,item_id):
#     return HttpResponse(f'The item id is {item_id}')

# def products(request,product_id):
#     return HttpResponse(f'The product id is {product_id}')

# def post(request,post):
#     return HttpResponse(f'Post-->{post}')

# # Error Handling in Django
# def order(request, category, subcategory):
#         if (category =="" and subcategory == ""):
#                 return HttpResponse("<h1 style = 'color : orange'>Not Found</h1>", status = 404)
#         else:
#                 return HttpResponse(f'The category is {category} and subcategory is {subcategory}.')

# # Templates <DTL: Django Template Language>
# def index(request):
#        return render(request, 'index.html')
# def carte(request):
#        items = {'name': 'South Indian Cuisine'}
#        return render(request, 'carte.html', items)
# def menu(request):
#        items = {'menu':[
#               {'Name': 'Pizza', 'Cost' : 499},
#               {'Name': 'Noodles', 'Cost' : 149},
#               {'Name': 'Fries', 'Cost' : 'free'},
#               {'Name': 'Momos', 'Cost' : 99},
#        ]}
#        return render(request, 'menu.html', items)
# def eatery(request, delicacy):
#        items = {'delicacies':[
#               {'Name': 'Pizza', 'Cost' : 499},
#               {'Name': 'Noodles', 'Cost' : 149},
#               {'Name': 'Fries', 'Cost' : 'free'},
#               {'Name': 'Momos', 'Cost' : 99},
#               {'Name': 'Chutney', 'Cost' : 'free'},
#               {'Name': 'Pasta', 'Cost' : 299},
#        ]}
#        selected_item = None
#        for item in items['delicacies']:
#               if item['Name'] == delicacy:
#                      selected_item = item
#                      break
#        return render(request, 'eatery.html', {'delicacy' : selected_item})
# def homme(request):
#        return render(request, 'home.html')
# def about(request):
#        return render(request, 'about.html')
# items = [
#               {'Name': 'Garlic Naan', 'Cost' : 69, 'Details': 'Delicious Garlic flavored Indian bread.'},
#               {'Name': 'Mutton Biryani', 'Cost' : 449, 'Details': 'Aromatic Rice dish with tender Mutton pieces.'},
#               {'Name': 'Chole Bhature', 'Cost' : 49, 'Details': 'Classic North Indian dish of spicy Chickpeas with fried bread.'},
#               {'Name': 'Afghani Chicken', 'Cost' : 349, 'Details': 'Creamy and mildly spiced Chicken curry with a rich gravy.'},
#               {'Name': 'Missal Pav', 'Cost' : 199, 'Details': 'Spicy Sprouts curry served with soft bread rolls.'},
#               {'Name': 'Jalebi', 'Cost' : 149, 'Details': 'Crispy and syrupy Indian sweet made from fermented batter.'}
#        ]
# def food(request):
#        return render(request, 'food.html', {'items' : items})
# def feed(request, item):
#        singleItem = {}
#        for food in items:
#               if(food['Name'] == item):
#                      singleItem = food
#                      break
#        data = {
#                "item": singleItem
#         }
#        return render(request, 'feed.html', data)


# #Forms in Django

# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt
# def simpleform(request):
#        if request.method == 'POST':
#               textbox1 = request.POST.get('textbox1')
#               textbox2 = request.POST.get('textbox2')
#               return HttpResponse(f"The values are {textbox1} & {textbox2}")
#        else:
#               form_html = """
#               <form method = "POST">
#               <label for = "textbox1">Text Box 1:</label><br>
#               <input type = "text" id = "textbox1" name = "textbox1"><br><br>
#               <label for = "textbox2">Text Box 2:</label><br>
#               <input type = "text" id = "textbox2" name = "textbox2"><br><br>
#               <input type = "submit" value = "Submit">
#               </form>
#               """
#        return HttpResponse(form_html) 

# from django.http import HttpResponse
# from django.middleware.csrf import get_token

# def simpleforms(request):
#        csrf_token = get_token(request)
#        if request.method == 'POST':
#               textbox1 = request.POST.get('textbox1')
#               textbox2 = request.POST.get('textbox2')
#               return HttpResponse(f"The values are {textbox1} & {textbox2}")
#        else:
#               form_html = f"""
#               <form method = "POST">
#               <input type = "hidden" name = "csrfmiddlewaretoken" value = "{csrf_token}">
#               <label for = "textbox1">Text Box 1:</label><br>
#               <input type = "text" id = "textbox1" name = "textbox1"><br><br>
#               <label for = "textbox2">Text Box 2:</label><br>
#               <input type = "text" id = "textbox2" name = "textbox2"><br><br>
#               <input type = "submit" value = "Submit">
#               </form>
#               """
#        return HttpResponse(form_html) 
# def testcss(request):
#        return render(request, 'test.css.html')

# class FormView(View):
#        def get(self, request):
#               return render(request, 'forms.html')
#        def post(self, request):
#               name = request.POST.get('name')
#               email = request.POST.get('email')
#               password = request.POST.get('password')

#               if name and email and password:
#                      return HttpResponse("Form submitted successfully")
#               else:
#                      return render(request, 'forms.html')
              
# def FormViews(request):
#        errors = {
#               'name' : "",
#               'email': "",
#               'password' : ""
#        }
#        if request.method == 'GET':
#               return render(request, 'forms.html', errors)
#        if request.method == 'POST':
#               name = request.POST.get('name')
#               email = request.POST.get('email')
#               password = request.POST.get('password')
#               if name and email and password:
#                      return HttpResponse("Form submitted successfully")
#        if not name:
#               errors['name'] = "* Name is required"
#        if not email:
#               errors['email'] = "* Email is required"
#        if not password:
#               errors['password'] = "* Password is required"
#        if not name or not email or not password:
#               return render(request, 'forms.html', errors)

# def validation(request):
#     submitted_values=''
#     if request.method=='POST':
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         password=request.POST.get('password')  

#         name_error=''
#         email_error=''
#         password_error=''
        

#         if not name:
#             name_error="Name cannot be left blank"
#         if not email:
#             email_error="Email cannot be left blank"
#         if not password:
#             password_error="Password cannot be left blank"

#         # if three error are existing which we write above
#         if name_error or email_error or password_error:
#             return render(request,'validation.html',{
#                 'name':name,
#                 'email':email,
#                 'password':password,
#                 'name_eror':name_error,
#                 'email_error':email_error,
#                 'password_error':password_error
#             })
        

#         # for printing values after succesfully form submission
#         submitted_values={
#             'name':name,
#             'email':email,
#             'password':password
#         }
        
#     return render(request,'validation.html',{'submitted_values':submitted_values})
       
# from .forms import InputForm1
# def val_django_form(request):
#        submitted_details = None
#        if(request.method=='POST'):
#               form = InputForm1(request.POST)
#               if form.is_valid():
#                      submitted_details = form.cleaned_data
#                      return render(request, 'val_djando_form.html',{'form': form,'submitted_details': submitted_details})
#               else:
#                      return render(request, 'val_djando_form.html',{'form': form,'submitted_details': submitted_details})
#        else:
#               form = InputForm1()
#        return render(request, 'val_djando_form.html',{'form': form,'submitted_details': submitted_details})

# def Sign(request):
#     account_created = False
#     if(request.method == 'POST'):
#         form = SignupForm(request.POST)
#         if form.is_valid():
#                username = form.cleaned_data['username']
#                email = form.cleaned_data['email']
#                password = form.cleaned_data['password']
#                s = Signup.objects.create(username = username, email = email, password = password)
#                s.save()
#                account_created = True
#     else:
#            form = SignupForm()
#     return render(request, 'signup.html', {'form': form, 'account_created': account_created})                 
# from .forms import CustomerForm
# from .models import Customer
# def Signup(request):
#     if(request.method == 'POST'):
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#                name = form.cleaned_data['name']
#                email = form.cleaned_data['email']
#                password = form.cleaned_data['password']
#                s = Customer.objects.create(name = name, email = email, password = password)
#                s.save()
#     else:
#            form = CustomerForm()
#     return render(request, 'signup.html', {'form': form})
# #Get Cookie
# def get_cookie(request):
#        cookie_value = request.COOKIES.get('name')
#        if cookie_value:
#               return HttpResponse(f"Cookie Value: {cookie_value}")
#        else:
#               return HttpResponse("Cookie not Found!")
# #Set Cookie
# def set_cookie(request):
#        response = HttpResponse("Cookie set!")
#        response.set_cookie('name', 'django', max_age = 15)
#        return response
# #Delete Cookie
# def delete_cookie(request):
#        response = HttpResponse("Cookie deleted!")
#        response.delete_cookie('name')
#        return response
# from .models import Blogspot
# def blogspot(request):
#        post = Blogspot.objects.all()
#        return render(request, 'blogspot.html', {'post':post})
# def set_session(request):
#     request.session['username'] = 'johnsharma'
#     request.session['email'] = 'john@gmail.com'
#     return render(request, 'set_session.html')
# def get_session(request):
#     username = request.session.get('username','Guest')
#     email = request.session.get('email','guest@gmail.com')
#     return render(request, 'get_session.html',{'username':username,'email':email})
# def delete_session(request):
#     request.session.flush()
#     return render(request, 'deleted_session.html')

