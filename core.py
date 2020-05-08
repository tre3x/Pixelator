from PIL import Image
def run(link,n, imageid):
    img = Image.open(link)
    imgSmall = img.resize((n,n), resample = Image.ANTIALIAS)
    finalimg = imgSmall.resize(img.size, Image.NEAREST)
    outputfilename = "output" + imageid + ".png"
    finalimg.save("static/output/" + outputfilename,"PNG")
    return(outputfilename)
