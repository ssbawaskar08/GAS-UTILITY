from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer, ServiceRequest

class CustomerModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser")
        Customer.objects.create(user=user, phone="1234567890", address="Test Address")

    def test_customer_creation(self):
        customer = Customer.objects.get(user__username="testuser")
        self.assertEqual(customer.phone, "1234567890")

class ServiceRequestModelTest(TestCase):
    def setUp(self):
        user = User.objects.create(username="testuser")
        customer = Customer.objects.create(user=user, phone="1234567890", address="Test Address")
        ServiceRequest.objects.create(customer=customer, service_type="Test Service", description="Test Description")

    def test_request_creation(self):
        service_request = ServiceRequest.objects.get(service_type="Test Service")
        self.assertEqual(service_request.description, "Test Description")
