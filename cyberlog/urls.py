"""cyberlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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


import textwrap
from django.http import HttpResponse
from django.views.generic.base import View
from django.conf.urls import url

class HelloView(View):

    def dispatch(request, *args, **kwargs):
        response_text = textwrap.dedent('''\
            <html>
            <head>
                <title>Hi Hans!</title>
            </head>
            <body>
                <h1>Hi Hans</h1>
                <p>SUP YO</p>
            </body>
            </html>
        ''')
        return HttpResponse(response_text)


urlpatterns = [
    url(r'^$', HelloView.as_view(), name='hi'),
    path('admin/', admin.site.urls),
]
