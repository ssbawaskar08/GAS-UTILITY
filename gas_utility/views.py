from django.shortcuts import redirect

def home(request):
    # Redirect to customers/submit-request/ as the default page
    # hi this is for my commit history
    return redirect('customers:submit_request')
