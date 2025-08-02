#Import required Libraries
from PIL import Image

# Open the images and resize them to equal size to ensure collage looks beautiful
image1 = Image.open("image1.png")
image1=image1.resize((500,500))
image2 = Image.open("image2.png")
image2=image2.resize((500,500))
image3 = Image.open("image3.png")
image3=image3.resize((500,500))
image4 = Image.open("image4.png")
image4=image4.resize((500,500))
image5 = Image.open("image5.png")
image5=image5.resize((500,500))

# Creation of Image which enables users to paste the images
collage= Image.new("RGBA",(1500,1500),color="black")
collage.paste(image1,(0,0))
collage.paste(image3,(1000,0))
collage.paste(image2,(500,500))
collage.paste(image4,(0,1000))
collage.paste(image5,(1000,1000))

# Save the newly genrated collage image
collage.save("Photo_Collage.png")