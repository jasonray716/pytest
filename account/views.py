# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from account.models import Account
from django.template import RequestContext
from datetime import datetime, timedelta

def getAllAccounts():
	try:
		accounts = Account.objects.all()
	except Account.DoesNotExist:
		accounts = None
	return accounts


def getAccountById(id_account):
	try:
		art = Account.objects.get(pk=id_account)
	except Account.DoesNotExist:
		art = None
	return art


def index(request):
	accounts = getAllAccounts()
	ctx ={
		"accounts" : accounts
	}
	return render_to_response("index.html", ctx)


def newAccount(request):
	from account.forms import AccountForm
	if request.method == "POST":
		form = AccountForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/#account")
	else:
		form = AccountForm()
	ctx ={
		"form": form
	}
	return render_to_response("form.html", ctx, context_instance=RequestContext(request))


def editAccount(request, id_account):
	art = getAccountById(id_account)
	from account.forms import AccountForm
	if request.method == "POST":
		form = AccountForm(request.POST, instance=art)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/#edit")
	else:
		if art:
			form = AccountForm(instance=art)
		else:
			return HttpResponseRedirect("/#no-exist-such-account")
	ctx ={
		"form": form
	}
	return render_to_response("form.html", ctx, context_instance=RequestContext(request))


def deleteAccount(request, id_account):
	art = getAccountById(id_account)
	if art:
		art.delete()
		return HttpResponseRedirect("/#delete")
	return HttpResponseRedirect("/#no-account-to-delete")

