from django.test import SimpleTestCase
from django.urls import reverse,resolve
from budget.views import project_list,ProjectCreateView,project_detail
import unittest
class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('list')
        self.assertEqual(resolve(url).func,project_list)
    def test_project_creat_url_resolved(self):
        url = reverse('add')
        self.assertEqual(resolve(url).func.view_class,ProjectCreateView)
    
    def test_project_detail_url_resolved(self):
        url = reverse('detail',args=['some-slug'])
        self.assertEqual(resolve(url).func,project_detail)
    
    
 
      