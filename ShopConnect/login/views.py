from django.shortcuts import render,redirect
from login.models import Customer,Shop_Owner
from django.contrib import messages
import re
import requests
def check_email(string):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, string)
    if match:
        return True
    else:
        return False
    
# Create your views here.

def home(request):
    return render(request,"home.html",{})



def custlogin(request):
    return render(request,"custlogin.html",{})

def custreg(request):
    return render(request,"custregister.html",{})

def clogin(request):
    mail=request.POST.get('mail') 
    password=request.POST.get('password')     
    try:
        cust=Customer.objects.get( Cust_Mail = mail , Cust_Pass = password )
        request.session['customer']=cust.id
        request.session['district']=cust.Cust_Dist
        return redirect('customer:custhome')
    except Customer.DoesNotExist:
        messages.error(request, 'Invalid email or password.')
        return render(request, 'custlogin.html',{})
    
def creg(request):
    name=request.POST.get('name')          
    mail=request.POST.get('mail')          
    phone=request.POST.get('phone')        
    password1=request.POST.get('password1')
    password=request.POST.get('password2') 
    house=request.POST.get('house')        
    road=request.POST.get('road')          
    locality=request.POST.get('locality')  
    district=request.POST.get('district')                                           
    
    if name=="" or mail=="" or phone=="" or password1=="" or password=="" or house=="" or road=="" or locality=="" or district=="":
        messages.error(request, 'Fill all fields.')
        return render(request,'custregister.html',{})
    if check_email(mail)==False:
        messages.error(request, 'Invalid email.')
        return render(request,'custregister.html',{})
    if len(phone)!=10 or phone.isalpha():
        messages.error(request, 'Invalid phone number.')
        return render(request,'custregister.html',{})
    if len(password1)<8:
        messages.error(request, 'Invalid password.')
        return render(request,'custregister.html',{})
    if password1!=password:
        messages.error(request, 'Passwords does not match.')
        return render(request,'custregister.html',{})
    
    try:
        check_cust=Customer.objects.get(Cust_Mail=mail)
        messages.error(request, 'Email already registered.')
        return render(request,'custregister.html',{})
    except Customer.DoesNotExist:
        cust=Customer(Cust_Name=name,Cust_Mail=mail,Cust_Phone=phone,Cust_Pass=password,Cust_House=house,Cust_Road=road,Cust_Locality=locality,Cust_Dist=district)
        cust.save()
        return render(request,"custlogin.html",{})




def shoplogin(request):
    return render(request,"shoplogin.html",{})

def shopreg(request):
    return render(request,"shopregister.html",{})

def slogin(request):
    mail=request.POST.get('mail')         
    password=request.POST.get('password')       
    try:
        shop=Shop_Owner.objects.get( Shop_Mail = mail , Shop_Pass = password )
        request.session['owner']=shop.id
        return redirect('owner:ownerhome')
    except Shop_Owner.DoesNotExist:
        messages.error(request, 'Invalid email or password.')
        return render(request, 'shoplogin.html',{})
        
def sreg(request):
    sname=request.POST.get('sname')                                                 
    oname=request.POST.get('oname')        
    mail=request.POST.get('mail')          
    phone=request.POST.get('phone')        
    password1=request.POST.get('password1')
    password=request.POST.get('password2') 
    road=request.POST.get('road')          
    locality=request.POST.get('locality')  
    district=request.POST.get('district')  
    if sname=="" or mail=="" or phone=="" or password1=="" or password=="" or oname=="" or road=="" or locality=="" or district=="":
        messages.error(request, 'Fill all fields.')
        return render(request,'shopregister.html',{})
    if check_email(mail)==False:
        messages.error(request, 'Invalid email.')
        return render(request,'shopregister.html',{})
    if len(phone)!=10 or phone.isalpha():
        messages.error(request, 'Invalid phone number.')
        return render(request,'shopregister.html',{})
    if len(password1)<8:
        messages.error(request, 'Invalid password.')
        return render(request,'shopregister.html',{})
    if password1!=password:
        messages.error(request, 'Passwords does not match.')
        return render(request,'shopregister.html',{})
    
    try:
        check_cust=Shop_Owner.objects.get(Shop_Mail=mail)
        messages.error(request, 'Email already registered.')
        return render(request,'shopregister.html',{})
    except Shop_Owner.DoesNotExist:
        shop=Shop_Owner(Shop_Name=sname,Shop_Mail=mail,Shop_Owner_Name=oname,Shop_Phone=phone,Shop_Pass=password,Shop_Road=road,Shop_Locality=locality,Shop_Dist=district)
        shop.save()
        return render(request,"shoplogin.html",{})