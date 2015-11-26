from oidc_provider.lib.claims import AbstractScopeClaims
from allauth import socialaccount

# This class returns information from the social network identidy provider and 
# information about the user's group membership as extra scope claims

class ExtraScopeClaims(AbstractScopeClaims):

    def setup(self):
        # Here you can load models that will be used
        # in more than one scope for example.

        pass

    # return information from social identity provider
    def scope_social(self, user):

        self.social_account = socialaccount.models.SocialAccount.objects.get(user_id = user.id)
        self.extra_data = self.social_account.extra_data
        self.social_provider = self.social_account.provider
        dic = {
            'provider': self.social_provider,
        }
        dic.update(self.extra_data)
        return dic
    
    # return information about user's group membership
    def scope_groups(self,user):
        self.user_groups = []
        for a in user.groups.all():
            self.user_groups.append(a.name)
        dic = {'groups': ",".join(self.user_groups)}    
        return dic
        