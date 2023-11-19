from django.shortcuts import render
from .forms import FormLink
from .models import Link
from django.shortcuts import redirect
from django.http.response import HttpResponse


def home(request):
    form = FormLink()
    status = request.GET.get('status')
    return render(request, 'home.html', {'form': form, 'status': status})


def link(request):
    if request.method == 'POST':
        form = FormLink(request.POST)
        if form.is_valid():
            link_encurtado = form.cleaned_data['link_encurtado']
            links = Link.objects.filter(link_encurtado=link_encurtado)
            if links.exists():
                return redirect('/?status=1')
            form.save()
            return render(request, 'links.html', {'link_pronto': link_encurtado})
    else:
        form = FormLink()
    return render(request, 'home.html', {'form': form})

def redirecionar(request, link):
    links = Link.objects.filter(link_encurtado = link)
    if len(link) == 0:
        return redirect('/')
    return redirect(links[0].link_redirect)
