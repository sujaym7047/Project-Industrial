from django.shortcuts import render,redirect
from django.http import HttpResponse
from Blood_Bank_Management_System.models import *

# Create your views here.

def home_page(request):
    return render(request, 'home_page.html')


'''def admin_home(request):
    data=request.GET.get('blood_group')
    if data=='A+':
        values=User23.objects.all().values_list('blood',flat=True)
        sum_of_values=sum(values)
        return render(request,'admin_home.html',{'sum_of_values':sum_of_values})
    elif data=='B+':
        values=User24.objects.all().values_list('blood',flat=True)
        sum_of_values=sum(values)
        return render(request,'admin_home.html',{'sum_of_values':sum_of_values})'''

def admin_home(request):
    '''sum_of_values1=sum(User31.objects.filter(blood_group="A+").values_list('blood_volume',flat=True))
    sum_of_values2=sum(User31.objects.filter(blood_group="B+").values_list('blood_volume',flat=True))
    sum_of_values3=sum(User31.objects.filter(blood_group="O+").values_list('blood_volume',flat=True))
    sum_of_values4=sum(User31.objects.filter(blood_group="AB+").values_list('blood_volume',flat=True))
    sum_of_values5=sum(User31.objects.filter(blood_group="A-").values_list('blood_volume',flat=True))
    sum_of_values6=sum(User31.objects.filter(blood_group="B-").values_list('blood_volume',flat=True))
    sum_of_values7=sum(User31.objects.filter(blood_group="O-").values_list('blood_volume',flat=True))
    sum_of_values8=sum(User31.objects.filter(blood_group="AB-").values_list('blood_volume',flat=True))

    obj=User33.objects.get(id=1)'''

    

    v1=User30.objects.get(pk=1).blood_groupA1
    v2=User30.objects.get(pk=1).blood_groupB1
    v3=User30.objects.get(pk=1).blood_groupO1
    v4=User30.objects.get(pk=1).blood_groupAB1
    v5=User30.objects.get(pk=1).blood_groupA2
    v6=User30.objects.get(pk=1).blood_groupB2
    v7=User30.objects.get(pk=1).blood_groupO2
    v8=User30.objects.get(pk=1).blood_groupAB2

    v9=User33.objects.get(pk=1).blood_groupA1
    v10=User33.objects.get(pk=1).blood_groupB1
    v11=User33.objects.get(pk=1).blood_groupO1
    v12=User33.objects.get(pk=1).blood_groupAB1
    v13=User33.objects.get(pk=1).blood_groupA2
    v14=User33.objects.get(pk=1).blood_groupB2
    v15=User33.objects.get(pk=1).blood_groupO2
    v16=User33.objects.get(pk=1).blood_groupAB2

    sum_of_values20=sum(User31.objects.values_list('blood_volume',flat=True))
   

    obj=User33.objects.get(id=1)
    obj.total_blood_unit=sum_of_values20
    obj.save()

    
    if v9<=v1 or v10<=v2 or v11<=v3 or v12<=v4 or v13<=v5 or v14<=v6 or v15<=v7 or v16<=v8:
        u=User33.objects.all()
        total_request=User20.objects.count()
        return render(request,'admin_home.html',{'u':u})
        
    else:
        u=User30.objects.all()
        return render(request,'admin_home.html',{'u':u})

    #u=User30.objects.all()
    #return render(request,'admin_home.html',{'u':u})
    #return render(request, 'admin_home.html')

def user_home(request):
    return render(request, 'user_home.html')

def admin_login(request):
    return render(request, 'admin_login.html')

def user_login(request):
    return render(request, 'user_login.html')

def user_login3(request):
    return render(request, 'user_login3.html')

'''def log5(request):
    a=request.GET['a1']
    b=request.GET['a2']
    if User14.objects.filter(user_name=a,pwd=b):
        u=User30.objects.all()
        return render(request,'admin_home.html',{'u':u})
        #return render(request,'admin_home.html')
    else:
        return render(request,'admin_login.html')'''

