"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from basic.views import sample,sample1,sampleinfo,dynamicResponse,health,addStudent,job1,job2,signUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('greet/',sample),
    path("sample1/",sample1),
    path('info/',sampleinfo),
    path("dynamic/",dynamicResponse),
    path("health/",health),
    path("student/",addStudent),
    path("job1/",job1),
    path("job2/",job2),
    path("signup/",signUp)

]
#get,post,put,delete
