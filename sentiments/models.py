from django.db import models

# class Tag(models.Model):
#     tagword = models.CharField(max_length=50, null=True, blank=True)

#     def __unicode__(self):
#         return self.tagword

#     class Meta:
#         ordering = ('tagword',)



class Post(models.Model):
    POSITIVE = 'POS'
    NEGATIVE = 'NEG'
    NEUTRAL = 'NEU'
    SENTM_CHOICES = (
            (POSITIVE, 'Positive'),
            (NEGATIVE, 'Negative'),
            (NEUTRAL, 'Neutral'),
    )

    timestamp = models.CharField(max_length=50)
    poster = models.CharField(max_length=100)
    statement = models.TextField()
    tags = models.CharField(max_length=50, null=True, blank=True)
    #Positive/Negative
    sentiment = models.CharField(max_length=3, choices=SENTM_CHOICES, null=True, blank=True)
    #Positive/Negative % value
    value = models.DecimalField(max_digits=19, decimal_places=10, null=True, blank=True)


    def __unicode__(self):
        return u'%s %s %s' % (self.statement, self.sentiment, self.tags)