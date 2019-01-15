"""
Copyright (c) 2019 Mathias Yde

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from os import listdir #List directory


#Replace this string variable below, if you have a different installation for SAI.
#If you don't know how to do that, please follow the instructions below:
#1. In file explorer, find your folder with the SAI program in. (The one with sai.exe in)
#2. Copy the text just above "Name". (The directory/path)
#3. Paste it between the quotation marks. ("")
#4. Change any back slashes to forward slashes. (\ -> /)
#5. If there's not a forward slash before the last quotation mark, please add one.
#It should look like this: "<DIRECTORY>/PaintToolSAI/"
root_folder = "C:/PaintToolSAI/"

#These are surfixes for root_folder ("C:/PaintToolSAI/<folder>/")
folders = ["blotmap/","brushtex/","elemap/","papertex/"]

for folder in folders: #Runs for every folder
    if folder == "brushtex/":
        conf_file = "brushtex.conf"

    if folder == "papertex/":
        conf_file = "papertex.conf"

    if folder == "blotmap/":
        conf_file = "brushform.conf"
        
    if folder == "elemap/":
        conf_file = "brushform.conf"

    print(folder)
    with open(root_folder + conf_file, "a") as cf: 
        for file in listdir(root_folder + folder):
            if folder == "brushtex/":
                print("      "+file)
                cf.write("1,"+folder+file+"\n")

            if folder == "papertex/":
                print("      "+file)
                cf.write("1,"+folder+file+"\n")

            if folder == "blotmap/":
                print("      "+file)
                cf.write("1,"+folder+file+"\n")
        
            if folder == "elemap/":
                print("      "+file)
                cf.write("2,"+folder+file+"\n")

    cf.close()
