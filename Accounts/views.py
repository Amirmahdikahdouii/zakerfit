from django.shortcuts import render
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Process the form data here (e.g., create a new user)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # Perform the necessary actions with the form data
            # ...
            return render(request, 'success.html')  # Redirect to a success page
    else:
        form = SignUpForm()

    return render(request, 'Accounts/forms.html', {'form': form})
