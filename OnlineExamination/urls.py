"""OnlineExamination URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import view

urlpatterns = [
    # url(r'^admin/$', admin.site.urls),
    url(r'^main/$', view.main),
    # url(r'^verify/$', view.verify),
    url(r'^login/$', view.loginpage),
    url(r'^admin_main/$', view.admin_main),
 
    # url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'main.html'}),
    url(r'^infoeditor/$', view.table),
    url(r'^asset_show_table/$',view.show_asset_in_table),  # 
    url(r'^aothertableview/$',view.aothertableview), 
]