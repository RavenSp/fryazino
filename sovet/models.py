from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class okrug(models.Model):

    title = models.CharField(max_length=50, verbose_name='Наименование')
    description = RichTextUploadingField(verbose_name='Описание округа')
    slug = models.SlugField(max_length=50, verbose_name='URL')

    class Meta:

        verbose_name = 'Округ'
        verbose_name_plural = 'Округа'

    def __str__(self):
        return self.title

class party(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название субъекта выдвижения')
    slug = models.SlugField(max_length=50, verbose_name='URL')

    class Meta:
        verbose_name_plural = 'Субъекты выдвижения'
        verbose_name = 'Субъект выдвижения'

    def __str__(self):
        return self.title



class deputat(models.Model):

    image = models.ImageField(upload_to='uplaods/sovet', verbose_name='Фото депутата', blank=True)
    first_name = models.CharField(max_length=255, verbose_name='Фамилия')
    last_name = models.CharField(max_length=255, verbose_name='Имя')
    middle_name = models.CharField(max_length=255, verbose_name='Отчество', blank=True, null=True)
    okrug = models.ForeignKey(okrug, verbose_name='Округ', on_delete=models.PROTECT)
    party = models.ForeignKey(party, verbose_name='Субъект выдвижения', on_delete=models.PROTECT)
    bDate = models.DateField(verbose_name='Дата рождения', blank=True, null=True)
    bio = RichTextUploadingField(verbose_name='Биография депутата', blank=True, null=True)
    phones = models.CharField(max_length=256, verbose_name='Контактные телефоны', blank=True, null=True)
    email = models.EmailField(verbose_name='E-mail депутата', default='sovet@fryazino.org')
    grafic = RichTextUploadingField(verbose_name='График приёма', blank=True, null=True)
    chairman = models.BooleanField(verbose_name='Председатель Совета', help_text='Председателем может быть только один депутат.', default=False)


    class Meta:

        verbose_name = 'Депутат'
        verbose_name_plural = 'Депутаты'

    def __str__(self):
        if self.middle_name:
            fio =  "%s %s %s" % (self.first_name.capitalize(), self.last_name.capitalize(), self.middle_name.capitalize())
        else:
            fio = "%s %s" % (self.first_name.capitalize(), self.last_name.capitalize())
        if self.chairman:
            fio += ' - председатель Совета'
        return fio

    def save(self, *args, **kwargs):

        if self.chairman:
            try:
                tmp = deputat.objects.get(chairman=True)
                if self != tmp:
                    tmp.chairman = False
                    tmp.save()

            except deputat.DoesNotExist:
                pass
        super(deputat, self).save(*args, **kwargs)


class commision(models.Model):

    COMTYPE = [
        ('CM', 'Комиссия'),
        ('WG', 'Рабочая группа'),
        ('OT', 'Иное')
    ]

    title = models.CharField(max_length=255, verbose_name='Название комиссии')
    description = models.TextField(verbose_name='Описание комисси')
    slug = models.SlugField(max_length=255, verbose_name='URL')
    tcom = models.CharField(max_length=2, verbose_name='Тип комиссии', choices=COMTYPE)
    chairman = models.ForeignKey(deputat, verbose_name='Председатель комиссии', on_delete=models.PROTECT, related_name='depchairman')
    members = models.ManyToManyField(deputat, verbose_name='Члены комисии', related_name='depmembers')

    class Meta:

        verbose_name = 'Комиссия'
        verbose_name_plural = 'Комисии'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        super(commision, self).save(*args, **kwargs)

        if self.chairman not in self.members.all():

            self.members.add(self.chairman)

            super(commision, self).save(*args, **kwargs)





