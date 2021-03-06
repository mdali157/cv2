from django.contrib import admin

# Register your models here.
from dashboard.models import Profile, ProfileSkills, ProfileEducation, ProfileExperience, Profilepic, ProfileProession, \
    ProfileCertificate, ProfessionalEducation, Profileinfo, Recommendations, CV, checks, CV2, ProfileTitlecv2,ProfileAwardscv2,ProfileProfessioncv2,ProfileCertificatecv2,ProfileReferencescv2,ProfileIntroductioncv2,ProfileAreaofexpertisecv2,ProfileBooksAuthoredcv2

admin.site.register(Profile)
admin.site.register(ProfileSkills)
admin.site.register(ProfileExperience)
admin.site.register(ProfileEducation)
admin.site.register(Profilepic)

admin.site.register(ProfileCertificate)
admin.site.register(ProfileProession)
admin.site.register(ProfessionalEducation)
admin.site.register(Profileinfo)
admin.site.register(Recommendations)
admin.site.register(CV)
admin.site.register(checks)

admin.site.register(CV2)
admin.site.register(ProfileAreaofexpertisecv2)
admin.site.register(ProfileCertificatecv2)
admin.site.register(ProfileBooksAuthoredcv2)
admin.site.register(ProfileAwardscv2)
admin.site.register(ProfileReferencescv2)
admin.site.register(ProfileProfessioncv2)
admin.site.register(ProfileIntroductioncv2)








