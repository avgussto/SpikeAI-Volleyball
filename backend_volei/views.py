from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo usuário
            return redirect('login')  # Redireciona para a página de login ou onde você quiser
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
