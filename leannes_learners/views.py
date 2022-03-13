from django.shortcuts import render

from django.http import HttpResponse


def page_not_found_view_404(request, exception):
    return render(request, "exceptions/404.html", status=404)


def forbidden_error_403(request, exception):
    return render(request, "exceptions/403.html", {})


def internal_error_500(request):
    return render(request, "exceptions/500.html", {})


def bad_request_error_400(request, exception):
    return render(request, "exceptions/400.html", {})
