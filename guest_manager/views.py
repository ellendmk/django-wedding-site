from django.shortcuts import render
import random
from guest_manager.forms import RSVPForm,RSVPForm_message
# Create your views here.from django.shortcuts import redirect
from django.shortcuts import redirect
import datetime
from dateutil.relativedelta import relativedelta

from guest_manager.models import guests, families
import plotly.offline as opy
import plotly.graph_objs as go




def index(request):
    """View function for home page of site."""

    return render(request, 'index.html')

def invite(request,id_):
    fam_id = families.objects.get(url_suffix=id_)
    child_allowed=fam_id.child_allowed
    fam_details = guests.objects.filter(family_id=fam_id.family_id)
    fun_invite = fam_details[0].fun
    
    invite_text =""
    fun_text = ["At our wedding we promise\nyou won't ever forget\nthe parts you remember", 
                "Love truly\ndrink deeply\n& dance badly",
                "Good food\nGreat music\nBad dancing",
                "Come for the love\nStay for the party"]
    formal_text = ["Come for the love\nStay for the party",
                   "Good food\nGreat music\nBad dancing"]
    
    child_allowed_text = ""
    if child_allowed !=0:
        child_allowed_text = ("We wish we could include all children,\nbut are unfortunately only able to invite immediate family.").upper()
    
    if fun_invite:
        invite_text=random.choice(fun_text)
    else:
        invite_text=random.choice(formal_text)
    fam_size = len(fam_details)
    names=[]
    kids=[]
    for member in fam_details:
        names.append(member.name)
        kids.append(member.child)
    totalNames=len(names)
    forms=RSVPForm(names=names,fun=fun_invite,kids=kids,fam_id=fam_id.family_id)
    
    rsvp_container=""
    response=""
    submit=False

    if(fam_size==4) or (fam_size==3):
        rsvp_container="grid-split-2"
    else:
        rsvp_container="grid-split"

    if request.method == "POST":
        allPost=request.POST
        message=request.POST.get('message')
        response="Thanks for your response!\nWe can't wait to share\nthis special day with you."
        attend_count=0
        for name in names:
            person = guests.objects.get(family_id=fam_id.family_id,name=name)
            if allPost[name]=="1":
                person.attending = 1
                attend_count+=1
            else:
                person.attending = 0
            print(message)
            person.responded =1
            person.message = message
 
            person.save()
        if(attend_count<len(names) and attend_count>0):
            response=("Thanks for your response!\nWe can't wait to share\nthis special day with you.\nSorry some of you can't make it.")
        elif (attend_count)==0:
            response=("Thanks for your response!\nWe're sorry you can't make it!")
        submit=True
        rsvpform=RSVPForm(names=names,fun=fun_invite,kids=kids,fam_id=fam_id.family_id)
        context = {
        'anchor':'rsvp',
        'submit':submit,
        'response':response,
        'invite_text':invite_text,
        'rsvp_url':'/rsvp/'+str(id_),
        'details_url':'/details/'+str(id_),
        'invite_url':'/invite/'+str(id_),
        'names_list': names,
        'rsvp_message': RSVPForm_message(),
        'rsvp_form': rsvpform,
        'rsvp_form_names': zip(names,forms),
        'submit_url': '/invite/'+str(id_),
        'rsvp_container':rsvp_container,
        'rsvp_nums':totalNames,
        'child_text':child_allowed_text,
        'anchor':"rsvp",
        }
        return render(request, 'index.html',context)

    context = {
    'anchor':False,
    'submit':submit,
    'response':response,
    'invite_text':invite_text,
    'rsvp_url':'/rsvp/'+str(id_),
    'details_url':'/details/'+str(id_),
    'invite_url':'/invite/'+str(id_),
    'names_list': names,
    'rsvp_form_names': zip(names,forms),
    'rsvp_message': RSVPForm_message(),
    'rsvp_form': RSVPForm(names=names,fun=fun_invite,kids=kids,fam_id=fam_id.family_id),
    'submit_url': '/invite/'+str(id_),
    'rsvp_container':rsvp_container,
    'rsvp_nums':totalNames,
    'child_text':child_allowed_text,
    }
    return render(request, 'index.html',context)

def rsvp_viewer(request):
    #filter guests by responded true
    responses=guests.objects.filter(responded=True)
    total=responses.count()
    x=['yes','no']
    attending=[]
    attend_m=[]
    not_attending=[]
    not_attend_m=[]
    famids_notattend=[]
    famids_attend=[]
    for member in responses:
        if (member.attending == True):
            attending.append(member.name)
            attend_m.append(member.message)
            famids_attend.append(member.family_id)
        elif (member.attending == False):
            not_attending.append(member.name)
            not_attend_m.append(member.message)
            famids_notattend.append(member.family_id)
    a=responses.filter(attending=True).count()
    children=(responses.filter(attending=True)).filter(child=True).count()
    no_children=(responses.filter(attending=False)).filter(child=True).count()
    y=[a,total-a]
    hover=["children: "+str(children),"children:"+str(no_children)]
    
    trace1 = go.Bar(
            x=x, y=y,
            text=y,
            textposition='auto',
            hovertext=hover)


    data=go.Data([trace1])
    layout=go.Layout(title="RSVP summary", xaxis={'title':'Attending'}, yaxis={'title':'# guests'})
    figure=go.Figure(data=data,layout=layout)
    div = opy.plot(figure, auto_open=False, output_type='div')

    context={
        'total_invites':guests.objects.count(),
        'total_responses':total,
        'attending_list':zip(attending,famids_attend,attend_m),
        'not_attending_list':zip(not_attending,famids_notattend,not_attend_m),
        'graph':div,
    }
    return render(request, 'rsvp_viewer.html',context)


def details(request,id_):

    fam_id = families.objects.get(url_suffix=id_)
    fam_details = guests.objects.filter(family_id=fam_id.family_id)
    fam_size = len(fam_details)
    names=[]
    for member in fam_details:
        names.append(member.name)
    
    context= {
        'names_list': names,
        'rsvp_url':'/rsvp/'+str(id_),
        'details_url':'/details/'+str(id_),
        'invite_url':'/invite/'+str(id_),
        'forms.rsvp': RSVPForm(names=names,fun=fun_invite,kids=kids,fam_id=fam_id.family_id),
        }

    attend = request.POST.get('rsvp')
    print(attend)
    return render(request, 'details.html',context)
