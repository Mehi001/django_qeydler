from django.db import models

class Qeyd(models.Model):
    basliq = models.CharField(max_length=200) # Başlıq sahəsi, maksimum 200 simvol
    mezmun = models.TextField()               # Məzmun sahəsi, limitsiz mətn üçün
    yaradilma_tarixi = models.DateTimeField(auto_now_add=True) # Yalnız yaradılma zamanı avtomatik təyin olunur

    def __str__(self):
        # Admin panelində və ya print edəndə obyektin necə göstəriləcəyini təyin edir
        return self.basliq