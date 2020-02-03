import face_recognition
from PIL import Image, ImageDraw

image = face_recognition.load_image_file ("/Desktop/ProjectCv2/faceRecognation/dataImage/a.jpg") #change with your own directory
face_locations = face_recognition.face_locations(image)
face_encodings = face_recognition.face_encodings(image, face_locations)


pil_image = Image.fromarray(image)

draw = ImageDraw.Draw(pil_image)

for (top, right, bottom ,left ), face_locations in zip (face_locations, face_encodings):
    draw.rectangle(((left, top),(right, bottom)), outline=(127,255,0))





del draw
pil_image.show()
