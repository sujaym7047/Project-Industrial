from django.urls import path
from django.urls import reverse
from . import views
urlpatterns=[
path('home_page',views.home_page),
    path('admin_home',views.admin_home),
    path('user_home',views.user_home),
    path("admin_login",views.admin_login),
    path("log5",views.log5),
    path("user_login",views.user_login),
    path("user_login1",views.user_login1),
    path("user_login2",views.user_login2),
    path("user_login3",views.user_login3),
    path("log6",views.log6),
    path("log7",views.log7),
    path("log10",views.log10),
    path("log20",views.log20),
    path("ins8",views.ins8),
    path("user_blood_request",views.user_blood_request),
    path("user_make_request",views.user_make_request),
    path("button_change",views.button_change),
    path("ins1",views.ins1),
    path("ins5",views.ins5),
    path("user_request_history",views.user_request_history),
    path("insert_data/<int:source_id>",views.insert_data),
    path("insert_data1/<int:source>",views.insert_data1),
    path("insert_data2/<int:source_id>",views.insert_data2),
    #path("insert_data1/<int:source_id>",views.insert_data1),
    path("user_request_accepted",views.user_request_accepted),
    path("user_request_rejected",views.user_request_rejected),
    path("insert4",views.insert4),
    path('ins21',views.ins21),
    #path("calculate_sum1/<blood_group>",views.calculate_sum1)
    path('popup',views.popup),
    path('admin_blood_stock',views.admin_blood_stock),
    path('ins30',views.ins30)
    #path('loggy',views.loggy),
    #path('try1',views.try1)

]