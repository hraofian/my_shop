from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.views.generic import TemplateView

def members(request): 
  mymembers = Member.objects.all().values()
  template = loader.get_template('index/all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('index/details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))


def main(request):
  template = loader.get_template('index/main.html')
  return HttpResponse(template.render())
    

  # print('request = ', request , 'context = ', context)



def testing(request):
  mydata = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))


class IndexView(TemplateView):
    template_name = 'index/index.html'