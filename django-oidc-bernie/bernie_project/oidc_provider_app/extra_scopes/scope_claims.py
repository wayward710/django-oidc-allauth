from oidc_provider.lib.claims import AbstractScopeClaims
from allauth import socialaccount
# from oidc_provider.models import *
# from allauth.socialaccount.models import SocialAccount

class ExtraScopeClaims(AbstractScopeClaims):

    def setup(self):
        # Here you can load models that will be used
        # in more than one scope for example.
        # print self.user
        # print self.scopes
        pass

    def scope_social(self, user):

        # Here you can search books for this user.

        self.social_account = socialaccount.models.SocialAccount.objects.get(user_id = user.id)
        self.extra_data = self.social_account.extra_data
        self.social_provider = self.social_account.provider
        dic = {
            'provider': self.social_provider,
        }
        dic.update(self.extra_data)
        return dic
    
    def scope_groups(self,user):
        self.user_groups = []
        for a in user.groups.all():
            self.user_groups.append(a.name)
        dic = {'groups': ",".join(self.user_groups)}    
        return dic
        