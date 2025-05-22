
# main/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.views.generic import ListView, DetailView
from .models import Post
from django.db.models import Q


# Create your views here.
def inicio(request):
    return render(request, 'main/inicio.html')

def sobre_mi(request):
    return render(request, 'main/sobre_mi.html')

def servicios(request):
    return render(request, 'main/servicios.html')

def recetas(request):
    return render(request, 'main/recetas.html')


def eventos(request):
    return render(request, 'main/eventos.html')
def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            mensaje = form.cleaned_data['mensaje']
            texto_mail = (
            f"Hola, tienes un mensaje de parte de {nombre}\n"
            f"Correo de quien escribe: {email}\n\n"
            f"Contenido del mensaje:\n{mensaje}"
            )
            # Envía correo
            send_mail(
                subject=f'Nuevo mensaje de {nombre}',
                message= texto_mail,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Tu mensaje se ha enviado con éxito.')
            return redirect('contacto')
    else:
        form = ContactForm()
    return render(request, 'main/contacto.html', {'form': form})

def blog(request):
    return render(request, 'main/blog.html')

class PostListView(ListView):
    model               = Post
    template_name       = 'main/post_list.html'
    context_object_name = 'posts'
    paginate_by         = 5

    def get_queryset(self):
        qs = super().get_queryset().filter(publicado_flag=True).order_by('-publicado')
        q  = self.request.GET.get('q')
        if q:
            # Filtra donde el título, el contenido o la categoría coincidan
            qs = qs.filter(
                Q(titulo__icontains=q) |
                Q(contenido__icontains=q) |
                Q(categoria__nombre__icontains=q)
            )
        return qs
class PostDetailView(DetailView):
    model         = Post
    template_name = 'main/post_detail.html'