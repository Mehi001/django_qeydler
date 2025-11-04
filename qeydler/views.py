

# Create your views here.
#from django.shortcuts import render
#from django.http import HttpResponse


#from django.shortcuts import render # << render funksiyası HTML şablonları göstərmək üçündür

# from django.http import HttpResponse # << Artıq buna ehtiyac yoxdur

#def qeyd_siyahisi(request):
    # render funksiyası: (sorğu obyekti, şablonun adı, kontekst dict (hələlik yoxdur))
#    return render(request, 'qeydler/qeyd_siyahisi.html', {})
from django.shortcuts import render
from .models import Qeyd # << Yeni yaratdığımız modeli import edirik
from django.shortcuts import render, get_object_or_404, redirect # << 'redirect'-i import edin
from .models import Qeyd
from .forms import QeydFormu # << Yaratdığımız Formu import edirik
def qeyd_siyahisi(request):
    # ORM istifadə edərək bazadan bütün qeydləri alırıq
    # .all() - bütün obyektləri qaytarır
    # .order_by('-yaradilma_tarixi') - ən yeni qeydi birinci göstərmək üçün
    butun_qeydler = Qeyd.objects.all().order_by('-yaradilma_tarixi')

    # Şablona göndəriləcək kontekst (sözlük/dictionary) yaradırıq
    kontekst = {
        'qeydler': butun_qeydler
    }

    # render funksiyası konteksti şablona ötürür
    return render(request, 'qeydler/qeyd_siyahisi.html', kontekst)
def qeyd_detali(request, pk):
    # get_object_or_404: Verilən pk-ya uyğun obyekti bazadan tapır.
    # Tapılmasa, avtomatik olaraq 404 səhifəsi göstərir (Django-nun gözəl xüsusiyyəti!)
    qeyd = get_object_or_404(Qeyd, pk=pk)

    kontekst = {
        'qeyd': qeyd
    }
    return render(request, 'qeydler/qeyd_detali.html', kontekst)
def qeyd_yarat(request):
    if request.method == 'POST':
        # 1. Sorğu POST olduqda: İstifadəçi formanı doldurub göndərib.
        form = QeydFormu(request.POST) # Göndərilən məlumatlarla formu doldururuq

        if form.is_valid():
            # 2. Məlumatlar etibarlıdırsa:
            yeni_qeyd = form.save() # Formu verilənlər bazasına yazırıq
            # 3. İstifadəçini yeni yaratdığı qeydin detal səhifəsinə yönləndiririk
            return redirect('detal', pk=yeni_qeyd.pk)

    else:
        # Sorğu GET olduqda: Səhifəyə ilk dəfə daxil olub.
        form = QeydFormu() # Boş bir form yaradırıq

    kontekst = {'form': form}
    return render(request, 'qeydler/qeyd_formu.html', kontekst)