from django.shortcuts import render, redirect

# from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
import pandas as pd
from .forms import *
from .FileHandler import *

from sok_website.settings import BASE_DIR, DEBUG, MEDIA_ROOT, STATICFILES_DIRS
from wsgiref.util import FileWrapper
from pathlib import Path
import random
import mimetypes
from django.utils.html import format_html
from django.utils.datastructures import MultiValueDictKeyError
queryChannels=["Yleinen","Huolto","AsPa","Myynti"]
allowed_types=["jpg","JPG","png","PNG","svg","jpeg","JPEG","bmp","webp","GIF","gif"]
def index(request):
    return render(request, "index.html")



def render_gallery(request,path=MEDIA_ROOT / "gallery",back_path=""):
    
    
    
    #           [completefilename for src, imagename,                         type/extension, id]
    
    image_files = [str(i).split("gallery")[-1][1:].replace("/","/") for i in path.iterdir() if str(i).split('.')[-1]in allowed_types ]
    image_names = [str(i).split("/")[-1].split('.')[0] for i in path.iterdir() if str(i).split('.')[-1]in allowed_types ]
    types = [str(i).split('.')[-1] for i in path.iterdir() if str(i).split('.')[-1]in allowed_types ]
    
    dataframe=pd.DataFrame({
        "filename":image_files,
        "name":image_names,
        "type":types,
    }).astype({"filename":str,"type":str},errors='raise')

    dataframe['name']=dataframe['name'].astype("string")
    dataframe['filename']=dataframe['filename'].astype("string")
    dataframe['type']=dataframe['type'].astype("string")

    print(dataframe.dtypes)
    
    
    dataframe.sort_values(by='filename', inplace=True, key=lambda col: col.str.lower())
        #dataframe.iloc[dataframe['name'].str.lower().argsort()]
        #dataframe.sort_values("name",ascending=True,inplace=True)
    folders = [str(i).split("gallery")[-1][1:].replace("\\",":").replace(" ","%").replace("\'","&").replace("\\","/") for i in path.iterdir() if i.is_dir() ]
    folder_names = [str(i).split("\\")[-1] for i in path.iterdir() if i.is_dir() ]
    print(folders)
    folder_types=["folder" for i in path.iterdir() if i.is_dir()]
    
    image_files=folders+list(dataframe["filename"])
    image_names=folder_names+list(dataframe["name"])
    types=folder_types+list(dataframe["type"])
    
    
    
    # if the file is text file we replace the source file path with the content string
    
    rows = []
    
    while image_files != []:
        rows.append(zip(image_files[:4],image_names[:4],types[:4]))
        image_files = image_files[4:]
        image_names = image_names[4:]
        types = types[4:]
        
    

    
    

    context = {"form":uploadNote(),"photo":uploadPhotoNote(),"rows": rows, "back_path":back_path}
    
    return render(request, "gallery.html", context)

def gallery(request,folder = ""):
    path = MEDIA_ROOT/"gallery"
    string="jee#jee"
    back_path=""
    if folder !="":
        print(folder)
        folder=folder.replace(":","/").replace("%"," ").replace("&","\'")
        path=path/folder
        print()
        print(folder,string.replace("#","\'"))
        print()
        back_path="/".join(folder.split("/")[:-1])
    if request.method == "GET":
        
        return render_gallery(request,path=path,back_path=back_path)
    elif request.method == "POST":
        photoform = uploadPhotoNote(request.POST,request.FILES)
        
        textform = uploadNote(request.POST)
        if(textform.is_valid()):
            handle_textnote(textform.data)
            response = redirect(reverse('gallery', kwargs={'folder':textform.data['folder']}))
            return response
            
        elif(photoform.is_valid()):
            handle_photonote(photoform.data,request.FILES['kuva'])
            response = redirect(reverse('gallery', kwargs={'folder':photoform.data['folder']}))
            return response
            
        else:
            # this is redundant and old
            try:
                selectedchannels=[request.POST['folder']]
                return render_gallery(request,selectedchannels,sortingmethod=request.POST['folder'])
            except MultiValueDictKeyError:
                response = redirect(reverse('gallery', kwargs={'folder':photoform.data['folder']}))
                return response
            

def image(request, file):
    print(file)
    path = BASE_DIR/file.replace(":","/").replace("%"," ").replace("&","\'")
    
    file=str(path).split("/")[-1]
    name=str(path.resolve().stem)
    directory=path.resolve().parent
    folder = str(str(directory).split("gallery")[-1]).replace("\\","/")
    image_files = [str(i).split("/")[-1] for i in directory.iterdir() if str(i).split('.')[-1]in allowed_types ]
    image_files.sort()
    current_index = image_files.index(str(file))
    

    next_index,previous_index=current_index+1,current_index-1
    if next_index == len(image_files):
        next_index=0
    if previous_index==-1:
        previous_index=len(image_files)-1
    #print(str(image_files[next_index]))
    next_url = folder+"/"+str(image_files[next_index])
    previous_url=folder+"/"+str(image_files[previous_index])
    image_path=str(path).split("gallery")[-1][1:] 
    return_url = "/".join(str(path).split("gallery")[-1][1:].split("\\")[:-1])
    #print(return_url)
    return render(request, 'image.html',{'path':image_path,'return_url':return_url,'next_url':next_url,'previous_url':previous_url,'name':name[-7:]})