def log5(request):
    a=request.GET['a1']
    b=request.GET['a2']
    if User14.objects.filter(user_name=a,pwd=b):

        '''sum_of_values1=sum(User31.objects.filter(blood_group="A+").values_list('blood_volume',flat=True))
        sum_of_values2=sum(User31.objects.filter(blood_group="B+").values_list('blood_volume',flat=True))
        sum_of_values3=sum(User31.objects.filter(blood_group="O+").values_list('blood_volume',flat=True))
        sum_of_values4=sum(User31.objects.filter(blood_group="AB+").values_list('blood_volume',flat=True))
        sum_of_values5=sum(User31.objects.filter(blood_group="A-").values_list('blood_volume',flat=True))
        sum_of_values6=sum(User31.objects.filter(blood_group="B-").values_list('blood_volume',flat=True))
        sum_of_values7=sum(User31.objects.filter(blood_group="O-").values_list('blood_volume',flat=True))
        sum_of_values8=sum(User31.objects.filter(blood_group="AB-").values_list('blood_volume',flat=True))

        obj=User33.objects.get(id=1)'''

        v1=User30.objects.get(pk=1).blood_groupA1
        v2=User30.objects.get(pk=1).blood_groupB1
        v3=User30.objects.get(pk=1).blood_groupO1
        v4=User30.objects.get(pk=1).blood_groupAB1
        v5=User30.objects.get(pk=1).blood_groupA2
        v6=User30.objects.get(pk=1).blood_groupB2
        v7=User30.objects.get(pk=1).blood_groupO2
        v8=User30.objects.get(pk=1).blood_groupAB2

        v9=User33.objects.get(pk=1).blood_groupA1
        v10=User33.objects.get(pk=1).blood_groupB1
        v11=User33.objects.get(pk=1).blood_groupO1
        v12=User33.objects.get(pk=1).blood_groupAB1
        v13=User33.objects.get(pk=1).blood_groupA2
        v14=User33.objects.get(pk=1).blood_groupB2
        v15=User33.objects.get(pk=1).blood_groupO2
        v16=User33.objects.get(pk=1).blood_groupAB2


        if v9<=v1 or v10<=v2 or v11<=v3 or v12<=v4 or v13<=v5 or v14<=v6 or v15<=v7 or v16<=v8:
            u=User33.objects.all()
            return render(request,'admin_home.html',{'u':u})
        else:
            u=User30.objects.all()
            return render(request,'admin_home.html',{'u':u})
            #return render(request,'admin_home.html')'''

    else:
        return render(request,'admin_login.html')


'''def log5(request):
    a=request.GET['a1']
    b=request.GET['a2']
    if User14.objects.filter(user_name=a,pwd=b):
        sum_of_values1=sum(User31.objects.filter(blood_group="A+").values_list('blood_volume',flat=True))
        sum_of_values2=sum(User31.objects.filter(blood_group="B+").values_list('blood_volume',flat=True))
        sum_of_values3=sum(User31.objects.filter(blood_group="O+").values_list('blood_volume',flat=True))
        sum_of_values4=sum(User31.objects.filter(blood_group="AB+").values_list('blood_volume',flat=True))
        sum_of_values5=sum(User31.objects.filter(blood_group="A-").values_list('blood_volume',flat=True))
        sum_of_values6=sum(User31.objects.filter(blood_group="B-").values_list('blood_volume',flat=True))
        sum_of_values7=sum(User31.objects.filter(blood_group="O-").values_list('blood_volume',flat=True))
        sum_of_values8=sum(User31.objects.filter(blood_group="AB-").values_list('blood_volume',flat=True))
        u=User30.objects.all()
        return render(request,'admin_home.html',{'u':u})
        obj=User30.objects.get(id=1)
        obj.blood_groupA1=sum_of_values1
        obj.blood_groupB1=sum_of_values2
        obj.blood_groupO1=sum_of_values3
        obj.blood_groupAB1=sum_of_values4
        obj.blood_groupA2=sum_of_values5
        obj.blood_groupB2=sum_of_values6
        obj.blood_groupO2=sum_of_values7
        obj.blood_groupAB2=sum_of_values8
        obj.save()
    else:
        return render(request,'admin_login.html')'''




'''def log5(request):
    a=request.GET['a1']
    b=request.GET['a2']
    if User14.objects.filter(user_name=a,pwd=b):
        data=request.GET.get('blood_group')
        if data=='A+':
            values=User23.objects.all().values_list('blood',flat=True)
            sum_of_values=sum(values)
            return render(request,'admin_home.html',{'sum_of_values':sum_of_values})
        elif data=='B+':
            values=User24.objects.all().values_list('blood',flat=True)
            sum_of_values=sum(values)
            return render(request,'admin_home.html',{'sum_of_values':sum_of_values})
    else:
        return render(request,'admin_login.html')'''

