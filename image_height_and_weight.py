import cv2 as cv 
   
# reading the heith and width of each place on an image with mouse click
def read_height_width():
        def onClick(event, x, y,flags, param):
           if event == cv.EVENT_LBUTTONDOWN:
                print(x, ' , ', y)
                font = cv.FONT_HERSHEY_SIMPLEX
                strXY = str(x) + ',' + str(y)
                cv.putText(img, strXY, (x,y), font, 1, (0,255,225), 4)
                cv.imshow('image', img)
           if event == cv.EVENT_RBUTTONDOWN:
              blue= (y,x,0)
              green = (y,x,1)
              red = (y, x,2)
              font = cv.FONT_HERSHEY_SIMPLEX
              bgr = str(blue) + ',' + str(green) + ',' + str(red)
              cv.putText(img, bgr, (x, y), font, 1, (0, 0, 225), 4)
              cv.imshow('image', img)


        #img = np.zeros((245, 544, 3), np.uint8)
        img = cv.imread('11.jpg')
        img = cv.resize(img, (1000, 400))
        cv.imshow('image', img)
        cv.setMouseCallback('image', onClick)

        cv.waitKey(0)

        cv.destroyAllWindows()

read_height_width()
