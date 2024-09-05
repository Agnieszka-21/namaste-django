from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from cloudinary.models import CloudinaryField
import uuid
# eventtool
from eventtools.models import BaseEvent, BaseOccurrence


# Create your models here.
class YogaStyle(models.Model):
    RESTORATIVE = "Restorative Yoga"
    YIN = "Yin Yoga"
    GENTLE = "Gentle Yoga"
    BEGINNERS = "Beginners' Yoga"
    FLOW1 = "Yoga Flow Level 1"
    FLOW2 = "Yoga Flow Level 2"
    FLOW_MIXED_LEVEL = "Yoga Flow Mixed Level"
    EXPRESS_LUNCHTIME = "Express Lunchtime Yoga"
    PRENATAL = "Prenatal Yoga"
    STYLE_CHOICES = [
        (RESTORATIVE, "REST"),
        (YIN, "YIN"),
        (GENTLE, "GENTLE"),
        (BEGINNERS, "BEGINNERS"),
        (FLOW1, "FLOW1"),
        (FLOW2, "FLOW2"),
        (FLOW_MIXED_LEVEL, "MIXED"),
        (EXPRESS_LUNCHTIME, "EXPRESS"),
        (PRENATAL, "PRENATAL")
    ]
    group_class_style = models.CharField(max_length=30, choices=STYLE_CHOICES, null=True, blank=True)

    def __str__(self):
        return str(self.group_class_style)



class StyleDescription(models.Model):
    RESTORATIVE_D = (
        "Restorative yoga is a slow, gentle practice using props "
        "(bolsters, blankets and blocks) to prop the body up in poses "
        "allowing the whole body to enter and remain in a deeply relaxed "
        "state. An active rest practice, there is no muscle contraction in "
        "restorative yoga with practitioners relaxing fully in the stretch "
        "so that tension can slowly be released. Restorative yoga enhances "
        "flexibility, deeply relaxes the body and aids better sleep by "
        "stilling the mind."
    )
    YIN_D = (
        "Yin Yoga is a perfect complement to the dynamic and muscular "
        "(yang) styles of yoga that emphasise internal heat, and the "
        "lengthening and contracting of our muscles. Yin Yoga generally "
        "targets the connective tissues of the hips, pelvis, and lower spine. "
        "While initially, this style of yoga can seem quite passive, or soft, "
        "yin practice can be quite challenging due to the longer duration of the "
        "poses. Yin and yang tissues respond quite differently to being exercised. "
        "You need to experience this to really know what Yin Yoga is all about. "
        "Not suitable for prenatal students."
    )
    GENTLE_D = (
        "Gentle Yoga Flow is a unique sequence of movements and postures "
        "which flow together creating heat in the body as well as peace of mind. "
        "It is particularly suitable to those seeking to improve their strength, "
        "flexibility, health and general well-being. "
        "Not suitable for prenatal students."
    )
    BEGINNERS_D = (
        "The beginners' yoga class is a great way to start your "
        "yoga journey. Students will learn yogic breathing, yoga "
        "postures, and relaxation techniques. It is the perfect class to "
        "build a strong foundation for yourself. The beginners yoga class "
        "is there to help you feel safe and supported in your practice. "
        "This class will help you build strength and mobility as well as "
        "cultivate a calmer mind. "
        "Not suitable for prenatal students."
    )
    FLOW1_D = (
        "This class is suitable for complete beginners and students who want "
        "to learn more about proper alignment in the poses. We spend more time "
        "instructing the poses and breathing techniques. The pace is gentle enough, but "
        "the class can still be challenging, helping you to build up strength. "
        "This is also a great option if you are low on energy, or if you are "
        "recovering from an injury and need to take it easy. "
        "Not suitable for prenatal students."
    )
    FLOW2_D = (
        "You will need a yoga foundation, this class is for those "
        "improving their practice, but not for those who are new to yoga. "
        "Ideal for anyone who wishes to prevent common misalignment in poses, "
        "refine transitions and establish a solid foundation for a steady development "
        "of practice. A Level 2 class gives you the option for a more challenging poses "
        "with space for deep relaxation, flexibility work and strength work. "
        "Not suitable for complete beginners or prenatal students."
    )
    FLOW_MIXED_LEVEL_D = (
        "The mixed-level class is designed to take you deeper into "
        "your practice by introducing asanas which will challenge you equally on "
        "strength and flexibility. Each class combines a dynamic "
        "Vinyasa practice with meditation, hands-on alignment and "
        "deep relaxation. "
        "Not suitable for complete beginners or prenatal students."
    )
    EXPRESS_LUNCHTIME_D = (
        "Make the most of your lunch break with an invigorating and "
        "rejuvenating midday yoga class to keep you going all day long. "
        "This class is designed as a yoga flow and moving meditation. Go "
        "back to your desk, children, errands or other daily activities with "
        "a clear mind and feeling energised! "
        "All levels are welcome. "
        "Not suitable for complete beginners or prenatal students."
    )
    PRENATAL_D = (
        "During pregnancy your body goes through many changes, which "
        "creates stress on you mentally and physically. A way to maintain a healthy "
        "mind and body is prenatal yoga. "
        "Prenatal yoga focuses on poses for pregnant women, in order to increase "
        "strength and flexibility. It also helps pregnant women to develop proper "
        "breathing and relaxation techniques for easier and more comfortable labor. "
        "This class is for prenatal women after 12 weeks/1st trimester without contra-indications."
    )
    DESCRIPTION_CHOICES = [
        (RESTORATIVE_D, "Restorative description"),
        (YIN_D, "Yin description"),
        (GENTLE_D, "Gentle description"),
        (BEGINNERS_D, "Beginners' description"),
        (FLOW1_D, "Flow 1 description"),
        (FLOW2_D, "Flow 2 description"),
        (FLOW_MIXED_LEVEL_D, "Flow Mixed description"),
        (EXPRESS_LUNCHTIME_D, "Express description"),
        (PRENATAL_D, "Prenatal description")
    ]
    group_class_description = models.CharField(max_length=5000, choices=DESCRIPTION_CHOICES, null=True, blank=True)

    def __str__(self):
        return str(self.group_class_description)


