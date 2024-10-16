import time
from rest_framework.response import Response

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()

        # Log the request method, URL, and view name
        view_name = request.resolver_match.view_name
        user = request.user if request.user.is_authenticated else "Anonymous"
        request_data = request.data if hasattr(request, "data") else None
        request_headers = dict(request.headers)
        
        print(f"Request: {request.method} {request.path} (View: {view_name})")
        print(f"User: {user}")
        print(f"Request Data: {request_data}")
        print(f"Request Headers: {request_headers}")

        # Log the response status code and processing time
        print(f"Response: {response.status_code} (Processed in {end_time - start_time:.2f} seconds)")

        return response