'''def log6(request):
    a=request.GET['a5']
    b=request.GET['a6']
    if User15.objects.filter(user_name=a,pwd=b):
        u=User15.objects.get(user_name=a,pwd=b)
        return render(request,'user_home.html',{'u':u})
    else:
        return render(request,'user_login.html')'''

def ins8(request):
    u=User15()
    u.user_name=request.GET["a7"]
    u.pwd=request.GET["a8"]
    u.save()
    return render(request,"user_login3.html") 


def user_blood_request(request):
    u=User20.objects.all()
    return render(request,'user_blood_request.html',{'u':u})


def user_make_request(request):
    return render(request, 'user_make_request.html')

def button_change(request):
    return render(request, 'button_change.html')

'''def ins1(request):
    u=User20()
    u.name=request.GET["a1"]
    u.age=request.GET["a2"]
    u.reason=request.GET["a3"]
    u.blood_group=request.GET["a4"]
    u.blood_volume=request.GET["a5"]
    u.save()'''

def ins1(request):
    u=User20()
    u.name=request.GET["a1"]
    u.age=request.GET["a2"]
    u.reason=request.GET["a3"]
    u.blood_group=request.GET["a4"]
    u.blood_volume=request.GET["a5"]
    u.save()
    record_count=User32.objects.count()
    if record_count>0:
        source_value=User20.objects.values_list('blood_group',flat=True).first()
        source_value1=User20.objects.values_list('blood_volume',flat=True).first()
        obj=User32.objects.get(id=10)
        obj.blood_group=source_value
        obj.blood_volume=source_value1
        obj.save()
    else:
        source_records=User20.objects.all()
        for record in source_records:
            destination_record=User32(
            blood_group=record.blood_group,
            blood_volume=record.blood_volume
        )
        destination_record.save()
    return render(request,"user_home.html")

def user_request_history(request):
    u=User20.objects.all()
    return render(request,'user_request_history.html',{'u':u})

'''def insert_data(request, source_id):
    source_data=User20.objects.get(pk=source_id)
    User21.objects.create(
        name=source_data.name,
        age=source_data.age,
        reason=source_data.reason,
        blood_group=source_data.blood_group,
        blood_volume=source_data.blood_volume
    )
    source_data.delete() 
    record_count=User32.objects.count()
    if record_count>0:
        source_value=User20.objects.values_list('blood_group',flat=True).first()
        source_value1=User20.objects.values_list('blood_volume',flat=True).first()
        obj=User32.objects.get(id=10)
        obj.blood_group=source_value
        obj.blood_volume=source_value1
        obj.save()
    else:
        source_records=User20.objects.all()
        for record in source_records:
            destination_record=User32(
            blood_group=record.blood_group,
            blood_volume=record.blood_volume
        )
        destination_record.save()
    return redirect("../user_blood_request")'''

#down code important
'''def insert_data(request, source_id):
    queryset=User28.objects.all()
    queryset1=User29.objects.all()
    if User29.objects.filter(blood_group="A+"): 
        for obj in queryset:
            for obj1 in queryset1:
                if obj.blood_group1<=0 or obj.blood_group1<obj1.blood:
                    return render(request,'home_page.html')
    elif User29.objects.filter(blood_group="B+"):
        for obj in queryset:
            for obj1 in queryset1:
                if obj.blood_group2<=0 or obj.blood_group2<obj1.blood:
                    return render(request, 'home_page.html')
    else:
        source_data=User20.objects.get(pk=source_id)
        User21.objects.create(
        name=source_data.name,
        age=source_data.age,
        reason=source_data.reason,
        blood_group=source_data.blood_group,
        blood_volume=source_data.blood_volume
        )
        source_data.delete() 
        return redirect("../user_blood_request")'''

'''def insert_data(request, source_id):
    queryset=User28.objects.all()
    queryset1=User20.objects.all()
    for obj in queryset:
        for obj1 in queryset1:
            if User20.objects.filter(blood_group="A+"):
                if obj.blood_group1<=0 or obj.blood_group1<obj1.blood_volume:
                    return render(request,'home_page.html')
            elif User20.objects.filter(blood_group="B+"):
                if obj.blood_group2<=0 or obj.blood_group2<obj1.blood_volume:
                    return render(request, 'home_page.html')
            else:
                source_data=User20.objects.get(pk=source_id)
                User21.objects.create(
                    name=source_data.name,
                    age=source_data.age,
                    reason=source_data.reason,
                    blood_group=source_data.blood_group,
                    blood_volume=source_data.blood_volume
                )
                source_data.delete() 
                return redirect("../user_blood_request")'''

