"""django_db_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from mysql_app import views

urlpatterns = [
    path('login/',views.login),
    path('login_succesfull',views.get_login),
    path('home/', views.home),
    path("index", views.mysql),
    path('new/',views.New_DB),
    path('edit_query/',views.quary_DB),
    path('success',views.success),
    path('quary_db/',views.quary_DB),
    path('query_types',views.query_DB_details),
    path('create_table/',views.create),
    path('create_done',views.create1),
    path('insert_data',views.insert),
    path('insert1',views.insert1),
    path('select_data',views.select),
    path('select1',views.select1),
    path('select_where',views.where),
    path('where1',views.where1),
    path('drop',views.drop),
    path('drop1',views.drop1),
    path('delete',views.delete),
    path('delete1',views.delete1),
    path('exit',views.exit)

]
