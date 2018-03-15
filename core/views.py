# from django.http import HttpResponse
from django.shortcuts import render


# def hi (request,w1,w2):
#     return HttpResponse(w1+w2)


def hi (request,n1,n2):
    s=n1+n2
    return render(request, 'hi.html',{
        's' :s,
    })
# def root(request, n1, n2):
#     s = n1 + n2
#     return render(request, 'hi.html',{
#     's':s,
#     })
def r(request, start ,stop):
    if start > stop:
         # x=start
         # start=stop
         # stop=x
        start,stop=stop,start
    rr=range(start,stop+1)
    rr=reversed(rr)
    return render(request,'r.html',{
     'rr':rr,
    })

