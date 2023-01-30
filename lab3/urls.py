from django.contrib import admin
from stocks import views as stock_views
from django.urls import include, path
from rest_framework import routers
from stocks.views import Registration, LoginView, LogoutView, Check
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'toys', stock_views.ToyViewSet)
router.register(r'users', stock_views.UsersViewSet)
router.register(r'basket', stock_views.BasketViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path('api/register/', Registration.as_view(), name='register'),
    path('authenticated', Check.as_view()),
    path('logout', LogoutView.as_view()),
    path('login', LoginView.as_view()),
    path('admin/', admin.site.urls),
    # path('', include(('sampleapp.urls'), namespace='sampleapp'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
