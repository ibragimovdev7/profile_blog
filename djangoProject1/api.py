from rest_framework import routers
from app1 import views

router = routers.DefaultRouter()
router.register(r'autor',views.AutorView,basename='autor')
router.register(r'article',views.ArticleView,basename='article')
router.register(r'linked_files',views.FileView,basename='linked_files')