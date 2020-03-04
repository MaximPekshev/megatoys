from django.urls import path

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.urls import include
from .views		 import show_index

from .views import show_about_us
from .views import show_manufacture
from .views import show_certificate
from .views import show_news
from .views import show_privacy_policy
from .views import show_payment
from .views import show_delivery
from .views import show_guarantee
from .views import show_help

urlpatterns = [	
	path('', 	   					show_index, name='show_index'),
	path('about_us/', 		        show_about_us , name='show_about_us'),
	path('manufacture/', 		    show_manufacture , name='show_manufacture'),
	path('certificate/', 		    show_certificate , name='show_certificate'),
	path('news/', 		            show_news , name='show_news'),
    path('privacy_policy/',         show_privacy_policy , name='show_privacy_policy'),
    path('payment/',                show_payment , name='show_payment'),
    path('delivery/',               show_delivery , name='show_delivery'),
    path('guarantee/',              show_guarantee , name='show_guarantee'),
    path('help/',                   show_help , name='show_help'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
