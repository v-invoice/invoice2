from django.shortcuts import render

def post_list(request):
    return render(request, 'djaApp/post_list.html', {})
