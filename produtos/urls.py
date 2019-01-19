from django.urls import path
from .views import prod_list
from .views import prod_new
from .views import update_pro
from .views import delete_p

urlpatterns = [
    path('list/', prod_list, name="product_list"),
    path('new/', prod_new, name="product_new"),
    path('update/<int:id>/', update_pro, name="product_update"),
    path('delete/<int:id>/', delete_p, name="product_delete"),
]