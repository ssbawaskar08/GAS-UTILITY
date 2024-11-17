from django.shortcuts import render, get_object_or_404
from .models import ServiceRequest
from django.utils import timezone


def manage_requests(request):
    requests = ServiceRequest.objects.all()
    return render(request, 'support/manage_requests.html', {'requests': requests})

def request_detail(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        service_request.status = request.POST.get('status')
        if service_request.status == 'Resolved':
            service_request.resolved_at = timezone.now()
        service_request.save()
    return render(request, 'support/request_detail.html', {'service_request': service_request})
