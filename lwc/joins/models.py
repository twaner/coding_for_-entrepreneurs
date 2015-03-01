from django.db import models

# Models


class Join(models.Model):
    email = models.EmailField()
    # Use related name in dot notation i.e. obj.referral
    friend = models.ForeignKey("self", related_name='referral', blank=True, null=True)
    ref_id = models.CharField(max_length=120, default='ABC', unique=True)
    ip_address = models.CharField(max_length=120, default='ABC')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.email

    class Meta:
            unique_together = ("email", "ref_id")


# class JoinFriends(models.Model):
#     # related name due to links to same object
#     email = models.OneToOneField(Join, related_name="Sharer")
#     friends = models.ManyToManyField(Join, related_name="Friend", null=True, blank=True)
#     emaillall = models.ForeignKey(Join, related_name="emailall")
#     # Can have an unlimited amount of joined friends due to FK
#
#     def __str__(self):
#         print(self.emaillall)
#         print(self.email)
#         return self.email.email