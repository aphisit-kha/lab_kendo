from django.db import models

# Create your models here.
class AccMst(models.Model):
    idno = models.AutoField(primary_key=True)
    accmstcod = models.CharField(max_length=12, unique=True, verbose_name='รหัสบัญชี')
    accmstnam = models.CharField(max_length=100, null=True, blank=True, verbose_name='คำอธิบาย (TH)')
    accmsteng = models.CharField(max_length=100, null=True, blank=True, verbose_name='คำอธิบาย (EN)')
    acctypcod = models.CharField(max_length=12, null=True, blank=True, verbose_name='หมวด')
    accgrpcod = models.CharField(max_length=12, null=True, blank=True, verbose_name='กลุ่ม')
    acclevel = models.CharField(max_length=1, default='1', verbose_name='Level')
    acctypjob = models.CharField(max_length=1, default='1', verbose_name='job')
    accbalndrcr = models.CharField(max_length=1, default='1', verbose_name='job')
    accontrol = models.CharField(max_length=12, null=True, blank=True, verbose_name='บัญชีคุม')
    accflag = models.CharField(max_length=1, default='N')
    memo1 = models.CharField(max_length=512, null=True, blank=True)
    accflaguse = models.CharField(max_length=1, default='Y')
    divifl = models.CharField(max_length=1, default='N')

    class Meta:
        db_table = 'accmst'
        ordering = ['accmstcod', ]
        verbose_name = 'ผังบัญชี'
        verbose_name_plural = 'ผังบัญชี'

    def __str__(self):
        return '%s - %s' % (self.accmstcod, self.accmstnam)