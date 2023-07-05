from django.shortcuts import render,redirect
from customer.models import Bill,Bill_Items,Cart,Feedback
from login.models import Customer,Shop_Owner
from owner.models import Shop_Item,Item
from django.contrib import messages
from datetime import date
from django.http import HttpResponseRedirect
# Create your views here.

def custhome(request):
    dist=request.session.get('district')
    print("here")
    cust_id=request.session.get('customer')
    cust=Customer.objects.get(id=cust_id)
    shop=Shop_Owner.objects.filter(Shop_Dist=dist)
    context={
        'shop':shop,
        'cust':cust
    }
    return render(request,'custhome.html',context)

def shoppage(request):
    id=request.POST.get('shop_id')
    shop=Shop_Owner.objects.filter(id=id)
    shop_items=Shop_Item.objects.filter(Shop_Id=id)
    item=Item.objects.all()
    context={}
    for shop_item in shop_items:
        item_id = shop_item.Item_Id
        item_qty=shop_item.Item_Quantity
        item_qty_type=shop_item.Item_Quantity_Type
        price=shop_item.Item_Price
        item_name = item.get(id=item_id).Item_Name
        item_photo=item.get(id=item_id).Item_Photo
        item_photo=str(item_photo).replace('static/','')
        count=shop_item.Item_Count
        data = {
            'item_id': item_id,
            'item_name': item_name,
            'quantity_type': item_qty_type,
            'quantity': item_qty,
            'price':price,
            'item_photo':item_photo,
            'count':count
        }
        context[str(item_id)+str(item_qty)+item_qty_type]=data
    return render(request,'shoppage.html',{'data':context,'shop':shop})
def addtocart(request):
    shop_id=request.POST.get('shop_id')
    item_id=request.POST.get('item_id')
    item_qty=request.POST.get('item_qty')
    item_qty_type=request.POST.get('item_qty_type')
    item_price=request.POST.get('item_price')
    count=request.POST.get('count',0)
    cust_id=request.session.get("customer")
    cart=Cart.objects.filter(Cust_Id=cust_id)
    if cart.exists():
        cart_shop=cart[0].Shop_Id
        if int(shop_id)!=int(cart_shop):
            messages.error(request, "Your cart already has items from a different seller.")
            return shoppage(request)
        else:
            cart=Cart.objects.filter(Cust_Id=cust_id,Shop_Id=shop_id,Item_Quantity=item_qty,Item_Id=item_id,Item_Quantity_Type=item_qty_type)
            if cart.exists():
                if count=='0':
                    cart.delete()
                else:
                    for i in cart:
                        i.Item_Count=int(i.Item_Count)+int(count)
                        item_price=float(item_price)*float(i.Item_Count)
                        i.Item_Price=float(item_price)
                        i.save()
            else:
                item_price=float(item_price)*int(count)
                cart=Cart(Cust_Id=cust_id,Shop_Id=shop_id,Item_Quantity=item_qty,Item_Id=item_id,Item_Quantity_Type=item_qty_type,Item_Price=item_price,Item_Count=count)
                cart.save()
    else:
        item_price=float(item_price)*int(count)
        cart=Cart(Cust_Id=cust_id,Shop_Id=shop_id,Item_Quantity=item_qty,Item_Id=item_id,Item_Quantity_Type=item_qty_type,Item_Price=item_price,Item_Count=count)
        cart.save()
    return shoppage(request)
def logout(request):
    del request.session['customer']
    request.session.save()
    return redirect('/')

def cart(request):
    cust_id=request.session.get('customer')
    carts=Cart.objects.filter(Cust_Id=cust_id)
    context={}
    cust=Customer.objects.get(id=cust_id)
    if carts.exists():
        shop_name=Shop_Owner.objects.filter(id=carts[0].Shop_Id)[0].Shop_Name
    for cart in carts:
        item=Item.objects.filter(id=cart.Item_Id)
        shop=Shop_Owner.objects.filter(id=cart.Shop_Id)
        for i in item:
            for j in shop:
                photo=str(i.Item_Photo).replace('static/','')
                data={
                    'item_id': cart.Item_Id,
                    'item_name': i.Item_Name,
                    'quantity_type': cart.Item_Quantity_Type,
                    'quantity': cart.Item_Quantity,
                    'price':cart.Item_Price,
                    'item_photo':photo,
                    'count':cart.Item_Count
                }
                context[str(cart.Item_Id)+str(cart.Item_Quantity)+cart.Item_Quantity_Type]=data
    if carts.exists():
        return render(request,'cart.html',{'data':context,'shop':shop_name,'customer':cust})
    else:
        return render(request,'cart.html',{'data':context,'customer':cust})
