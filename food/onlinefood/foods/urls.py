from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.conf import settings 
from django.conf.urls.static import static 


urlpatterns = [
    url(r'login/',views.login,name="login"),
    url(r'home/',TemplateView.as_view(template_name='home.html')),
    url(r'signin/',views.signin,name="signin"),
    url(r'select/', TemplateView.as_view(template_name='select.html')),
    url(r'hotel/',views.displayhotels,name="hotel"),
    url(r'food/(?P<id>\d+)/$',views.displayfood,name="food"),
    url(r'status/', TemplateView.as_view(template_name='status.html')),
    url(r'payment/', TemplateView.as_view(template_name='payment.html')),
    url(r'cart/', TemplateView.as_view(template_name='cart.html')),
    url(r'shipping/', TemplateView.as_view(template_name='shipping.html')),
    url(r'review/',views.review,name="review"),
]
if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT)
