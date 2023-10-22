from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from . import views


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



# add router

urlpatterns = [
    path("api/swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("api/redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("api/swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"),

    # path('worker/', views.WorkerListCreate.as_view()),
    path('api/worker/list/', views.workers),
    path('api/worker/c/', views.worker_c),
    path('api/worker/<str:pk>/', views.workers_pk),

    path('api/news/', views.news, name='news'),
    path("api/weather/", views.weather),
]