'''def insert_data(request, source_id):
    source_value=User20.objects.values_list('blood_group',flat=True).first()
    source_value1=User20.objects.values_list('blood_volume',flat=True).first()
    obj=User32.objects.get(id=10)
    obj.blood_group=source_value
    obj.blood_volume=source_value1
    obj.save()
    value1=User30.objects.get(pk=1).blood_groupA1
    value2=User30.objects.get(pk=1).blood_groupB1
    value3=User30.objects.get(pk=1).blood_groupO1
    value4=User30.objects.get(pk=1).blood_groupAB1
    value5=User30.objects.get(pk=1).blood_groupA2
    value6=User30.objects.get(pk=1).blood_groupB2
    value7=User30.objects.get(pk=1).blood_groupO2
    value8=User30.objects.get(pk=1).blood_groupAB2
    value9=User32.objects.get(pk=10).blood_volume
    data1=User32.objects.filter(blood_group="A+")
    data2=User32.objects.filter(blood_group="B+")
    data3=User32.objects.filter(blood_group="O+")
    data4=User32.objects.filter(blood_group="AB+")
    data5=User32.objects.filter(blood_group="A-")
    data6=User32.objects.filter(blood_group="B-")
    data7=User32.objects.filter(blood_group="O-")
    data8=User32.objects.filter(blood_group="AB-")
    if data1:
        if value1==0 or value1<value9:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete() 
            value1=User30.objects.get(pk=1).blood_groupA1
            queryset=User32.objects.all()
            for obj in queryset:
                if obj.blood_group=='A+':
                    result1=value1 - value9
                    obj=User30.objects.get(id=1)
                    obj.blood_groupA1=result1
                    obj.save()
                else:
                    return redirect("../user_blood_request")
            return redirect("../user_blood_request")
    elif data2:
        if value2==0 or value2<value9:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete() 
            value2=User30.objects.get(pk=1).blood_groupB1
            queryset=User32.objects.all()
            for obj in queryset:
                if obj.blood_group=='B+':
                    result2=value2 - value9
                    obj=User30.objects.get(id=1)
                    obj.blood_groupB1=result2
                    obj.save()
                else:
                    return redirect("../user_blood_request")
            return redirect("../user_blood_request")
    elif data3:
        if value3==0 or value3<value9:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            value3=User30.objects.get(pk=1).blood_groupO1
            queryset=User32.objects.all()
            for obj in queryset:
                if obj.blood_group=='O+':
                    result3=value3 - value9
                    obj=User30.objects.get(id=1)
                    obj.blood_groupO1=result3
                    obj.save()
                else:
                    return redirect("../user_blood_request")
            return redirect("../user_blood_request")
    elif data4:
        if value4==0 or value4<value9:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete() 
            value4=User30.objects.get(pk=1).blood_groupAB1
            queryset=User32.objects.all()
            for obj in queryset:
                if obj.blood_group=='AB+':
                    result4=value4 - value9
                    obj=User30.objects.get(id=1)
                    obj.blood_groupAB1=result4
                    obj.save()
                else:
                    return redirect("../user_blood_request")
            return redirect("../user_blood_request")
    elif data5:
        if value5==0 or value5<value9:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete() 
            value5=User30.objects.get(pk=1).blood_groupA2
            queryset=User32.objects.all()
            for obj in queryset:
                if obj.blood_group=='A-':
                    result5=value5 - value9
                    obj=User30.objects.get(id=1)
                    obj.blood_groupA2=result5
                    obj.save()
                else:
                    return redirect("../user_blood_request")
            return redirect("../user_blood_request")
    elif data6:
        if value6==0 or value6<value9:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete() 
            value6=User30.objects.get(pk=1).blood_groupB2
            queryset=User32.objects.all()
            for obj in queryset:
                if obj.blood_group=='B-':
                    result6=value6 - value9
                    obj=User30.objects.get(id=1)
                    obj.blood_groupB2=result6
                    obj.save()
                else:
                    return redirect("../user_blood_request")
            return redirect("../user_blood_request")
    elif data7:
        if value7==0 or value7<value9:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete() 
            value7=User30.objects.get(pk=1).blood_groupO2
            queryset=User32.objects.all()
            for obj in queryset:
                if obj.blood_group=='O-':
                    result7=value7 - value9
                    obj=User30.objects.get(id=1)
                    obj.blood_groupO2=result7
                    obj.save()
                else:
                    return redirect("../user_blood_request")
            return redirect("../user_blood_request")
    elif data8:
        if value8==0 or value8<value9:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete() 
            value8=User30.objects.get(pk=1).blood_groupAB2 
            queryset=User32.objects.all()
            for obj in queryset:
                if obj.blood_group=='AB-':
                    result8=value8 - value9
                    obj=User30.objects.get(id=1)
                    obj.blood_groupAB2=result8
                    obj.save()
                else:
                    return redirect("../user_blood_request")
            return redirect("../user_blood_request")'''
    
    #return redirect("../user_blood_request")'''