default_class_img = '../static/images/down_dog.jpg'


class GroupClass(models.Model):

    DAYS = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fri', 'Friday'),
        ('Sat', 'Saturday'),
        ('Sun', 'Sunday')
    )

    TIMES = (
        ('7.30 am', '7.30'),
        ('9 am', '9.00'),
        ('10 am', '10.00'),
        ('11 am', '11.00'),
        ('1.05 pm', '13.05'),
        ('6 pm', '18.00'),
        ('6.30 pm', '18.30'),
        ('7.15 pm', '19.15'),
        ('7.30 pm', '19.30')
    )

    DURATION_OPTIONS = (
        (45, 45),
        (60, 60)
    )

    LOCATION_OPTIONS = (
        ('Studio 1', 'Studio 1'),
        ('Studio 2', 'Studio 2')
    )

    TEACHER_OPTIONS = (
        ('Mary Dawson', 'Mary Dawson'),
        ('Joanne West', 'Joanne West')
    )

    BIO_MARY = (
        "Mary is +500-hour qualified yoga teacher. She teaches yoga with an "
        "emphasis on safety and alignment. This offers students a supportive "
        "environment to explore their personal yoga practice. Mary began practising "
        "yoga in 2012. Her interest derived from the desire to balance out a busy lifestyle. "
        "Finding a new level of stillness, she is now on a mission to share the benefits "
        "of yoga with everyone! She will continue her mission by going to training and events "
        "to improve her teaching skills."
    )

    BIO_JOANNE = (
        "Joanne's approach to teaching yoga is very much like her approach to life - full of "
        "curiosity, gentleness, and playfulness. 2014 was the beginning of her journey into a "
        "deeper understanding of herself, and this brought her to Goa, India where she completed "
        "her 200hr Yoga teacher training in 2017, and returning again in 2018 to Rishikesh to "
        "complete 100 hours of Yin, breathwork and Meditation training. Joanne's teaching style "
        "is non-judgemental and focused on helping to foster the student's unique "
        "relationship with yoga and their own bodies. She uses the fluidity of vinyasa to help "
        "awaken and inspire this connection to ourselves and to the world around us."
    )

    BIO_OPTIONS = [
        (BIO_MARY, 'Mary\'s bio'),
        (BIO_JOANNE, 'Joanne\'s bio')
    ]

    title = models.ForeignKey(YogaStyle, on_delete=models.CASCADE, related_name='title', null=True, blank=True)
    description = models.ForeignKey(StyleDescription, on_delete=models.CASCADE, null=True, blank=True)
    weekday = models.CharField(max_length=10, choices=DAYS, null=True, blank=True)
    start_time = models.CharField(max_length=10, choices=TIMES, null=True, blank=True)
    duration_mins = models.IntegerField(choices=DURATION_OPTIONS, default=60)
    location = models.CharField(choices=LOCATION_OPTIONS, default='Studio 1')
    image = CloudinaryField('image', default=default_class_img)
    participants = models.ManyToManyField(User, blank=True)
    teacher = models.CharField(choices=TEACHER_OPTIONS, max_length=100, null=True, blank=True)
    teacher_bio = models.CharField(choices=BIO_OPTIONS, max_length=3000, null=True, blank=True)
    capacity = models.IntegerField(validators=[MaxValueValidator(16)], null=True, blank=True)
    first_class = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'GroupClasses'
        ordering = ['first_class__week_day', 'start_time']

    def __str__(self):
        return f"{self.title} | {self.weekday} {self.start_time}"


class RepeatedEvent(BaseEvent):
    title = models.ForeignKey(GroupClass, on_delete=models.CASCADE)


class EventOccurrence(BaseOccurrence):
    event = models.ForeignKey(RepeatedEvent, on_delete=models.CASCADE)


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    chosen_class = models.ForeignKey(GroupClass, on_delete=models.CASCADE, null=True, blank=True)
    client = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    class_datetime = models.DateTimeField(null=True, blank=True)
    booking_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    waiver_signed = models.BooleanField(null=True, blank=True)
    booking_cancelled = models.BooleanField(default=False)

    class Meta:
        ordering = ['-booking_time']

    def __str__(self):
        return f"Booking {self.id} for {self.client} | {self.chosen_class} | {self.booking_time}"

