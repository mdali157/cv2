from django.shortcuts import render

# Create your views here.
from dashboard.models import Profile, CV, CV2


def createpage(request):
    cv = CV.objects.filter(user=request.user).all()
    cv2 = CV2.objects.filter(user=request.user).all()
    print(cv)
    return render(request, 'createpage/addpages.html', {'cv': cv, 'cv2' : cv2})
