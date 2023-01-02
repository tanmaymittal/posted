import io
import os
from google.cloud import vision



def returnLabel(img):
    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.abspath(f'./static/uploads/{img}')

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image, max_results=50)
    labels = response.label_annotations

    new_labels = []
    print('Labels:')
    for label in labels:
        if label.score >= 0.6:
            new_labels.append(label)

    # print(new_labels)
    final_labels = []
    for l in new_labels:
        final_labels.append(l.description)
        print(l.description)
    return final_labels

# from mvp import captionMaker

# print(captionMaker('The Blue Warf', 'Santa Cruz', final_labels))