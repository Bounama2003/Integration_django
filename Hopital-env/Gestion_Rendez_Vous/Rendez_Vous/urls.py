from django.urls import path, include
#from django.contrib.auth import views as auth_views

from Rendez_Vous.views import liste_rendezvous,liste_patient,enregistrer_rendez_vous,modifier_rdv,supprimer_rdv,details_rdv,ajouter_patient, supprimer_patient, modifier_patient,details_patients, index,inscription, connexion,deconnexion
from django.contrib.auth import views


urlpatterns=[
    path('rendezvous/',liste_rendezvous, name='rendezvous'),
    path('liste_patient/', liste_patient, name='liste_patient'),
    path('enregistrer_rendez_vous/', enregistrer_rendez_vous, name='enregistrer_rendez_vous'),
    path('modifier/<int:id>', modifier_rdv, name='modifier'),
    path('supprimer_rdv/<int:id>', supprimer_rdv, name='supprimer_rdv'),
    path('details_rdv/<int:id>', details_rdv, name='details_rdv'),
    path('ajouter_patient/', ajouter_patient, name='ajouter_patient'),
    path('supprimer_patient/<int:id>', supprimer_patient, name='supprimer_patient'),
    path('modifier_patient/<int:id>', modifier_patient, name='modifier_patient'),
    path('details_patient/<int:id>', details_patients, name='details_patients'),
    path('', index, name='index'),
    path('inscription/', inscription, name='inscription'),
    path('accounts/login/', connexion, name='connexion'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path('reset_password/',views.PasswordResetView.as_view(template_name='password_reset.html'),name='reset_password'),
    path('reset_password_send/',views.PasswordResetDoneView.as_view(template_name='password_reset_send.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',views.PasswordResetCompleteView.as_view(template_name='password_confirm.html'),name='password_reset_complete'),
    
    #path('accounts/',include('django.contrib.auth.urls'))
    #path('enregistrer_rdv_patient/<int:id>', enregistrer_rdv_patient, name='enregistrer_rdv_patient')


]
   
