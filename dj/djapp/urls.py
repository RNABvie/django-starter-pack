from django.urls import path
from . import views

urlpatterns = [
    # path('worker/', views.WorkerListCreate.as_view()),
    # # path('worker/', views.workers),
    # path('worker/<str:pk>', views.workers_pk),

    path('news/', views.news),
    path("weather/", views.weather),
]
