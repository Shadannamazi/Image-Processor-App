# CMPT 120 Yet Another Image Processer
# Starter code for cmpt120imageManip.py
# Author(s): Faiza Tabassum(301470578), Shadan Namazifard(301475038)
# Group: ProjectYAIPGroup- 112
# Date: Dec. 6 2021
# Description: 
"""
Every function for the manipulations is defined here 
later used in main.py where they are executed. 
"""

import cmpt120imageProjHelper as ch
import numpy
import copy 

def ApplyRedFilter(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: Retains the R values of all pixels in the image, 
  and sets G and B to zero and returns an image that has a red filter
  """
  height = len(pixels)
  width = len(pixels[0])
  new_img = ch.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      r = pixels[row][col][0]
      new_img[row][col] = [r,0,0]
   
  return new_img  

def ApplyGreenFilter(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Retains the G values of all pixels in the image, 
  and sets R and B to zero and returns an image that has a green filter
  """
  height = len(pixels)
  width = len(pixels[0])
  new_img = ch.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      g = pixels[row][col][1]
      new_img[row][col] = [0,g,0]
   
  return new_img

def ApplyBlueFilter(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: Retains the B values of all pixels in the image,
  and sets R and G to zero and returns an image that has a blue filter
  """
  height = len(pixels)
  width = len(pixels[0])
  new_img = ch.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      b = pixels[row][col][2]
      new_img[row][col] = [0,0,b]
   
  return new_img

def SepiaFilter(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: applies the formula for R,G,B and changes the color accordingly
  and returns an image with all the colors with warm brownish tone
  """
  height = len(pixels)
  width = len(pixels[0])
  new_img = ch.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      r = pixels[row][col][0]
      g = pixels[row][col][1]
      b = pixels[row][col][2]
      sepiaRed = int((r * .393) + (g *.769) + (b * .189))
      sepiaGreen = int((r * .349) + (g *.686) + (b * .168))
      sepiaBlue = int((r * .272) + (g *.534) + (b * .131))
      new_img[row][col] = [min(255,sepiaRed),min(255,sepiaGreen),min(255,sepiaBlue)]
  
  return new_img 

def scale_down(value):
  """
  Input:  value - integer or float 
  Output: returns result- from the value scaled down 
  """
  if value<64:
    result = int(value/64 * 50)
  elif 64<=value<128:
    result = int((value-64)/(128-64) * (100-50) + 50)
  else:
    result = int((value-128)/(255-128) * (255-100) + 100)
  
  return result  

def scale_up(value):
  """
  Input:  value - integer or float 
  Output: returns result- from the value scaled up 
  """
  if value<64:
    result = int(value/64 * 80)
  elif 64<=value<128:
    result = int((value-64)/(128-64) * (160-80) + 80)  
  else:
    result = int((value-128)/(255-128) * (255-160) + 160) 
  
  return result  

def ApplyWarmFilter(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: uses the functions scale_up to get scaled up value of red 
  and scale_down to get scaled down value of blue 
  and returns an image with all the colors with a warm tone
  """
  height = len(pixels)
  width = len(pixels[0])
  new_img = ch.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      r = pixels[row][col][0]
      g = pixels[row][col][1]
      b = pixels[row][col][2]
      
      new_img[row][col] = [scale_up(r),g,scale_down(b)]
   
  return new_img  
   
def ApplyColdFilter(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: uses the functions scale_up to get scaled up value of blue
  and scale_down to get scaled down value of red 
  and returns an image with all the colors with a cold tone
  """
  height = len(pixels)
  width = len(pixels[0])
  new_img = ch.getBlackImage(width, height)
  for row in range(height):
    for col in range(width):
      r = pixels[row][col][0]
      g = pixels[row][col][1]
      b = pixels[row][col][2]
      new_img[row][col] = [scale_down(r),g,scale_up(b)]
   
  return new_img

def RotateLeft(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: returns the img rotated counter-clockwise by 90 degrees 
  by creating a new image with width equal to the original’s height 
  and height equal to the original’s width
  """
  height = len(pixels)
  width = len(pixels[0])
  new_img = ch.getBlackImage(height, width)
  for col in range(width):
    for row in range(height):
      new_img[col][row] = pixels[row][width-1-col]
 
  return new_img

def RotateRight(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: returns the img rotated clockwise by 90 degrees 
  by creating a new image with width equal to the original’s height 
  and height equal to the original’s width
  """
  height = len(pixels)
  width = len(pixels[0])
  new_img = ch.getBlackImage(height, width)
  for col in range(width):
    for row in range(height):
      new_img[col][row] = pixels[height-1-row][col]

  return new_img

def DoubleSize(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: returns an img with both width and height doubled
  """
  height = len(pixels)
  width = len(pixels[0])
  new_img = ch.getBlackImage(2*width, 2*height)
  for row in range(height):
    for col in range(width):
          new_img[(2*row)+1][(2*col)+1] = pixels[row][col]
          new_img[2*row][2*col] = pixels[row][col]
          new_img[2*row][(2*col)+1] = pixels[row][col]
          new_img[(2*row)+1][2*col] = pixels[row][col]
  
  return new_img 

def HalfSize(pixels):
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: returns an img with both width and height halved
  """
  height = len(pixels)
  width = len(pixels[0])
  new_img = ch.getBlackImage((width+1)//2, (height+1)//2)
  for row in range(height):
    for col in range(width):
          new_img[row//2][col//2] = pixels[row//2][col//2]
          new_img[row//2][col//2] = pixels[row][col//2]
          new_img[row//2][col//2] = pixels[row//2][col]
          new_img[row//2][col//2] = pixels[row][col]

  return new_img

def LocateFish(pixels): 
  """
  Input:  pixels - 3d list of lists of RGB values
  Output: returns a deepcopy img of the fish 
  with a drawn green bounding box around the fish
  """
  fish_copy = copy.deepcopy(pixels)
  height_f = len(pixels)
  width_f = len(pixels[0]) 
  #a list containing all the row and columns which contain the yellow pixels of the fish
  row_list = []
  col_list = []
  for row in range(height_f):
    for col in range(width_f):
      r = pixels[row][col][0]
      g = pixels[row][col][1]
      b = pixels[row][col][2]
      h = ch.rgb_to_hsv(r,g,b)[0]
      s = ch.rgb_to_hsv(r,g,b)[1]
      v = ch.rgb_to_hsv(r,g,b)[2]
      
      if 40<h<100 and 30<s<101 and 85<v<101:
        row_list.append(row)
        col_list.append(col)
  
  for row in range(height_f):
    for col in range(width_f):
      r = pixels[row][col][0]
      g = pixels[row][col][1]
      b = pixels[row][col][2]
      h = ch.rgb_to_hsv(r,g,b)[0]
      s = ch.rgb_to_hsv(r,g,b)[1]
      v = ch.rgb_to_hsv(r,g,b)[2]
      #find the first and last col and row where the yellow pixels appear 
      if 40<h<100 and 30<s<101 and 85<v<101:
        #set all the rows in the min col from the col_list to green 
        fish_copy[row][min(col_list)] = [0,255,0]
        #set all the col in the min row from the row_list to green 
        fish_copy[min(row_list)][col] = [0,255,0]
        #set all the rows in the max col from the col_list to green
        fish_copy[row][max(col_list)] = [0,255,0]
        #set all the col in the max row from the row_list to green
        fish_copy[max(row_list)][col] = [0,255,0]
      
  return fish_copy
    