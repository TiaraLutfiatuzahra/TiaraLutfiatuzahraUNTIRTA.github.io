from django.shortcuts import render

# Create your views here.
def fk(request):
    judul = "Akademik"
    S1 = ("Program Studi S-1", "Program Studi S-2")

    konteks = {
        'title' : judul,
        'S1' : S1,
    }
    return render(request, 'indexfk.html', konteks)
    