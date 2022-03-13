from django.shortcuts import render

from django.http import HttpResponse


def bad_request_error_400(request, exception):
    return render(request, "exceptions/400.html", status=400)


def forbidden_error_403(request, exception):
    return render(request, "exceptions/403.html", status=403)


def page_not_found_view_404(request, exception):
    return render(request, "exceptions/404.html", status=404)


def internal_error_500(request):
    return render(request, "exceptions/500.html", {})
