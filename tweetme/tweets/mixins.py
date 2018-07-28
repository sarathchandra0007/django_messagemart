from django import forms
from django.forms.utils import ErrorList

class FormUserNeededMixin(object):
    def form_valid(self,form):
        if self.request.user.is_authenticated():
        # print (self.request.user)#anonymus if not loggedin
        # print (form.instance.user)#Sarathchandra beacause models default user is Sarathchandra
            form.instance.user=self.request.user
            return super(FormUserNeededMixin,self).form_valid(form)
        else:
            form._errors[forms.forms.NON_FIELD_ERRORS]=ErrorList(["User must be uthenticated"])   #error warning if not uthenticated
            return self.form_invalid(form)
