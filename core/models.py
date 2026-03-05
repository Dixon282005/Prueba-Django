from django.db import models

class Project(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.code} - {self.name}"

class Document(models.Model):
    class Status(models.TextChoices):
        BORRADOR = 'BORRADOR', 'Borrador'
        REVISION = 'REVISION', 'En Revisión'
        APROBADO = 'APROBADO', 'Aprobado'

    project = models.ForeignKey(
        Project, 
        on_delete=models.CASCADE, 
        related_name='documents'
    )
    
    tag = models.CharField(max_length=50)
    revision = models.CharField(max_length=5) 
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.BORRADOR
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['project', 'tag'], 
                name= 'unique_tag_per_project'
            )
        ]

    def __str__(self):
        return f"{self.tag} (Rev {self.revision}) - {self.project.code}"