#important****code down
def insert_data(request, source_id):
    value1=User33.objects.values_list('blood_groupA1',flat=True).first() 
    value2=User33.objects.get(pk=1).blood_groupB1
    value3=User33.objects.get(pk=1).blood_groupO1
    value4=User33.objects.get(pk=1).blood_groupAB1
    value5=User33.objects.get(pk=1).blood_groupA2
    value6=User33.objects.get(pk=1).blood_groupB2
    value7=User33.objects.get(pk=1).blood_groupO2
    value8=User33.objects.get(pk=1).blood_groupAB2
    value10=User20.objects.filter(blood_group="A+").values_list('blood_volume',flat=True).first()
    value11=User20.objects.filter(blood_group="B+").values_list('blood_volume',flat=True).first()
    value12=User20.objects.filter(blood_group="O+").values_list('blood_volume',flat=True).first()
    value13=User20.objects.filter(blood_group="AB+").values_list('blood_volume',flat=True).first()
    value14=User20.objects.filter(blood_group="A-").values_list('blood_volume',flat=True).first()
    value15=User20.objects.filter(blood_group="B-").values_list('blood_volume',flat=True).first()
    value16=User20.objects.filter(blood_group="O-").values_list('blood_volume',flat=True).first()
    value17=User20.objects.filter(blood_group="AB-").values_list('blood_volume',flat=True).first()
    data1=User20.objects.filter(blood_group="A+")
    data2=User20.objects.filter(blood_group="B+")
    data3=User20.objects.filter(blood_group="O+")
    data4=User20.objects.filter(blood_group="AB+")
    data5=User20.objects.filter(blood_group="A-")
    data6=User20.objects.filter(blood_group="B-")
    data7=User20.objects.filter(blood_group="O-")
    data8=User20.objects.filter(blood_group="AB-")
    if data1:
        if value1==0 or value1<value10:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else: 
            result1=value1 - value10
            obj=User33.objects.get(id=1)
            obj.blood_groupA1=result1
            obj.save()
            negative_value = -value10
            my_object=User31.objects.create(
                blood_group=User20.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value
            )
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_blood_request")
    elif data2:
        if value2==0 or value2<value11:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result2=value2 - value11
            obj=User33.objects.get(id=1)
            obj.blood_groupB1=result2
            obj.save()
            negative_value1 = -value11
            my_object=User31.objects.create(
                blood_group=User20.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value1
            )
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_blood_request")
    elif data3:
        if value3==0 or value3<value12:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result3=value3 - value12
            obj=User33.objects.get(id=1)
            obj.blood_groupO1=result3
            obj.save()
            negative_value2 = -value12
            my_object=User31.objects.create(
                blood_group=User20.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value2
            )
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_blood_request")
    elif data4:
        if value4==0 or value4<value13:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result4=value4 - value13
            obj=User33.objects.get(id=1)
            obj.blood_groupAB1=result4
            obj.save()
            negative_value3 = -value13
            my_object=User31.objects.create(
                blood_group=User20.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value3
            )
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_blood_request")
    elif data5:
        if value5==0 or value5<value14:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result5=value5 - value14
            obj=User33.objects.get(id=1)
            obj.blood_groupA2=result5
            obj.save()
            negative_value4 = -value14
            my_object=User31.objects.create(
                blood_group=User20.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value4
            )
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_blood_request")
    elif data6:
        if value6==0 or value6<value15:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result6=value6 - value15
            obj=User33.objects.get(id=1)
            obj.blood_groupB2=result6
            obj.save()
            negative_value5 = -value15
            my_object=User31.objects.create(
                blood_group=User20.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value5
            )
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_blood_request")
    elif data7:
        if value7==0 or value7<value16:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result7=value7 - value16
            obj=User33.objects.get(id=1)
            obj.blood_groupO2=result7
            obj.save()
            negative_value6 = -value16
            my_object=User31.objects.create(
                blood_group=User20.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value6
            )
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_blood_request")
    elif data8:
        if value8==0 or value8<value17:
            u=User20.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result8=value8 - value17
            obj=User33.objects.get(id=1)
            obj.blood_groupAB2=result8 
            obj.save()
            negative_value7 = -value17
            my_object=User31.objects.create(
                blood_group=User20.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value7
            )
            source_data=User20.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_blood_request")

