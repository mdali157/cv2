from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from createpage import urls as createurl

# Create your views here.
from . import forms
from dashboard.models import Profile, ProfileEducation, ProfileExperience, ProfileSkills, ProfileProession, \
    ProfileCertificate, ProfessionalEducation, Profileinfo, Profilepic, Recommendations, CV, cvtitle, checks, CV2, \
    ProfileProfessioncv2, ProfileIntroductioncv2, ProfileAreaofexpertisecv2, ProfileCertificatecv2, \
    ProfileReferencescv2, ProfileAwardscv2, ProfileTitlecv2, ProfileBooksAuthoredcv2


def addpic(request):
    if request.method == 'POST':
        form = forms.addProfilepic(request.POST, request.FILES)
        if form.is_valid():
            obj = Profile.objects.get(user=request.user)
            r = form.save()
            print("---------- 1st")
            print(request.FILES['picture'].name)
            obj.profile_pic = request.FILES['picture'].name

            print("----------")
            obj.save()
            request.method='GET'
            return newProfile(request)
    else:
        form = forms.addProfilepic()
    return newProfile(request)


@login_required(login_url='/accounts/login')
def dashboard_view(request):
    return newProfile(request)


def profile_form(request):
    id = request.user.id
    detail = Profile.objects.filter(id=id)
    return render(request, 'dashboard/profile_view.html', {'id': id, 'detail': detail})


def newProfile(request):
    id = request.user.id
    if request.method == 'POST':
        form = forms.addProfilepic(request.POST, request.FILES)
        if form.is_valid():
            obj = Profile.objects.filter(user=request.user).first()
            r = form.save()
            print("---------- 1st")

            # obj.profile_pic = request.FILES['picture'].name

            print("----------")
            obj.save()
            return newProfile(request)
    else:
        form = forms.addProfilepic()
    detail = Profile.objects.filter(user=request.user).first()
    return render(request, 'dashboard/profile_view.html', {'id': id, 'form': form, 'detail': detail})


def update_profile(request):
    id = request.user.id
    profile = Profile.objects.filter(user=request.user).first()
    print(profile)

    if request.method == 'POST':
        if profile:
            print("--------------")
        else:
            profile = Profile()
        firstname = request.POST.get("fname")
        fathername = request.POST.get("lname")
        aging = request.POST.get("age")
        sex = request.POST.get("gender")

        # education

        inslist = request.POST.getlist("Institute[]")
        boardlist = request.POST.getlist("Board_Uni[]")
        degreelist = request.POST.getlist("Degree[]")
        startingdatelist = request.POST.getlist("PassingYear[]")
        endingdatelist = request.POST.getlist("enddate[]")
        resultlist = request.POST.getlist("Result[]")
        percentagelist = request.POST.getlist("Number_CGPA[]")

        # Experience

        orglist = request.POST.getlist("Organization[]")
        pdlist = request.POST.getlist("Previous_Designation[]")
        fromdlist = request.POST.getlist("FromDate[]")
        todlist = request.POST.getlist("ToDate[]")
        reslist = request.POST.getlist("Responsibility[]")

        # skiils
        skilllist = request.POST.getlist('Skills[]')

        # contact
        mail = request.POST.get('email')
        number1 = request.POST.get('contact1')
        number2 = request.POST.get('contact2')
        linked = request.POST.get('linkedin')
        location = request.POST.get('address')

        profile.name = firstname
        profile.fname = fathername
        profile.age = aging
        profile.gender = sex

        profile.email = mail
        profile.contactno1 = number1
        profile.contactno2 = number2
        profile.linkedin = linked
        profile.address = location
        profile.save()
        profile.user.add(request.user)
        profile.save()

        # cont = ProfileContact(email=mail, contactno1=number1, contactno2=number2, linkedin=linked, address=location)
        # cont.save()
        # profile.contact.add(cont)
        # profile.save()

        profile.education.clear()
        # object = Employee.objects.all()
        for i in range(len(inslist)):
            print(i)

            edu = ProfileEducation(institute=inslist[i], board=boardlist[i], degree=degreelist[i],
                                   startingdate=startingdatelist[i], endingdate=endingdatelist[i],
                                   result=resultlist[i], percentage=percentagelist[i])
            edu.save()
            profile.education.add(edu)
            profile.save()

        profile.experience.clear()
        for i in range(len(orglist)):
            exp = ProfileExperience(organization=orglist[i], previousDesignation=pdlist[i], startingDate=fromdlist[i],
                                    endingDate=todlist[i], responsibilities=reslist[i])
            exp.save()
            profile.experience.add(exp)
            profile.save()

        profile.skills.clear()
        for i in range(len(skilllist)):
            skl = ProfileSkills(skills=skilllist[i])
            skl.save()
            profile.skills.add(skl)
            profile.save()
        #
        # detail = Profile.objects.filter(user=request.user).first()
        # return render(request, 'dashboard/profile_view.html', {'id': id, 'detail': detail})
        request.method = 'GET'
        return newProfile(request)
    return render(request, 'dashboard/profile_update.html', {'profile': profile, 'id': id})


def generate(request, id):
    uid = request.user.id
    detail = Profile.objects.filter(user=request.user).first()
    cv = CV.objects.get(id=id, user=request.user)
    print(cv)
    return render(request, 'dashboard/createresume.html', {'detail': detail, 'id': uid, 'cv': cv})


