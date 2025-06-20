import PIL.Image
from PIL import ImageEnhance,ImageOps

class ASCIIArt:
    def __init__(self,path,width,contrast,negativ):
        #● ─ ┐ ─ └ ┘
        self.new_width = width
        ASCIIChar1 = [ "@", "#", "S", "%", "?", "*", "+", ";", ":", ",", " "]
        #ASCIIChar2 = [ "@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
        #ASCIIChar3 = ["●", "#", "S", "%", "?", "*", "+", ";", ":", ",", " "]
        #ASCIIChar4 = ["●", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]
        #ASCIIChar4 = ["@", "@", "@", "@", "@", "@", "@",  ":", ":", ".", " "]

  
self.ASCIIChar = ASCIIChar1


        try:
            image = PIL.Image.open(path)
            if(contrast):
                enhancer = ImageEnhance.Contrast(image)
                factor = float(input("contrast enhancing factor: "))
                image = enhancer.enhance(factor)
            if(negativ):
                image = ImageOps.invert(image)

        except:
            path = input("try to input path again: ")
            self.__init__(path)
        self.ConImToASC(image)
    def ConImToASC(self,image):
        new_image = self.PixleToASCII(self.GrayShade(self.Resize(image,self.new_width)))
        pixlecount = len(new_image)
        ascii_image = "\n".join(new_image[i:(i+self.new_width)] for i in range(0,pixlecount,self.new_width))
        print(ascii_image)
    def Resize(self,image,new_width):
        width,hight = image.size
        a = hight/width
        new_hight = int(a*new_width)
        resized_image = image.resize((new_width,new_hight))
        return(resized_image)

    def GrayShade(self,image):
        image = image.convert("L")
        return(image)

    def PixleToASCII(self,image):
        pixels = image.getdata()
        characters = "".join([self.ASCIIChar[pixel//25] for pixel in pixels])
        return(characters)
Pictures = ["picture Paths"]
width = 25
Art = ASCIIArt(Pictures[5],width,False,False)