def edit_user_item(request):
    iname=request.POST.get('pname_label')
    qty=request.POST.get('qty_input')
    vol=request.POST.get('item_vol')
    item_id=Item.objects.filter(Item_Name=iname).values_list('id',flat=True)[0]
    cart=Cart.objects.filter(Cust_Id=request.session.get('customer'),Item_Id=item_id,Item_Quantity=vol)
    if qty=='0':
        cart.delete()
    else:
        for i in cart:
            price=float(i.Item_Price)/float(i.Item_Count)
            i.Item_Count=qty
            print(type(qty),qty)
            print(type(price),price)
            i.Item_Price=int(qty)*price
            i.save()
    return render(request,'ownerhome.html')
def clear_cart(request):
    print("heyy")
    cust_id=request.session.get('customer')
    cart=Cart.objects.filter(Cust_Id=cust_id)
    cart.delete()
    return HttpResponseRedirect("/customer/")

def buyitems(request):
    cust_id=request.session.get('customer')
    carts=Cart.objects.filter(Cust_Id=cust_id)
    shop_id=carts[0].Shop_Id
    shop=Shop_Owner.objects.get(id=shop_id)
    shop_item=Shop_Item.objects.filter(Shop_Id=shop_id)
    for i in carts:
        shop_item=Shop_Item.objects.get(Shop_Id=shop_id,Item_Id=i.Item_Id,Item_Quantity=i.Item_Quantity,Item_Quantity_Type=i.Item_Quantity_Type)
        if int(i.Item_Count)>int(shop_item.Item_Count):
            item=Item.objects.get(id=i.Item_Id).Item_Name
            messages.error(request,item+" is not available with the crrent seller in desired quantity.")
            return cart(request)
    house=request.POST.get('house_name')
    road=request.POST.get('road_name')
    locality=request.POST.get('locality')
    district=request.POST.get('district')
    print(house,road,locality,district)
    bill=Bill(Cust_Id=cust_id,Shop_Id=shop_id,Cust_House=house,Cust_Road=road,Cust_Locality=locality,Cust_Dist=district,date=date.today(),Total_Price=0,Item_Delivered="N")
    bill.save()
    total=0
    for i in carts:
        item_id=i.Item_Id
        item_name=Item.objects.get(id=item_id).Item_Name
        bill_items=Bill_Items(Item_Name=item_name,Bill_Id=bill.id,Item_Id=i.Item_Id,Item_Quantity=i.Item_Quantity,Item_Quantity_Type=i.Item_Quantity_Type,Item_Count=i.Item_Count,Item_Price=i.Item_Price)
        bill_items.save()
        shop_item=Shop_Item.objects.get(Shop_Id=shop_id,Item_Id=i.Item_Id,Item_Quantity=i.Item_Quantity,Item_Quantity_Type=i.Item_Quantity_Type)
        shop_item.Item_Count=int(shop_item.Item_Count)-int(i.Item_Count)
        if shop_item.Item_Count==0:
            shop_item.delete()
        else:
            shop_item.save()
        total+=float(i.Item_Price)
        i.delete()
    bill_items=Bill_Items.objects.filter(Bill_Id=bill.id)
    bill.Total_Price=total
    bill.save()
    cust=Customer.objects.get(id=request.session.get('customer'))

    context={'bill':bill,'bill_items':bill_items,'shop':shop, 'cust':cust}
    return render(request,'bill.html',context)

def orders(request):
    cust_id=request.session.get('customer')
    bill=Bill.objects.filter(Cust_Id=cust_id)
    return render(request,'orders.html',{'bill':bill})

def custorderdetails(request):
    cust=Customer.objects.get(id=request.session.get('customer'))
    bill_id = request.GET.get('bill_id')
    bill=Bill.objects.get(id=bill_id)
    shop=Shop_Owner.objects.get(id=bill.Shop_Id)
    bill_items=Bill_Items.objects.filter(Bill_Id=bill_id)

    context={'bill':bill,'bill_items':bill_items,'shop':shop,'cust':cust}
    return render(request,'custorderdetails.html',context)

def custfeedback(request):
    feed=request.POST.get("feedback")
    com=request.POST.get("comment")
    shop_id=request.POST.get("shop_id")
    feedback=Feedback(Cust_Id=request.session.get('customer'),Shop_Id=shop_id,Satisfaction=feed,Comment=com,Cust_Name=Customer.objects.get(id=request.session.get('customer')).Cust_Name)
    feedback.save()
    return shoppage(request)