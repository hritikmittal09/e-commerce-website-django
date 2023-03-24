from django.shortcuts import render,redirect
from .models import post
from.models import User
from time import sleep
import uuid
cart =None
import json
cart = None 
user_cart_id =None
log_in = 0
total_price = 0

try:
    with open("cart.json") as f:
        cart = json.load(f)    
except Exception as e:
    cart = dict()
    with open("cart.json",'w')as f:
        json.dump(cart, f)

message = ""

def home(request):
    global log_in
    log_in =1
    data ={"posts":post.objects.all()}
    return  render(request, "home.html",data)


def product_view(request,product_id):
    product_details =post.objects.get(id = product_id)
    data = {"product_details": product_details}
    return render(request, "product_view.html",data)
def login(req):
    global message
    
    return render(req, "login.html", {"message":message})
def signup(req):
    message =""
    if req.method == "POST":
        user = req.POST["name"]
        password = req.POST["password"]
        email = req.POST["email"]
        if User.objects.filter(email=email).exists():
            message = "user with same email exist"
        else:

            new_cart_id = str(uuid.uuid1())
            with open("cart.json") as f:
                cart = json.load(f)
            cart[new_cart_id] = dict()
            with open("cart.json","w") as f:
                json.dump(cart, f)

            data = User(full_name=user,email=email,password=password,cart_id=new_cart_id)
            data.save()
            message = "login successful"

      
    return render(req, "signup.html", {"message":message})

def checkcadentails(req):
    if req.method == "POST":
        email = req.POST["email"]
        input_password = req.POST["password"]
        if User.objects.filter(email=email).exists():
            user_email = User.objects.get(email=email)
            global user_cart_id
            user_cart_id = user_email.cart_id
            password = user_email.password
            with open("cart.json") as f:
                global cart
                cart = json.load(f)
                if input_password != password:
                    return render(req, "error.html", {"message" : "Email or password is incorrect"})

            
                
            
            return redirect("/shop")
        else:
            global message
            message = "account not exist"
            return redirect("/")


def add_cart(req, product, product_prize):
    if req.method == "GET":
        return render(req, "error.html",{"message": "click on show cart"})
    global log_in
    if log_in ==1:
        if product_prize :
            global cart,total_price
            total_price =0
            global user_cart_id
            data = cart[user_cart_id]
            if product not in data:
                data[product] ={"name": product,"price": int(product_prize), "qty": 1}
            else:
                data[product]["qty"] = data[product]["qty"] +1    
            
            
            with open("cart.json" ,"w") as f:
                json.dump(cart, f)
            cart_products = data.keys()
            for i in data.values():
                total_price = total_price + i["price"] * i["qty"]
            qtys = []
            for i in data.values():
                qtys .append(i["qty"])
            

                


        return render(req, "cart.html", { "total_price": total_price , "product_to_qty" : zip(list (cart_products),qtys) })            
    else:
        return render(req, "error.html")            



def cart_show(req  ):
    if req.method == "POST":
        return render(req, "error.html",{"message": "click on show cart"})
    global log_in
    if log_in ==1:
        if True:
            global cart,total_price
            total_price =0
            global user_cart_id
            data = cart[user_cart_id]
           
            
        
            cart_products = data.keys()
            for i in data.values():
                total_price = total_price + i["price"] * i["qty"]
            qtys = []
            for i in data.values():
                qtys .append(i["qty"])
            return render(req, "cart.html", { "total_price": total_price , "product_to_qty" : zip(list (cart_products),qtys) })          
               
    else:
        return render(req, "error.html",{"message": "login first"})            
            
def delete(req,product):
    global log_in,cart,user_cart_id
    if log_in ==1:
        data = cart[user_cart_id]
        del data[product]
        with open("cart.json","w") as f:
            json.dump(cart, f)
        return redirect("/cart_show")    
    
    else:
        return render(req, "error.html", {"message": "login first"})
def payment_sucess(req):
    global log_in,cart,user_cart_id
    if log_in == 1:
        cart[user_cart_id] = dict()
        with open("cart.json", "w") as f:
            json.dump(cart, f)
        return render(req,"payment_sucess.html" )
    else:
        return render(req, "error.html", {"message": "login first to make payment"})        

            
                
  
                


# Create your views here.
