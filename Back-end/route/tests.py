from django.test import TestCase
from .models import Manager,Merchandiser,Comment,Address
# Create your tests here.

class ManagerTestClass(TestCase):
    def setUp(self):
        self.manager = Manager(name='Melody',description='I am the Manager at xyz Company',phone_number='+254256272',location='Nairobi')
    def test_instance(self):
        self.assertTrue(isinstance(self.manager,Manager))

    def test_save_manager(self):
        self.manager.save_manager()
        managers = Manager.objects.all()
        self.assertTrue(len(managers) > 0)