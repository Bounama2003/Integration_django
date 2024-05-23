from django.db import models
class Patient(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    numtel=models.CharField(max_length=20)
    motif=models.TextField()
    def __str__(self):
        return f" {self.nom} {self.prenom}"
    
class Rendez_vous(models.Model):
    patient=models.ForeignKey(Patient, on_delete=models.CASCADE)
    date=models.DateField()
    heure=models.TimeField()

    def __str__(self):
        return f"Rendez-vous pour {self.patient.nom} le {self.date} à {self.heure}"
    
