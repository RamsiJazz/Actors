from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [

                  path('', views.home, name='home'),
                  path('mammootty/', views.mammootty, name='mammootty'),
                  path('mohanlal', views.mohanlal, name='mohanlal'),
                  path('dileep', views.dileep, name='dileep'),
                  path('jayasurya', views.jayasurya, name='jayasurya'),
                  path('jayaram', views.jayaram, name='jayaram'),
                  path('sreenivasan', views.sreenivasan, name='sreenivasan')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
