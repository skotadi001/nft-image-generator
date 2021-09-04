

## About
This is a fork from https://github.com/benyaminahmed/nft-image-generator
Instead of using a Python Notebook, this is strait Python.  I left the Notebook file for comparison, but the main script here is generator.py

I added detailed notes on what needs to be changed in each section of the code, to fit your graphics, layers and traits.
## Getting Started
1. Install [Python](https://www.python.org/downloads/)

2. Install PIP
Download PIP get-pip.py
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python get-pip.py
```

3. Install Python Pillow
```
pip install pillow
```

4. Run the code
```
python generator.py
```

# Results
If the program executes successfully, it will output all the generated images to the /images folder, and the metadata to the /metadata folder. The filenames will refer to tokenIds. 

## Common Errors
VaueError: Images do not match

Fix: your images all need to be of the same size.  If the background is 1000x1000 and a trait layer is 500x500 this error will be thrown.
