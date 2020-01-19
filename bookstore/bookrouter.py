from rest_framework.routers import SimpleRouter
from bookstore.views import *
router = SimpleRouter()
router.register('authors',AuthorOperations)
router.register('books',BookOperations)
router.register('publishers',PublisherOperations)
router.register('addresses',AddressOperations)
urlpatterns = router.urls


