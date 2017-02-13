from django.test import TestCase
from account.models import Account
from django.utils import timezone
import datetime
from django.core.urlresolvers import reverse
from account.forms import AccountForm
from django.template import Template, Context

# models test
class AccountTest(TestCase):

    def create_account(self, username="username123", num=37, birthday=datetime.datetime.now()):
        return Account.objects.create(username=username, num=num, birthday=birthday)

    def test_account_creation(self):
        acct = self.create_account()
        self.assertTrue(isinstance(acct, Account))

class BizzFuzzTagTest(TestCase):

    TEMPLATE = Template("{% load bizzfuzz %} {{ num | bizzfuzz }}")

    def test_entry_for_bizz(self):
        rendered = self.TEMPLATE.render(Context({'num': 18}))
        self.assertIn('Bizz', rendered)

    def test_entry_for_fuzz(self):
        rendered = self.TEMPLATE.render(Context({'num': 10}))
        self.assertIn('Fuzz', rendered)

	def test_entry_for_bizzfuzz(self):
		rendered = self.TEMPLATE.render(Context({'num': 30}))
		self.assertIn('BizzFuzz', rendered)

    def test_entry_for_other(self):
        rendered = self.TEMPLATE.render(Context({'num': 19}))
        self.assertIn('19', rendered)

class EligibleTagTest(TestCase):

    TEMPLATE = Template("{% load eligible %} {{ birthday | eligible }}")

    def test_entry_for_bizz(self):
        birthday = datetime.datetime.now() - datetime.timedelta(days=365*18)
        rendered = self.TEMPLATE.render(Context({'birthday': birthday}))
        self.assertIn('allowed', rendered)

    def test_entry_for_fuzz(self):
        birthday = datetime.datetime.now() - datetime.timedelta(days=365*11)
        rendered = self.TEMPLATE.render(Context({'birthday': birthday}))
        self.assertIn('blocked', rendered)

