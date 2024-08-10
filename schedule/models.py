from django.db import models

# Create your models here.
class YogaStyle(models.Model):
    RESTORATIVE = "REST"
    YIN = "YIN"
    GENTLE = "GENTLE"
    BEGINNERS = "BEGINNERS"
    FLOW1 = "FLOW1"
    FLOW2 = "FLOW2"
    FLOW_MIXED_LEVEL = "MIXED"
    EXPRESS_LUNCHTIME = "EXPRESS"
    PRENATAL = "PRENATAL"
    STYLE_CHOICES = [
        (RESTORATIVE, "Restorative Yoga"),
        (YIN, "Yin Yoga"),
        (GENTLE, "Gentle Yoga"),
        (BEGINNERS, "Beginners' Yoga"),
        (FLOW1, "Yoga Flow Level 1"),
        (FLOW2, "Yoga Flow Level 2"),
        (FLOW_MIXED_LEVEL, "Yoga Flow Mixed Level"),
        (EXPRESS_LUNCHTIME, "Express Lunchtime Yoga"),
        (PRENATAL, "Prenatal Yoga")
    ]
    group_class_style = models.CharField(max_length=10, choices=STYLE_CHOICES, default=FLOW_MIXED_LEVEL)

    def __str__(self):
        return str(self.group_class_style)


class StyleDescription(models.Model):
    RESTORATIVE_D = "Restorative yoga is a slow, gentle practice using props "
    "(bolsters, blankets and blocks) to prop the body up in poses "
    "allowing the whole body to enter and remain in a deeply relaxed "
    "state. An active rest practice, there is no muscle contraction in "
    "restorative yoga with practitioners relaxing fully in the stretch "
    "so that tension can slowly be released. Restorative yoga enhances "
    "flexibility, deeply relaxes the body and aids better sleep by "
    "stilling the mind."
    YIN_D = "Yin Yoga is a perfect complement to the dynamic and muscular "
    "(yang) styles of yoga that emphasise internal heat, and the "
    "lengthening and contracting of our muscles. Yin Yoga generally "
    "targets the connective tissues of the hips, pelvis, and lower spine. "
    "While initially, this style of yoga can seem quite passive, or soft, "
    "yin practice can be quite challenging due to the longer duration of the "
    "poses. Yin and yang tissues respond quite differently to being exercised. "
    "You need to experience this to really know what Yin Yoga is all about."
    "\n**Not suitable for prenatal students**"
    GENTLE_D = "Gentle Yoga Flow is a unique sequence of movements and postures "
    "which flow together creating heat in the body as well as peace of mind. "
    "It is particularly suitable to those seeking to improve their strength, "
    "flexibility, health and general well-being. "
    "\n**Not suitable for prenatal students**"
    BEGINNERS_D = "The beginners yoga class is a great way to start your "
    "yoga journey. Students will learn yogic breathing, yoga "
    "postures, and relaxation techniques. It is the perfect class to "
    "build a strong foundation for yourself. The beginners yoga class "
    "is there to help you feel safe and supported in your practice. "
    "This class will help you build strength and mobility as well as "
    "cultivate a calmer mind. "
    "\n**Not suitable for prenatal students**"
    FLOW1_D = "This class is suitable for complete beginners and students who want "
    "to learn more about proper alignment in the poses. We spend more time "
    "instructing the poses and breathing techniques. The pace is gentle enough, but "
    "the class can still be challenging, helping you to build up strength. "
    "This is also a great option if you are low on energy, or if you are "
    "recovering from an injury and need to take it easy."
    "\n**Not suitable for prenatal students**"
    FLOW2_D = "You will need a yoga foundation, this class is for those "
    "improving their practice, but not for those who are new to yoga. "
    "Ideal for anyone who wishes to prevent common misalignment in poses, "
    "refine transitions and establish a solid foundation for a steady development "
    "of practice. A Level 2 class gives you the option for a more challenging poses "
    "with space for deep relaxation, flexibility work and strength work."
    "\n**Not suitable for complete beginners or prenatal students**"
    FLOW_MIXED_LEVEL_D = "This class is designed to take you deeper into your practice "
    "by introducing asanas which will challenge you equally on "
    "strength and flexibility. Each class combines a dynamic "
    "Vinyasa practice with meditation, hands-on alignment and "
    "deep relaxation. "
    "\n**Not suitable for complete beginners or prenatal students**"
    EXPRESS_LUNCHTIME_D = "Make the most of your lunch break with an invigorating and "
    "rejuvenating midday yoga class to keep you going all day long. "
    "This class is designed as a yoga flow and moving meditation. Go "
    "back to your desk, children, errands or other daily activities with "
    "a clear mind and feeling energised! "
    "\nAll levels are welcome. "
    "\n**Not suitable for complete beginners or prenatal students**"
    PRENATAL_D = "During pregnancy your body goes through many changes, which "
    "creates stress on you mentally and physically. A way to maintain a healthy "
    "mind and body is prenatal yoga. "
    "\nPrenatal yoga focuses on poses for pregnant women, in order to increase "
    "strength and flexibility. It also helps pregnant women to develop proper "
    "breathing and relaxation techniques for easier and more comfortable labor. "
    "\nThis class is for prenatal women after 12 weeks/1st trimester without contra-indications"
    DESCTIPTION_CHOICES = [
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
    group_class_description = models.TextField(choices=DESCTIPTION_CHOICES, default=FLOW_MIXED_LEVEL_D)

    def __str__(self):
        return str(self.group_class_description)


