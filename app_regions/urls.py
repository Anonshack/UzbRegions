from django.urls import path

from .views import RegionsListView, setLanguage, DistrictsListView


urlpatterns = [
    path('setLang/<str:lang>', setLanguage),
    path('districts', DistrictsListView.as_view(), name='districts'),
    path('', RegionsListView.as_view()),
]