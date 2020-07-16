from django.db import models


class SetProv(models.Model):
    idno = models.AutoField(primary_key=True)
    provcod = models.CharField(max_length=5, unique=True)
    provdes = models.CharField(max_length=60, null=True, blank=True)
    catalogid = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        db_table = 'setprov'
        ordering = ['-idno']

    def __str__(self):
        return self.provdes


class SetAump(models.Model):
    idno = models.AutoField(primary_key=True)
    aumpcod = models.CharField(max_length=5, unique=True)
    aumpdes = models.CharField(max_length=60, null=True, blank=True)
    provcod = models.CharField(max_length=10, null=True, blank=True)
    postcod = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        db_table = 'setaump'

    def __str__(self):
        return self.aumpdes
