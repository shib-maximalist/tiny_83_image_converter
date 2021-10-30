## What is this?
This tool allows you to convert any 14p high and 22p wide Bitmap (.bmp) to the seed needed for the 
[Tiny-83 NFT project](https://opensea.io/collection/tiny-83 "Tiny-83 NFT project").

Project Twitter: https://twitter.com/TINY83_nft

Project Open Sea: https://opensea.io/collection/tiny-83

Minting Page: https://tiny-83.github.io/tiny-83/


My Twitter: https://twitter.com/shib_maximalist

My Open Sea: https://opensea.io/shib_maximalist

## Usage
### Windows
```
git clone https://github.com/shib-maximalist/tiny_83_image_converter
cd tiny_83_image_converter
py -m pip install -r requirements.txt
py main.py
```

### Linux
```
git clone https://github.com/shib-maximalist/tiny_83_image_converter
cd tiny_83_image_converter
pip install -r requirements.txt
python main.py
```

## How does it work?
When I played arround with the [minting page](https://tiny-83.github.io/tiny-83/ "minting page")  
I noticed that the two seed value had a very distinctive influence on the outcome on the screen:
<p align="center">
    <img src="documentation/1.png"><br>
    (1,1)
</p>
<p align="center">
    <img src="documentation/2.png"><br>
    (2,2)
</p>
<p align="center">
    <img src="documentation/3.png"><br>
    (3,3)
</p>
3

Notice something? Thats binary! Both panes (left an right) are composed of 11x14 pixels. Thats 154 pixels in total per pane and 308 for the whole image.
What we need is a way to address the pixels individually.

