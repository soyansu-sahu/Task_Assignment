from django.http.response import JsonResponse


def root(request):
    response = JsonResponse({'status':True,'message':'success'}, status=500)
    return response