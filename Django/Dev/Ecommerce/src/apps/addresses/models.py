from django.db import models
from ..billing.models import BillingProfile

ADDRESS_TYPES = (
    ('billing', 'Billing address'),
    ('shipping', 'Shipping address'),
)

class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=models.CASCADE)
    # name            = models.CharField(max_length=120, null=True, blank=True, help_text='Shipping to? Who is it for?')
    # nickname        = models.CharField(max_length=120, null=True, blank=True, help_text='Internal Reference Nickname')
    address_type    = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    address_line_1  = models.CharField(max_length=120)
    address_line_2  = models.CharField(max_length=120, null=True, blank=True)
    city            = models.CharField(max_length=120)
    country         = models.CharField(max_length=120, default='United States of America')
    state           = models.CharField(max_length=120)
    postal_code     = models.CharField(max_length=120)
    
    def __str__(self):
        # if self.nickname:
        #     return str(self.nickname)
        return str(self.billing_profile)

    def get_address(self):
        return "{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
            line1=self.address_line_1,
            line2=self.address_line_2 or "",
            city=self.city,
            state=self.state,
            postal=self.postal_code,
            country=self.country
        )
            # for_name=self.name or "",
