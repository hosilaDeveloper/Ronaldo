from django.urls import path
from person.views import *

app_name = 'main'

urlpatterns = [
    # path('', home_view, name='home'),
    path('', index, name='home'),
]
