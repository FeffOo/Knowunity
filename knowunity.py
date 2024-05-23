
import requests
import shutil
import time
import os
import subprocess
from PIL import Image


def convert_webp_to_jpg(input_file, output_file):
    try:
        # Open the WebP image
        with Image.open(input_file) as img:
            # Convert to RGB mode if the image is in CMYK mode
            if img.mode == 'CMYK':
                img = img.convert('RGB')
            
            # Save as JPG
            img.save(output_file, 'JPEG')
            
        print('Conversion successful!')
        
    except IOError:
        print(f'Unable to open {input_file}')
        


pageCounter = 1
url = input('URL: ')
response = requests.get(url + str(pageCounter) + '.webp', stream=True)
while response.status_code == 200:
	with open('Knowunity/img' + str(pageCounter) + '.webp', 'wb') as out_file:
			shutil.copyfileobj(response.raw, out_file)
			time.sleep(0.3)
			out_file.close()
                  
			webp_img = 'Knowunity/img' + str(pageCounter) + '.webp'
			jpg_out_file = 'Knowunity/img' + str(pageCounter) + '.jpg'
			convert_webp_to_jpg(webp_img, jpg_out_file)

			time.sleep(0.2)
			
			with open(jpg_out_file, 'r') as file:
				lpr =  subprocess.Popen(["lpr", "-o", "page-ranges=1-2"], stdin=file)
				output = lpr.communicate()[0]
				file.close()

			os.remove(webp_img)
			os.remove(jpg_out_file)
			pageCounter += 1
			response = requests.get(url + str(pageCounter) + '.webp', stream = True)
