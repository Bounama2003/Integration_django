from django.urls import path
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
   # path('reset_password/',views.PasswordResetView.as_view(),name='reset_password'),
   # path('reset_password_send/',views.PasswordResetDoneView.as_view(),name='reset_password_send'),
   # path('reset_password_confirm/',views.PasswordResetConfirmView.as_view(),name='reset_password_confirm'),
   # path('reset_password_complete/',views.PasswordResetCompleteView.as_view(),name='reset_password_complete')


]
   
