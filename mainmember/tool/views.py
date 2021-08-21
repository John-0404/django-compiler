from django.db import models
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Tool
# Create your views here.

class ToolCreateView(CreateView):
    model = Tool
    fields = ['text']
    template_name = 'tool/tool_create.html'

    def form_valid(self, form):
        # obj = Tool.objects.get(pk=1)
        # print (obj.text)
        form.instance.edited_text = call_tool(form.instance.text)
        return super().form_valid(form)

class ToolDetailView(DetailView):
    model = Tool
    template_name = 'tool/tool_detail.html'

def about(request):
    return render(request, 'tool/about.html', {'title': 'About'})

#import
import json #,requests
from subprocess import Popen, PIPE, STDOUT

def call_tool(string):
    command = ["python", "/home/meedee/Desktop/project/call_tool/script.py", string]
    #command = ["g++ script.cpp -o src && ./src"]
    
    try:
        process = Popen(command, stdout=PIPE, stderr=STDOUT)
        output = process.stdout.read()
        output = str(output, 'utf-8')
        exitstatus = process.poll()
        if (exitstatus==0):
            return output
        else:
            print ("status: Failed@", "output:",str(output))
    except Exception as e:
        print ("status: failed!", "output:",str(e))
