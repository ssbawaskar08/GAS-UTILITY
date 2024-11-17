from django.shortcuts import redirect

def home(request):
    # Redirect to customers/submit-request/ as the default page
    return redirect('customers:submit_request')
