from django.shortcuts import render, redirect, get_object_or_404
from . models import Patient, Rendez_vous
from . forms import PatientForms,RendezvousForm, UserForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def liste_rendezvous(request):
    rendez_vous=Rendez_vous.objects.all()
    return render(request, 'liste_rendezvous.html', {'rendez_vous':rendez_vous})

@login_required
def liste_patient(request):
    patients=Patient.objects.all()
    item_submit=request.GET.get('item-submit')
    # rechercher par le nom du patient
    if item_submit != '' and item_submit is not None:
        
        patients=Patient.objects.filter(nom__icontains=item_submit)
    
        
    return render(request, 'liste_patient.html', {'patients':patients})

@login_required
def enregistrer_rendez_vous(request):
    form=RendezvousForm()
    if request.method=='POST':
        form=RendezvousForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rendezvous')
    else:
        form=RendezvousForm()
    return render(request, 'rendezvousform.html', {'form':form})


"""def enregistrer_rdv_patient(request, id):
    patient=Patient.objects.get(id=id)
    if request.method == 'POST':
        form = RendezvousForm(request.POST)
        if form.is_valid():
            rendezvous = form.save(commit=False)
            rendezvous.patient = patient
            rendezvous.save()
            return redirect('rendezvous', id=patient.id)
    else:
        form=RendezvousForm(initial={'patient': patient})
    return render(request, 'addrdvparID.html',{'form':form, 'patient':patient})"""

@login_required
def modifier_rdv(request, id):
    rendezvous=Rendez_vous.objects.get(id=id)
    if request.method=='POST':
        form=RendezvousForm(request.POST, instance=rendezvous)
        if form.is_valid():
            form.save()
            return redirect('rendezvous')
    else:
        form=RendezvousForm(instance=rendezvous)
        return render(request, 'modifier_rdv.html', {'form':form})
    
@login_required
def supprimer_rdv(request, id):
    rendezvous=Rendez_vous.objects.get(id=id)
    if request.method=='POST':
        rendezvous.delete()
        return redirect('rendezvous')
    return render(request, 'confirmer_supprdv.html', {'rendezvous':rendezvous})

@login_required
def details_rdv(request, id):
    rendezvous=Rendez_vous.objects.get(id=id)
    return render(request, 'details_rdv.html', {'rendezvous':rendezvous})

@login_required
def ajouter_patient(request):
    fors=PatientForms()
    if request.method=='POST':
        fors=PatientForms(request.POST)
        fors.save()
        return redirect('liste_patient')
    return render(request, 'ajouter_patient.html', {'fors': fors})

@login_required
def supprimer_patient(request, id):
    patient=Patient.objects.get(id=id)
    if request.method=='POST':
        patient.delete()
        return redirect('liste_patient')
    return render(request, 'supprimer_patient.html', {'patient':patient})

@login_required
def modifier_patient(request, id):
    patient=Patient.objects.get(id=id)
    if request.method=='POST':
        fors=PatientForms(request.POST, instance=patient)
        if fors.is_valid():
            fors.save()
            return redirect('liste_patient')
    else:
        fors=PatientForms(instance=patient)
        return render(request, 'modifier_patient.html', {'fors':fors})
    

@login_required
def details_patients(request, id):
    patient=Patient.objects.get(id=id)
    return render(request,'details_patient.html', {'patient':patient})


def index(request):
    return render(request, 'index.html')


def inscription(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre inscription a bien réussi')
            return redirect('connexion')
        else:
            messages.error(request, form.errors)
    return render(request, 'inscription.html', {'form':form})


def connexion(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Authentification réussi avec succés')
            return redirect('liste_patient')
        else:
            messages.error(request, 'Erreur d\'authentification')
    return render(request, 'login.html')


@login_required
def deconnexion(request):
    logout(request)
    return redirect('connexion')




    







    

# Create your views here.
