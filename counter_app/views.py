from django.shortcuts import render, redirect


def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
        request.session['timelabel'] = 'times'
    else:
        request.session['counter'] = 1
        request.session['timelabel'] = 'time'

    return render(request, "index.html")


def reset(request):
    if 'counter' in request.session:
        del request.session['counter']  
    return redirect('/')

