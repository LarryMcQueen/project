from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, full_name, matric_number, email, department, level, college, session, password=None):
        if not full_name:
            raise ValueError("Student must have a name")
        if not matric_number:
            raise ValueError("Student must have a matric number")
       
        if not email:
             raise ValueError("Student must have an email")
        if not department:
             raise ValueError("Student must have a department")
        
        user = self.model(
                email=self.normalize_email(email),
                matric_number=matric_number,
                full_name=full_name,
                department=department,
                level = level,
                college = college,
                session = session,
                
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, full_name, matric_number, email, department, level, college, session, password=None):
        user = self.create_user(
                full_name=full_name,
                matric_number=matric_number,
                email=self.normalize_email(email),
                department=department,
                level = level,
                college = college,
                session = session,
                password=password,
                
        )
        
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user





GENDER=[
    ('', 'Select Gender'),
    ("M","Male"),
    ("F","Female"),
]

DEPARTMENT=[
    ('', 'Select Department'),
    ('Chemistry', 'Chemistry'),
    ('Industrial Chemistry', 'Industrial Chemistry'),
    ('Physics', 'Physics'),
    ('Geophysics', 'Geophysics'),
    ('Geology', 'Geology'),
    ('Computer Science', 'Computer Science'),
    ('Mathematics', 'Mathematics'),
    ('Environmental Management Toxicology', 'Environmental Sci'),
    ('Petroleum Engineering', 'Petroleum Engr'),
    ('Chemical Engineering','Chemical Engr'),
    ('Electrical Electronics Engineering', 'Elect/Elect Engr'),
    ('Mechanical Engineering', 'Mechanical Engr'),
    ('Marine Engineering', 'Marine Engr'),
]

SESSION=[
    ('', 'Select Year'),
    ('2020/2021', '2020/2021'),
]

COLLEGE=[
    ('', 'Select College'),
    ('Science','College Of Science'),
    ('Technology','College OF Technology'),
]

LEVEL=[
    ('', 'Select Level'),
    ('300','300'),
    ('400','400'),
]


class Account(AbstractBaseUser):
    full_name       = models.CharField(max_length=100, null=True, blank=True)
    email           = models.EmailField(max_length=100, null=True, blank=True)
    session         = models.CharField(max_length=100, choices=SESSION, null=True, blank=True)
    college         = models.CharField(max_length=100, choices=COLLEGE, null=True, blank=True)
    level           = models.CharField(max_length=100, choices=LEVEL, null=True, blank=True)
    gender          = models.CharField( max_length=50, choices=GENDER, null=True, blank=True)
    department      = models.CharField( max_length=50, choices=DEPARTMENT, null=True, blank=True)
    matric_number   = models.CharField(max_length=100, unique=True, null=True, blank=True)
    image           = models.ImageField(upload_to='profile_image', blank=True, null=True)
    date_joined     = models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login      = models.DateField(verbose_name='last login', auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'matric_number'  #requred detail that would be used to login
    REQUIRED_FIELDS = ['full_name', 'email', 'department','level','college','session']  #Required fields to be filled

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    
    


    # def get_absolute_url(self):
    #     return reverse("school:detail", kwargs={"pk": self.pk})
    
class SiwesInformation(models.Model):
    account                     = models.ForeignKey(Account, on_delete=models.CASCADE)
    bankName                    = models.CharField(max_length=50, blank=True, default='', null=True)
    accountNo                   = models.CharField(max_length=50, blank=True,  null=True, default='')
    phoneNo                     = models.CharField(max_length=50, null=True,blank=True)
    industryName                = models.CharField(max_length=50, default='', blank=True, null=True)
    industryAddress             = models.CharField(max_length=50, default='', blank=True, null=True)
    industrySupervisorname      = models.CharField(max_length=50, default='', blank=True, null=True)
    industrySupervisorPhoneno   = models.CharField(max_length=50, blank=True, null=True)

    
    def __str__(self):
        pkz = self.user.matric_number
        return pkz


    

    

    



