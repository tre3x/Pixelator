from PIL import Image 
import numpy as np
import time

def converter(link, n ,choice, imageid):
  im = Image.open(link) 


  print(im.size[0] * im.size[1], im.size[0], im.size[1])
  if(choice == 1) or (im.size[0] * im.size[1] < 490000):

    if((im.size[0] % n) > (n - (im.size[0] % n))):
      newresx = im.size[0] + (n - (im.size[0] % n))
    if((im.size[0] % n) <= (n - (im.size[0] % n))):
      newresx = im.size[0] - (im.size[0] % n)

    if((im.size[1] % n) > (n - (im.size[1] % n))):
      newresy = im.size[1] + (n - (im.size[1] % n))
    if((im.size[1] % n) <= (n - (im.size[1] % n))):
      newresy = im.size[1] - (im.size[1] % n)
  
  if(choice == 0) and (im.size[0] * im.size[1] > 490000):
    newresx = 700 - (700 % n)
    newresy = 700 - (700 % n)



  newres = (newresx , newresy)


  im_resized = np.array(im.resize(newres, Image.ANTIALIAS))

  #print(im_resized.shape)

  pixelblockcount = [int(im_resized.shape[0]/n), int(im_resized.shape[1]/n)]

  startx = 0
  endx = pixelblockcount[0]

  starty = 0
  endy = pixelblockcount[1]

  #print(endx, endy)

  starttime = time.time()

  while(endx <= im_resized.shape[0]):

        rgblist = []

        for x in range(startx, endx):
          for y in range(starty, endy):
            rgblist.append(im_resized[x][y])

        rgblist = np.array(rgblist)
        #print(np.mean(rgblist, axis = 0))

        for x in range(startx, endx):
          for y in range(starty, endy):
            im_resized[x][y] = np.median(rgblist, axis = 0)


        startx = endx
        endx = startx + pixelblockcount[0]

        if(startx >= im_resized.shape[0]):
          startx = 0
          endx = startx + pixelblockcount[0]
          starty = endy
          endy = endy + pixelblockcount[1]
          if(starty >= im_resized.shape[1]):
            break

        '''    
        print("x : ")
        print(startx,endx, np.median(rgblist, axis = 0))

        print("y : ")
        print(starty,endy)
        '''

  #print(time.time() - starttime)

  #print(im_resized.size)
  #print(im_resized)



  new_image = Image.fromarray(im_resized)
  outputfilename = "output" + imageid + ".png"
  new_image.save("static/output/" + outputfilename,"PNG")
  return(outputfilename)




