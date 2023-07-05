from django.shortcuts import render,redirect
from login.models import Shop_Owner,Customer
from owner.models import Shop_Item,Item
from customer.models import Bill,Bill_Items,Feedback

# Create your views here.


def ownerhome(request):
    shop_id=request.session.get('owner')
    shop=Shop_Owner.objects.filter(id=shop_id).values_list('Shop_Name',flat=True)
    shop_item=Shop_Item.objects.filter(Shop_Id=shop_id)
    item_ids = [item.Item_Id for item in shop_item]
    items = Item.objects.filter(id__in=item_ids)
    shop_items_with_names = []
    for shop_items in shop_item:
        Item_Name = items.get(id=shop_items.Item_Id).Item_Name
        shop_items_with_names.append((shop_items, Item_Name))
    
    items=Item.objects.all()
    item_var=Shop_Item.objects.filter(Shop_Id=shop_id)
    name={'name':shop,
          'shop_item':shop_items_with_names,
          'items':items,
          'item_var':item_var
          }
    return render(request,'ownerhome.html',name)

def owner_add_item(request):
    pname=request.POST.get('product-name')
    pcount=request.POST.get('product-count')
    pvol=request.POST.get('product-volume')
    pprice=request.POST.get('product-pri')
    proim= request.FILES['product-image']
    print(proim)
    ptype=request.POST.get('product-sel')
    item=Item(Item_Name=pname,Item_Photo=proim)
    item.save()
    it_id=item.id
    shop=Shop_Item(Shop_Id=request.session.get('owner'),Item_Id=it_id,Item_Quantity=pvol,Item_Count=pcount,Item_Quantity_Type=ptype,Item_Price=pprice)
    shop.save()
    
    return render(request,'ownerhome.html')

def edit_shop_item(request):
    iname=request.POST.get('pname_label')
    qty=request.POST.get('qty_input')
    vol=request.POST.get('item_vol')
    item_id=Item.objects.filter(Item_Name=iname).values_list('id',flat=True)[0]
    shop=Shop_Item.objects.filter(Shop_Id=request.session.get('owner'),Item_Id=item_id,Item_Quantity=vol)
    if qty=='0':
        shop.delete()
    else:
        for i in shop:
            i.Item_Count=qty
            i.save()
    return render(request,'ownerhome.html')

def submit_existing_item(request):
    id=request.POST.get('item_id')
    count=request.POST.get('product-count')
    vol=request.POST.get('product-volume')
    sel=request.POST.get('product-sel')
    price=request.POST.get('product-pri')
    print(id,count,vol,sel,price)
    shop=Shop_Item.objects.filter(Shop_Id=request.session.get('owner'),Item_Id = id)
    k=0
    for i in shop:
        if i.Item_Quantity==int(vol) and i.Item_Price==float(price):
            i.Item_Count+=int(count)
            i.save()
            k=1
            break
    if k==0:
        shop=Shop_Item(Shop_Id=request.session.get('owner'),Item_Id=id,Item_Quantity=vol,Item_Count=count,Item_Quantity_Type=sel,Item_Price=price)
        shop.save()
    return render(request,'ownerhome.html')

def ownerorders(request):
    shop_id=request.session.get('owner')
    bill=Bill.objects.filter(Shop_Id=shop_id,Item_Delivered='N')
    context={'bill':bill}
    return render(request,'ownerorders.html',context)

def orderdetails(request):
    bill_id = request.GET.get('bill_id')
    bill=Bill.objects.get(id=bill_id)
    bill_items=Bill_Items.objects.filter(Bill_Id=bill_id)
    shop=Shop_Owner.objects.get(id=bill.Shop_Id)
    cust=Customer.objects.get(id=bill.Cust_Id)
    context={'bill':bill,'bill_items':bill_items,'shop':shop,'cust':cust}
    return render(request,'orderdetails.html',context)

def deliver(request):
    bill_id = request.GET.get('bill_id')    
    bill=Bill.objects.get(id=bill_id)
    bill.Item_Delivered="Y"
    bill.save()
    return ownerhome(request);

def logout(request):
    del request.session['owner']
    request.session.save()
    return redirect('/')

def ownerfeedback(request):
    shop_id=request.session.get('owner')
    feedback=Feedback.objects.filter(Shop_Id=shop_id)
    context={'feedback':feedback}
    return render(request,'ownerfeedbacks.html',context)