def generateCV2(request, id):
    uid = request.user.id
    detail = Profile.objects.filter(user=request.user).first()
    cv2 = CV2.objects.get(id=id, user=request.user)
    print(cv2)
    return render(request, 'dashboard/cvblack.html', {'detail': detail, 'id': uid, 'cv': cv2})


def generateCV(request):
    uid = request.user.id
    detail = Profile.objects.filter(user=request.user).first()
    return render(request, 'dashboard/newresume.html', {'detail': detail, 'id': uid})

# Create PagesResume

def addcvdetail(request):
    id = request.user.id
    profile = None

    if request.method == 'POST':
        if profile:
            print("--------------")
        else:
            profile = Profile()
        cv = CV()
        cv.save()
        objectivelist = request.POST.getlist('objective[]')
        certilist = request.POST.getlist('certificate[]')
        recommendationlist = request.POST.getlist('rec[]')
        recomendbylist = request.POST.getlist('recby[]')
        titlelist = request.POST.getlist('title[]')
        professionlist = request.POST.getlist('prof[]')

        print("_________________________________")
        print(certilist)
        for i in range(len(certilist)):
            print(i)
            cer = ProfileCertificate(cert=certilist[i])
            cer.save()
            cv.certificate.add(cer)
            cv.save()

        for i in range(len(titlelist)):
            title = cvtitle(resumetitle=titlelist[i])
            title.save()
            cv.title.add(title)
            cv.save()

        for i in range(len(professionlist)):
            profe = ProfileProession(profession=professionlist[i])
            profe.save()
            cv.profession.add(profe)
            cv.save()

        for i in range(len(objectivelist)):
            objective = Profileinfo(info=objectivelist[i])
            objective.save()
            cv.profinfo.add(objective)
            cv.save()
        for i in range(len(recommendationlist)):
            recomend = Recommendations(recomend=recommendationlist[i], recomendby=recomendbylist[i])
            recomend.save()
            cv.recommend.add(recomend)
            cv.save()

        cv.user.add(request.user)

        cv.save()
        return generate(request,cv.id)
    return render(request, 'dashboard/resume_form.html', {'profile': profile, 'id': id})

def selectcv(request):
    profile = Profile.objects.filter(user=request.user).count()

    return render(request, 'dashboard/selectCV.html',{'flag':profile})

def printcv(request, id):
    uid = request.user.id
    detail = Profile.objects.filter(user=request.user).first()
    cv = CV.objects.get(id=id, user=request.user)
    print(cv)
    return render(request, 'dashboard/CVwithPrint.html', {'detail': detail, 'id': uid, 'cv': cv})

def addcvdetail2(request):
    id = request.user.id
    profile = None

    if request.method == 'POST':
        if profile:
            print("--------------")
        else:
            profile = Profile()
        cv2 = CV2()
        cv2.save()
        title2list = request.POST.getlist('titelecv2[]')
        proslist = request.POST.getlist('profession[]')
        introlist = request.POST.getlist('Introduction[]')
        expertiselist = request.POST.getlist('Areaofexpertise[]')
        bookslist = request.POST.getlist('BooksAuthored[]')
        certificatelist = request.POST.getlist('certificatecv2[]')
        reflist = request.POST.getlist('ref[]')
        orglist = request.POST.getlist('org[]')
        emaillist = request.POST.getlist('email[]')
        awardlist = request.POST.getlist('awards[]')

        print("_________________________________")

        for i in range(len(title2list)):
            print(i)
            title2 = ProfileTitlecv2(titcv2=title2list[i])
            title2.save()
            cv2.titlecv2.add(title2)
            cv2.save()


        for i in range(len(awardlist)):
            print(i)
            award2 = ProfileAwardscv2(awcv2=awardlist[i])
            award2.save()
            cv2.awardscv2.add(award2)
            cv2.save()


        for i in range(len(reflist)):
            print(i)
            refference2 = ProfileReferencescv2(refcv2=reflist[i],orgcv2=orglist[i],emailcv2=emaillist[i])
            refference2.save()
            cv2.referencescv2.add(refference2)
            cv2.save()

        for i in range(len(certificatelist)):
            print(i)
            certificate2 = ProfileCertificatecv2(certcv2=certificatelist[i])
            certificate2.save()
            cv2.certificatecv2.add(certificate2)
            cv2.save()


        for i in range(len(bookslist)):
            print(i)
            book = ProfileBooksAuthoredcv2(bookscv2=bookslist[i])
            book.save()
            cv2.books_authored.add(book)
            cv2.save()

        for i in range(len(proslist)):
            print(i)
            prof = ProfileProfessioncv2(procv2=proslist[i])
            prof.save()
            cv2.professsioncv2.add(prof)
            cv2.save()

        for i in range(len(introlist)):
            intro = ProfileIntroductioncv2(introcv2=introlist[i])
            intro.save()
            cv2.introductioncv2.add(intro)
            cv2.save()

        for i in range(len(expertiselist)):
            expertise = ProfileAreaofexpertisecv2(areaofexpertisecv2=expertiselist[i])
            expertise.save()
            cv2.area_of_expertisecv2.add(expertise)
            cv2.save()

        cv2.user.add(request.user)
        cv2.save()
        return generateCV2(request, cv2.id)
    return render(request, 'dashboard/resume_form2.html', {'profile': profile, 'id': id})

def printcvblack(request, id):
    uid = request.user.id
    detail = Profile.objects.filter(user=request.user).first()
    cv2 = CV2.objects.get(id=id, user=request.user)
    print(cv2)
    return render(request, 'dashboard/cvblack_afterprint.html', {'detail': detail, 'id': uid, 'cv': cv2})