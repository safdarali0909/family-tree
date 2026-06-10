from django.db import models


from django.db import models


class FamilyMember(models.Model):
    name = models.CharField(max_length=255)

    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.CASCADE
    )

    birth_date = models.DateField(
        null=True,
        blank=True
    )
    death_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name