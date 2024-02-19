from PIL import Image

images = [Image.open("E:/Python/Learning-Python/manga_downloader/saved_pics/"+f)
          for f in ["school logo.png", "Akagami.png"]]

print(images)

pdf_path = "E:/Python/Learning-Python/manga_downloader/logo.pdf"
images[0].save(pdf_path, "PDF" , resolution=100.0, save_all=True, append_images=images[1:])
print(images)