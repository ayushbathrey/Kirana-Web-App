from PIL import Image 
import os 
directory = r'B:\OBJDectExp\webflask\test' 
for filename in os.listdir(directory): 
    if filename.endswith(".webp"): 
        prefix = filename.split(".webp")[0]
        im = Image.open(filename).convert("RGB")
        im.save(prefix+'.jpg',"jpeg")  
    else: 
        continue