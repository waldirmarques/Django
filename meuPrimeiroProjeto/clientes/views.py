from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm

def person_list(request):
    #Pegar os dados do banco de dados
    bancoT = Person.objects.all()
    return render(request,"person.html",{'persons':bancoT})

def person_new(request):
    #CASO NÃO TENHA NADA CADASTRADO, ELE MANDARA UM POST VAZIO
    #PARA PEGAR ARQUIVOS DE MEDIA DO FORM, USA O REQUEST.FILES COMO ATRIBUTO

    form = PersonForm(request.FILES or None, request.POST or None)
    #if form.is_valid():
        #form.save()
        #return redirect('person_list')
    #return render(request, 'personForm.html' ,{'form': form})

    if (request.method == 'POST'):

        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        salary = request.POST.get('salary')
        #photo = request.FILES('photo')

        # Criando o usuario Aurora
        myUser = Person(first_name=first_name, last_name=last_name, age=age, salary=salary)
        print("Entrou aquiiiiiiiiiiiiiiiiii")
        myUser.save_base()
        return redirect('person_list')
    return render(request, 'personForm.html', {'form': form})

