from django . urls import path
from . import views

urlpatterns = [
    path('',views.index,name='expensive'),
    path('AddExpensive/',views.AddExpensives),
]

