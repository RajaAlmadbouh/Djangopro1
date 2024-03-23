from django.urls import path
from .views import *

urlpatterns = [

    path('HomePage/', HomePage, name='HomePage'),

    
    # path('', include('members.urls')),
    # path('admin/', admin.site.urls),
    # path('HomePage' , HomePage , name="HomePage"),

]
     