def user_request_accepted(request):
    u=User21.objects.all()
    return render(request,'user_request_accepted.html',{'u':u})

def user_request_rejected(request):
    u=User34.objects.all()
    return render(request,'user_request_rejected.html',{'u':u})

'''def log6(request):
    a=request.GET['a5']
    b=request.GET['a6']
    if User21.objects.filter(name=a):
        u=User21.objects.filter(name=a)
        return render(request,'user_request_accepted.html',{'u':u}) 
    else:
        return render(request,'user_login.html')'''


def log6(request):
    a=request.GET['a5']
    b=request.GET['a6']
    if User15.objects.filter(user_name=a,pwd=b):
        #if User21.objects.filter(name=a):
        return render(request,'user_make_request.html') 
        #else:
            #return render(request,'user_login.html')
    else:
        return render(request,'user_login3.html')

def log20(request):
    a=request.GET['a5']
    b=request.GET['a6']
    if User15.objects.filter(user_name=a,pwd=b):
        #if User21.objects.filter(name=a):
        u=User21.objects.filter(name=a)
        return render(request,'user_request_accepted.html',{'u':u}) 
        #else:
            #return render(request,'user_login.html')
    else:
        return render(request,'user_login.html')

    

def user_login1(request):
    return render(request, 'user_login1.html')

def user_login2(request):
    return render(request, 'user_login2.html')

'''def log7(request):
    a=request.GET['a5']
    b=request.GET['a6']
    if User20.objects.filter(name=a):
        u=User20.objects.filter(name=a)
        return render(request,'user_request_history.html',{'u':u}) 
    else:
        return render(request,'user_login1.html')'''

def log7(request):
    a=request.GET['a5']
    b=request.GET['a6']
    if User15.objects.filter(user_name=a,pwd=b):
        #if User20.objects.filter(name=a):
        u=User20.objects.filter(name=a)
        return render(request,'user_request_history.html',{'u':u}) 
        #else:
            #return render(request,'user_login1.html')
    else:
        return render(request,'user_login1.html')

def insert4(request):
    return render(request, 'insert4.html')

def ins21(request):
    u=User23()
    u.blood_group=request.GET["a1"]
    u.blood=request.GET["a2"]
    u.save()
    return render(request,"insert4.html")

'''def calculate_sum1(request,blood_group):
    donors_with_blood_group=User23.objects.filter(blood_group=blood_group)
    sum_of_donations=sum(donor.blood for donor in donors_with_blood_group)
    return render(request,'admin_home.html',{'blood_group':blood_group,'sum_of_donations':sum_of_donations})'''

def popup(request):
    return render(request, 'popup.html')

def admin_blood_stock(request):
    return render(request,'admin_blood_stock.html')

