from rest_framework import routers
from .views import CarouselImgViewSet
from .views import BulletInViewSet

router = routers.DefaultRouter()
router.register(r'carouselimg', CarouselImgViewSet)
router.register(r'bulletin', BulletInViewSet)

