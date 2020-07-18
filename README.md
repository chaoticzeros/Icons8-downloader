# Icons8-downloader

Script to download PNG and ICO from Icons8 website (Max resolution 550px)

1. Make sure you have the following python packages installed

   * requests
   * imageio (To convert PNG files to ICO files)

2. Go to https://icons8.com/icons and select the pack you want to download

3. Find the name of the pack from the pack URL. Ex: For fluent icons (https://icons8.com/icons/fluent) the name of the pack would be "**fluent**". Paste this in the PACK field in the code

4. Navigate to any icon category in the pack you want to download (https://icons8.com/icon/pack/logos/fluent) and right click on one of the icons. Click Inspect to use the inspector of the browser.  You will find something like this.

   ```html
   <img alt="Adobe After Effects icon" src="https://img.icons8.com/fluent/96/adobe-after-effects.png" style="height: 48px; width: 48px;">
   ```

   copy the image size (96 in this example) from the "src=https://img..." field and paste it in the DEFAULT_SIZE field in the code. Note that the image size could be a number like "**96**" or a multiple like "**2x**". This step is essential to download icons in 550px resolution. (Otherwise you will get small images). If you want graphical instructions, follow steps 1 and 2 from [this](https://medium.com/@PBalquet/how-to-download-vector-icons-in-icons8-free-e8502828cb08) guide 

5. Run the script!




### Important Notes

* The following two fields need to be replaced appropriately to download a specific icon pack

  ```python
  PACK = "fluent"
  DEFAULT_SIZE = "96"
  ```

* This method only downloads **550x550** pixel images which are present as previews in the website (which is probably not illegal, but note that icons8 requires that you give credit when you use their stuff)

* If you only want the PNG files, comment out the code below the line

  ```python
  # Convert to ICO
  ```

  

