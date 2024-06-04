import json
import uuid
import os

from django.http import HttpResponse
from django.utils import timezone
from locations.models import Location

from django.conf import settings


def download_locations(request):
    base_dir = os.getenv('GOODMAP_BASE_DIR', settings.BASE_DIR)
    file_path = os.path.join(base_dir, 'tests', 'e2e_tests', 'e2e_test_data.json')

    with open(file_path, 'rb') as json_file:
        response = HttpResponse(json_file, content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename=locations.json'
    return response