def ins30(request):
    u=User31()
    u.blood_group=request.GET["a1"]
    u.blood_volume=request.GET["a2"]
    u.save()

    sum_of_values1=sum(User31.objects.filter(blood_group="A+").values_list('blood_volume',flat=True))
    sum_of_values2=sum(User31.objects.filter(blood_group="B+").values_list('blood_volume',flat=True))
    sum_of_values3=sum(User31.objects.filter(blood_group="O+").values_list('blood_volume',flat=True))
    sum_of_values4=sum(User31.objects.filter(blood_group="AB+").values_list('blood_volume',flat=True))
    sum_of_values5=sum(User31.objects.filter(blood_group="A-").values_list('blood_volume',flat=True))
    sum_of_values6=sum(User31.objects.filter(blood_group="B-").values_list('blood_volume',flat=True))
    sum_of_values7=sum(User31.objects.filter(blood_group="O-").values_list('blood_volume',flat=True))
    sum_of_values8=sum(User31.objects.filter(blood_group="AB-").values_list('blood_volume',flat=True))

    obj=User33.objects.get(id=1)
    obj.blood_groupA1=sum_of_values1
    obj.blood_groupB1=sum_of_values2
    obj.blood_groupO1=sum_of_values3
    obj.blood_groupAB1=sum_of_values4
    obj.blood_groupA2=sum_of_values5
    obj.blood_groupB2=sum_of_values6
    obj.blood_groupO2=sum_of_values7
    obj.blood_groupAB2=sum_of_values8
    obj.save()

    obj=User30.objects.get(id=1)
    obj.blood_groupA1=sum_of_values1
    obj.blood_groupB1=sum_of_values2
    obj.blood_groupO1=sum_of_values3
    obj.blood_groupAB1=sum_of_values4
    obj.blood_groupA2=sum_of_values5
    obj.blood_groupB2=sum_of_values6
    obj.blood_groupO2=sum_of_values7
    obj.blood_groupAB2=sum_of_values8
    obj.save()
    return render(request,"admin_blood_stock.html")

'''def loggy(request):
    value=User32.objects.get(pk=8).blood_group
    if value=="A+":
        return render(request,"try1.html")
    else:
        return render(request,"insert4.html")

def try1(request):
    return render(request,"try1.html")'''

def insert_data1(request, source):
    source_data1=User20.objects.get(pk=source)
    User34.objects.create(
        name=source_data1.name,
        age=source_data1.age,
        reason=source_data1.reason,
        blood_group=source_data1.blood_group,
        blood_volume=source_data1.blood_volume
    )
    source_data1.delete()
    return redirect("../user_blood_request")

'''def insert_data2(request, source_id):
    source_data=User34.objects.get(pk=source_id)
    User21.objects.create(
        name=source_data.name,
        age=source_data.age,
        reason=source_data.reason,
        blood_group=source_data.blood_group,
        blood_volume=source_data.blood_volume
    )
    source_data.delete()
    return redirect("../user_request_rejected")'''


