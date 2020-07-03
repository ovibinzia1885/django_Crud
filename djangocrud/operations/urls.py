"""djangocrud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from .import views
urlpatterns = [
    path('',views.index,name="index"),
    path('add/',views.addstudent,name="addstudent"),
    path('register',views.register,name="register"),

    path('view/',views.view,name="view"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('delete/<id>/', views.delete, name='delete'),
    path('update/<int:id>', views.update, name="update"),
    path('search',views.search,name="search"),
]