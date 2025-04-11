from django.contrib import admin
from django.urls import path

from fire.views import HomePageView, ChartView, PieCountbySeverity, LineCountbyMonth, MultilineIncidentTop3Country, multipleBarbySeverity, map_station, fire_incident_map
from fire.views import firestationListView, firestationCreateView, firestationUpdateView, firestationDeleteView
from fire.views import IncidentListView
from fire import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('stations', views.map_station, name='map-station'),
    path('', HomePageView.as_view(), name='home'),
    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('chart/', PieCountbySeverity, name='chart'),
    path('lineChart/', LineCountbyMonth, name='chart'),
    path('multilineChart/', MultilineIncidentTop3Country, name='chart'),
    path('multiBarChart/', multipleBarbySeverity, name='chart'),
    path('stations/', map_station, name='map-station'),  
    path('fire_incident_map/', fire_incident_map, name='fire-incident-map'),

    path('firestation_list/', firestationListView.as_view(), name='station-list'),
    path('firestation_list/add', firestationCreateView.as_view(), name='firestation-add'),
    path('firestation_list/<pk>', firestationUpdateView.as_view(), name='firestation-update'),
    path('firestation_list/<pk>/delete/', firestationDeleteView.as_view(), name='firestation-delete'),
    
    path('incident_list/',  IncidentListView.as_view(), name='incident-list'),
]
