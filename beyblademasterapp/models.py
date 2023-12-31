from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
class CurAddress(BaseModel):
    houseNo = models.IntegerField(null=True, blank=True)
    street = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    province = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    
    def __str__(self):
        return ", ".join([str(self.houseNo), self.street, self.city, self.province, self.country])

class Mentor(BaseModel):
    curAddr = models.ForeignKey(CurAddress, blank=True, null=True, on_delete=models.CASCADE, related_name='%(class)s_mentor')
    firstName = models.CharField(max_length=50, null=True, blank=True)
    lastName = models.CharField(max_length=50, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    homeTown = models.CharField(max_length=250, null=True, blank=True)
    homeCountry = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return " ".join([self.firstName, self.lastName])

class Player(BaseModel):
    curAddr = models.ForeignKey(CurAddress, blank=True, null=True, on_delete=models.CASCADE, related_name='%(class)s_player')
    mentor = models.ForeignKey(Mentor, blank=True, null=True, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50, null=True, blank=True)
    lastName = models.CharField(max_length=50, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    homeTown = models.CharField(max_length=250, null=True, blank=True)
    homeCountry = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)

    def __str__(self):
        return " ".join([self.firstName, self.lastName])
    
class Beyblade(BaseModel):
    WHEELS = (
        ('Storm', 'Storm'),
        ('Dark', 'Dark'),
        ('Rock', 'Rock'),
        ('Flame', 'Flame'),
        ('Lightning', 'Lightning'),
        ('Earth', 'Earth'),
        ('Killer', 'Killer'),
        ('Thermal', 'Thermal'),
        ('Burn', 'Burn'),
        ('Poison', 'Poison'),
        ('Galaxy', 'Galaxy'),
        ('Gravity', 'Gravity'),
        ('Cyclone', 'Cyclone'),
        ('Cyber', 'Cyber'),
        ('Hell', 'Hell'),
        ('Bassalt', 'Bassalt'),
    )
    SPINDIRECTION = (
        ('Clockwise', 'Clockwise'),
        ('Counter-clockwise', 'Counter-clockwise'),
        ('Variable', 'Variable'),
    )
    TYPE = (
        ('Balance', 'Balance'),
        ('Defense', 'Defense'),
        ('Attack', 'Attack'),
        ('Stamina', 'Stamina'),
    )
    faceBolt = models.CharField(max_length=100, null=True, blank=True)
    fusionWheel = models.CharField(
        max_length=100, null=True, blank=True, choices=WHEELS
    )
    spinDirection = models.CharField(
        max_length=100, null=True, blank=True, choices=SPINDIRECTION
    )
    type = models.CharField(
        max_length=100, null=True, blank=True, choices=TYPE
    )
    weightGrams = models.FloatField(null=True, blank=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    release_date = models.DateField(null=True,blank=True)
    abilities = models.CharField(max_length=250, null=True, blank=True)
    image = models.ImageField(upload_to="files/images", null=True, blank=True)
    
    def __str__(self):
        return " ".join([self.fusionWheel, self.faceBolt])

class Collection(BaseModel):
    beyblade = models.ForeignKey(Beyblade, blank=True, null=True, on_delete=models.CASCADE)
    
    player = models.ForeignKey(
        Player, blank=True, null=True, on_delete=models.CASCADE
    )
    acquisition_date = models.DateField()
