# 📝 Şəxsi Qeydlər Tətbiqi (Django CRUD Layihəsi)

Bu, Python veb çərçivəsi olan **Django** istifadə edilərək yaradılmış sadə bir tətbiqdir. Məqsəd Django-nun əsas MVT (Model-View-Template) arxitekturasını, Verilənlər Bazasını (Models) və **CRUD (Create, Read, Update, Delete)** əməliyyatlarını mənimsəməkdir.

### 🌟 Əsas Xüsusiyyətlər

* **Qeydlərin Siyahısı (Read):** Bütün qeydlərin siyahısı.
* **Detallı Baxış (Read):** Hər bir qeydin tam məzmunu.
* **Yeni Qeyd Yaratma (Create):** `ModelForm` vasitəsilə yeni qeydlərin əlavə edilməsi.
* **Qeydi Yeniləmə (Update):** Mövcud qeydlərin redaktəsi.
* **Qeydi Silmə (Delete):** (Hazırda qurulma mərhələsindədir.)

### 🛠️ Texnologiyalar

| Komponent | İstifadə Olunan Texnologiya |
| :--- | :--- |
| **Backend** | Python 3.x |
| **Web Çərçivə** | Django 4.x / 5.x |
| **Verilənlər Bazası** | SQLite (İnkişaf Mühiti) |

### 🚀 Quraşdırma və İşə Salma

Layihəni lokal kompüterinizdə işə salmaq üçün:

#### 1. Mühitin Hazırlanması

```bash
# Layihə qovluğuna keçid
cd django_qeydler

# Virtual mühiti yarat və aktivləşdir
python -m venv venv
source venv/bin/activate 
# Windows (Cmd) istifadəçiləri: venv\Scripts\activate