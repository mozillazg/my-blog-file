# [web.py]上传图片并生成略缩图


生成略缩图时，用到了第三方库 [PIL(Python Imaging Library)](http://www.pythonware.com/products/pil/) 。

## upload.py

    import web
    import Image
    
    urls = ('/upload', 'Upload')
    render = web.template.render('templates/',)
    class Upload:
    
        def GET(self):
            web.header("Content-Type","text/html; charset=utf-8")
            return render.upload('')
    
    
        def POST(self):
            x = web.input(myfile={})
            filedir = './static' # change this to the directory you want to store the file in.
            if 'myfile' in x: # to check if the file-object is created
                filepath=x.myfile.filename.replace('\\','/') # replaces the windows-style slashes with linux ones.
                filename=filepath.split('/')[-1] # splits the and chooses the last part (the filename with extension)
                fout = open(filedir +'/'+ filename,'wb') # creates the file where the uploaded file should be stored
                fout.write(x.myfile.file.read()) # writes the uploaded file to the newly created file.
                fout.close() # closes the file, upload complete.

                infile = filedir +'/'+filename
                outfile = infile + ".thumbnail"
                im = Image.open(filedir +'/'+filename)
                im.thumbnail((128, 128))
                im.save(outfile, im.format)

            return render.upload(outfile)
    
    if __name__ == "__main__":
       app = web.application(urls, globals()) 
       app.run()
    

## upload.html

    $def with(src)
    
    <html><head></head><body>
    <form method="POST" enctype="multipart/form-data" action="">
    <input type="file" name="myfile" />
    <br/>
    <input type="submit" />
    </form>
    $if src:
        <img src="$src" />
    </body></html>
    
##参考

* [Web.py Cookbook(File Upload)](#)
* [Web.py Cookbook(Store an uploaded file)](#)
* [pil-handbook(Reading and Writing Images)](#)