def insert_data2(request, source_id):
    value1=User33.objects.values_list('blood_groupA1',flat=True).first() 
    value2=User33.objects.get(pk=1).blood_groupB1
    value3=User33.objects.get(pk=1).blood_groupO1
    value4=User33.objects.get(pk=1).blood_groupAB1
    value5=User33.objects.get(pk=1).blood_groupA2
    value6=User33.objects.get(pk=1).blood_groupB2
    value7=User33.objects.get(pk=1).blood_groupO2
    value8=User33.objects.get(pk=1).blood_groupAB2
    value10=User34.objects.filter(blood_group="A+").values_list('blood_volume',flat=True).first()
    value11=User34.objects.filter(blood_group="B+").values_list('blood_volume',flat=True).first()
    value12=User34.objects.filter(blood_group="O+").values_list('blood_volume',flat=True).first()
    value13=User34.objects.filter(blood_group="AB+").values_list('blood_volume',flat=True).first()
    value14=User34.objects.filter(blood_group="A-").values_list('blood_volume',flat=True).first()
    value15=User34.objects.filter(blood_group="B-").values_list('blood_volume',flat=True).first()
    value16=User34.objects.filter(blood_group="O-").values_list('blood_volume',flat=True).first()
    value17=User34.objects.filter(blood_group="AB-").values_list('blood_volume',flat=True).first()
    data1=User34.objects.filter(blood_group="A+")
    data2=User34.objects.filter(blood_group="B+")
    data3=User34.objects.filter(blood_group="O+")
    data4=User34.objects.filter(blood_group="AB+")
    data5=User34.objects.filter(blood_group="A-")
    data6=User34.objects.filter(blood_group="B-")
    data7=User34.objects.filter(blood_group="O-")
    data8=User34.objects.filter(blood_group="AB-")
    if data1:
        if value1==0 or value1<value10:
            u=User34.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else: 
            result1=value1 - value10
            obj=User33.objects.get(id=1)
            obj.blood_groupA1=result1
            obj.save()
            negative_value = -value10
            my_object=User31.objects.create(
                blood_group=User34.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value
            )
            source_data=User34.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_request_rejected")
    elif data2:
        if value2==0 or value2<value11:
            u=User34.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result2=value2 - value11
            obj=User33.objects.get(id=1)
            obj.blood_groupB1=result2
            obj.save()
            negative_value1 = -value11
            my_object=User31.objects.create(
                blood_group=User34.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value1
            )
            source_data=User34.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_request_rejected")
    elif data3:
        if value3==0 or value3<value12:
            u=User34.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result3=value3 - value12
            obj=User33.objects.get(id=1)
            obj.blood_groupO1=result3
            obj.save()
            negative_value2 = -value12
            my_object=User31.objects.create(
                blood_group=User34.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value2
            )
            source_data=User34.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_request_rejected")
    elif data4:
        if value4==0 or value4<value13:
            u=User34.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result4=value4 - value13
            obj=User33.objects.get(id=1)
            obj.blood_groupAB1=result4
            obj.save()
            negative_value3 = -value13
            my_object=User31.objects.create(
                blood_group=User34.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value3
            )
            source_data=User34.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_request_rejected")
    elif data5:
        if value5==0 or value5<value14:
            u=User34.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result5=value5 - value14
            obj=User33.objects.get(id=1)
            obj.blood_groupA2=result5
            obj.save()
            negative_value4 = -value14
            my_object=User31.objects.create(
                blood_group=User34.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value4
            )
            source_data=User34.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_request_rejected")
    elif data6:
        if value6==0 or value6<value15:
            u=User34.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result6=value6 - value15
            obj=User33.objects.get(id=1)
            obj.blood_groupB2=result6
            obj.save()
            negative_value5 = -value15
            my_object=User31.objects.create(
                blood_group=User34.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value5
            )
            source_data=User34.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_request_rejected")
    elif data7:
        if value7==0 or value7<value16:
            u=User34.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result7=value7 - value16
            obj=User33.objects.get(id=1)
            obj.blood_groupO2=result7
            obj.save()
            negative_value6 = -value16
            my_object=User31.objects.create(
                blood_group=User34.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value6
            )
            source_data=User34.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_request_rejected")
    elif data8:
        if value8==0 or value8<value17:
            u=User34.objects.all()
            return render(request,'popup.html',{'u':u})
            #return render(request,'popup.html',{'message':'hello'})
        else:
            result8=value8 - value17
            obj=User33.objects.get(id=1)
            obj.blood_groupAB2=result8 
            obj.save()
            negative_value7 = -value17
            my_object=User31.objects.create(
                blood_group=User34.objects.values_list('blood_group',flat=True).first(), 
                blood_volume=negative_value7
            )
            source_data=User34.objects.get(pk=source_id)
            User21.objects.create(
            name=source_data.name,
            age=source_data.age,
            reason=source_data.reason,
            blood_group=source_data.blood_group,
            blood_volume=source_data.blood_volume
            )
            source_data.delete()
            #return render(request,'user_blood_request.html')
            return redirect("../user_request_rejected")

def log10(request):
    a=request.GET['a1']
    b=request.GET['a2']
    if User15.objects.filter(user_name=a,pwd=b):
        #if User21.objects.filter(name=a):
        u=User34.objects.filter(name=a)
        return render(request,'user_request_rejected1.html',{'u':u}) 
        #else:
            #return render(request,'user_login.html')
    else:
        return render(request,'user_login2.html')

def ins5(request):
    u=User20()
    u.name=request.GET["a1"]
    u.age=request.GET["a2"]
    u.reason=request.GET["a3"]
    u.blood_group=request.GET["a4"]
    u.blood_volume=request.GET["a5"]
    u.save()
    record_count=User32.objects.count()
    if record_count>0:
        source_value=User20.objects.values_list('blood_group',flat=True).first()
        source_value1=User20.objects.values_list('blood_volume',flat=True).first()
        obj=User32.objects.get(id=10)
        obj.blood_group=source_value
        obj.blood_volume=source_value1
        obj.save()
    else:
        source_records=User20.objects.all()
        for record in source_records:
            destination_record=User32(
            blood_group=record.blood_group,
            blood_volume=record.blood_volume
        )
        destination_record.save()
    return render(request,"home_page.html")



    