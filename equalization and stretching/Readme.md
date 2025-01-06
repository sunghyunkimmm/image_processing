Today is my first uploading in GitHub. I'm so excited to start my activity. You'll see my progress!

I learned about Equalization and Histogram Stretching. I think we need to know why they use these methods.

Before we know about them we need to know about "image contrast". It's simply says that the difference between bright region and dark region.

![image](https://github.com/user-attachments/assets/fb7899bb-5884-4a63-8687-9643e20b3323)



If we look at these 4 images. All left box have the same intensity but it seems a little difference because of the right box. The same color can appear differntly depending on the brightness of adjacent colors, which can cause confusion in images where contrast is low.

If an image contains mostly similar pixel values, it becomes difficult to identify important features or details. Among the ways to improve image quality, we will try to improve image contrast.

Implementation: If we compare original image and processed image, we should compare histogram!

**Histogram Stretching**

This method is often referred to as the histogram normalization technique. It is a method of normalizing as much as the image pixel bit.

The calculation formula is as follows.

![image](https://github.com/user-attachments/assets/ec41ede8-af80-4b3b-a115-2dff4c2fa9e0)


Let's compare original image and processed image.

![image](https://github.com/user-attachments/assets/09390841-1c48-4ee1-9377-f5d26bbe460f)


As the method was named, the histogram of the image has stretched. I don't think it's working well.

**Equalization**

This method converts the histogram to make the pixel value distribution more uniform.

Procedure

1. Calcualte the histogram of the image to obtain the frequency of each pixel intensity value
2. Compute the cumulative frequency from the histogram values.
3. Normalize the cumulative frequencies.
4. Convert pixel values

More detailed explanations will be understood by searching or by looking at my code.

![image](https://github.com/user-attachments/assets/3c6ff0a6-1429-417b-9d17-72836cbb87dc)


This is the result! It seems that the goal of improving image contrast has been reached.

These results clearly show the difference between the two methods.

<Original image>

![image](https://github.com/user-attachments/assets/fb5e93f0-23fa-4c16-b358-580ad219c606)


<Stretched_image>

![image](https://github.com/user-attachments/assets/42d81ecd-038c-42ad-a482-03e9923a33c4)


<Equalized_image>

![image](https://github.com/user-attachments/assets/ee84899c-bbc0-4202-8953-faa2703f7875)


We can make decision that the quality of this Equalized_image has been further improved. But it doesn't look natural. After considering why this happens, I observed the histogram of the equalized image and noticed that the values in the histogram are spaced apart after the process. I believe this occurs because the values are not continuous, which makes the image appear unnatural to our eyes.
