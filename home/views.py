from django.shortcuts import render, redirect
from .forms import UploadCSVForm
import csv
# Create your views here.
def index_page(request):
    if request.method == 'POST':
        form = UploadCSVForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the uploaded file
            csv_file = request.FILES['csv_file']
            decoded_file = csv_file.read().decode('utf-8').splitlines()
            reader = csv.reader(decoded_file)
            csv_data = [row for row in reader]  # Collect CSV data into a list
            
            # Render the data in the template
            return render(request, 'index.html', {'csv_data': csv_data})
    else:
        form = UploadCSVForm()

    return render(request, 'index.html', {'form': form})
