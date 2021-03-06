from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profilepic(models.Model):
    picture = models.ImageField(blank=True)


class ProfileCertificate(models.Model):
    cert = models.TextField(blank=True, max_length=50)


class ProfileProession(models.Model):
    profession = models.TextField(blank=True, max_length=50)


class ProfessionalEducation(models.Model):
    profedu = models.TextField(blank=True, max_length=300)


class Profileinfo(models.Model):
    info = models.TextField(blank=True, max_length=600)


class Recommendations(models.Model):
    recomend = models.TextField(blank=True, max_length=300)
    recomendby = models.TextField(blank=True, max_length=500)


class cvtitle(models.Model):
    resumetitle = models.TextField(blank=True, max_length=300)





class ProfileEducation(models.Model):
    institute = models.TextField(max_length=50)
    board = models.TextField(max_length=50)
    degree = models.TextField(max_length=50)
    startingdate = models.TextField(max_length=20)
    endingdate = models.TextField(max_length=20)
    result = models.TextField(max_length=10)
    percentage = models.IntegerField(default=None)

    def __str__(self):
        return self.institute


class ProfileSkills(models.Model):
    skills = models.TextField(max_length=20)

    def __str__(self):
        return self.skills


class ProfileExperience(models.Model):
    organization = models.TextField(max_length=20)
    previousDesignation = models.TextField(max_length=20)
    startingDate = models.TextField(max_length=20)
    endingDate = models.TextField(max_length=20)
    responsibilities = models.TextField(max_length=100)

    # abc = models.

    def __str__(self):
        return self.organization


class Profile(models.Model):
    boolChoice = (
        ("Male", "Male"), ("Female", "Female"))

    name = models.CharField(max_length=50)
    fname = models.TextField(max_length=50)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=boolChoice)
    profile_pic = models.ImageField(default='place.png')

    email = models.TextField(max_length=20, default=None)
    contactno1 = models.IntegerField(default=None)
    contactno2 = models.IntegerField(blank=True, null=True)
    linkedin = models.TextField(max_length=50, default=None)
    address = models.TextField(max_length=100, default=None)

    education = models.ManyToManyField(ProfileEducation, default=None)
    experience = models.ManyToManyField(ProfileExperience, default=None)
    skills = models.ManyToManyField(ProfileSkills, default=None)
    # contact = models.ManyToManyField(ProfileContact, default=None)

    user = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name


class CV(models.Model):
    certificate = models.ManyToManyField(ProfileCertificate, default=None)
    profession = models.ManyToManyField(ProfileProession, default=None)
    profinfo = models.ManyToManyField(Profileinfo, default=None)
    recommend = models.ManyToManyField(Recommendations, default=None)
    title = models.ManyToManyField(cvtitle, default=None)

    user = models.ManyToManyField(User, blank=True)


class checks(models.Model):
    boolean = models.BooleanField()
    user = models.ManyToManyField(User, blank=True)


class ProfileProfessioncv2(models.Model):
    procv2 = models.TextField(blank=True, max_length=300)

class ProfileIntroductioncv2(models.Model):
    introcv2 = models.TextField(blank=True, max_length=300)

class ProfileAreaofexpertisecv2(models.Model):
    areaofexpertisecv2 = models.TextField(blank=True, max_length=300)

class ProfileBooksAuthoredcv2(models.Model):
    bookscv2 = models.TextField(blank=True, max_length=300)

class ProfileCertificatecv2(models.Model):
    certcv2 = models.TextField(blank=True, max_length=300)

class ProfileReferencescv2(models.Model):
    refcv2 = models.TextField(blank=True, max_length=300)
    orgcv2 = models.TextField(blank=True, max_length=300)
    emailcv2 = models.TextField(blank=True, max_length=300)


class ProfileAwardscv2(models.Model):
    awcv2 = models.TextField(blank=True, max_length=300)

class ProfileTitlecv2(models.Model):
    titcv2 = models.TextField(blank=True, max_length=300)


class CV2(models.Model):
    professsioncv2 = models.ManyToManyField(ProfileProfessioncv2,default=None)
    introductioncv2 = models.ManyToManyField(ProfileIntroductioncv2,default=None)
    area_of_expertisecv2 = models.ManyToManyField(ProfileAreaofexpertisecv2,default=None)
    books_authored = models.ManyToManyField(ProfileBooksAuthoredcv2,default=None)
    certificatecv2 = models.ManyToManyField(ProfileCertificatecv2,default=None)
    referencescv2 = models.ManyToManyField(ProfileReferencescv2,default=None)
    awardscv2 = models.ManyToManyField(ProfileAwardscv2,default=None)
    titlecv2 = models.ManyToManyField(ProfileTitlecv2, default=None)

    user = models.ManyToManyField(User,blank=True)