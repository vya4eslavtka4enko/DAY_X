from django.shortcuts import render
import matplotlib.pyplot as plt
import pandas as pd
import csv
from .forms import FileForm


# Global var
DATA = []



def main(request):
    context = {}
    context['form'] = FileForm()
    if request.method == "POST":
        path=request.POST
        open_csv_file(request, path['CSV_FILES'])
    return render(request,'main.html',{'context':context,
                                                            'DATA':DATA})


def open_csv_file(request,filepath):
    DATA = pd.read_csv(filepath,sep=';')







