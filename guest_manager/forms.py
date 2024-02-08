from django import forms

class RSVPForm(forms.Form):
	def __init__(self, *args, **kwargs):
		names = kwargs.pop('names')
		fun = kwargs.pop('fun')
		kids = kwargs.pop('kids')
		fam_id = kwargs.pop('fam_id')

		attend_choices=(('1',("Ready to eat, drink, and see you get married!").upper()),
				('0',("Will toast to you from afar").upper()),)
		attend_choices_kids=(('1',("Can't wait to play with the cousins!").upper()),
				('0',("Sad to miss all the fun").upper()),)
		if fun==1:
			attend_choices=(('1',("Ready to eat, drink, and see you get married!").upper()),
				('0',("Will toast to you from afar").upper()),)
			attend_choices_kids=(('1',("Can't wait to play with the cousins!").upper()),
				('0',("Sad to miss all the fun").upper()),)
		if fam_id == 21:
			attend_choices_kids=(('1',("Can't wait to dance!").upper()),
				('0',("Sad to miss all the fun").upper()),)


		super(RSVPForm, self).__init__(*args, **kwargs)
		counter = 1
		for q in range(0,len(names)):
			print(kids[q])
			if kids[q]==1:
				self.fields[names[q]] = forms.ChoiceField(widget=forms.RadioSelect, choices=attend_choices_kids,label=names[q].upper())
				# self.fields[names[q]].widget.attrs.update({'class':'checkmark input'})
			else:
				self.fields[names[q]] = forms.ChoiceField(widget=forms.RadioSelect, choices=attend_choices,label=names[q].upper())
				# self.fields[names[q]].widget.attrs.update({'class':'checkmark input'})

			counter += 1

# class RSVPForm(forms.Form):

# 	attend_choices=(('1',"Attending"),
# 					('0',"Not attending"),)
# 	diet_choices=(('none',"No requirements"),
# 		('veg',"Vegetarian"),
# 		('vegan',"Vegan"),)
# 	attending=[]
# 	for i in range(0,10):
# 		attending.append(forms.ChoiceField(widget=forms.RadioSelect, choices=attend_choices))
# 	# diet = forms.ChoiceField(choices=diet_choices)
	
class RSVPForm_message(forms.Form):
	# message = forms.CharField(max_length=1000,required = False,widget=forms.Textarea(attrs={'rows':7, 'cols':20}))
	# def __init__(self,*args,**kwargs):
	# 	self.mobile = kwargs.pop('mobile')
	# 	super(RSVPForm_message,self).__init__(*args,**kwargs)
		
			# message = forms.CharField(max_length=1000,required = False,widget=forms.Textarea(attrs={'rows':7, 'cols':20}))
		# else:
	message = forms.CharField(max_length=1000,required = False,widget=forms.Textarea(attrs={'placeholder':'Message...','rows':6, 'cols':18}))