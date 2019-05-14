# coding: utf-8

from django.test.testcases import TestCase
from django.test.utils import override_settings
from django.urls.base import reverse


class TestsMiddleware(TestCase):

    def test_success_view(self):
        resp = self.client.get(reverse('success_view'))
        self.assertEquals(resp.status_code, 200)
        self.assertEquals(resp['Content-Type'], 'application/json')
        data = resp.json()
        self.assertEquals(data['status'], True)
        self.assertNotIn('exception', data)

    def test_fail_view(self):
        resp = self.client.get(reverse('fail_view'))
        self.assertEquals(resp.status_code, 500)
        self.assertEquals(resp['Content-Type'], 'application/json')
        data = resp.json()
        self.assertEquals(data['status'], False)
        self.assertIn('exception', data)
        self.assertEquals(data[u'exception'], 'ZeroDivisionError')
        self.assertIn('message', data)
        self.assertNotIn('traceback', data)

    @override_settings(DEBUG=True)
    def test_fail_debug_view(self):
        resp = self.client.get(reverse('fail_view'))
        self.assertEquals(resp.status_code, 500)
        self.assertEquals(resp['Content-Type'], 'application/json')
        data = resp.json()
        self.assertEquals(data['status'], False)
        self.assertIn('exception', data)
        self.assertEquals(data[u'exception'], 'ZeroDivisionError')
        self.assertIn('message', data)
        self.assertIn('traceback', data)
