
import keras
from keras.preprocessing import image
from keras.models import load_model
import streamlit as st
import numpy as np



def main():

	model = load_model('model_palm_life_line_2010.h5')

	st.write(""" # Read Your Future """ )

	st.write("This is a palm reading web app to predict your future")

	file = st.file_uploader("Please upload an image file", type=["jpg", "png"])
	image_size = (180,180) 
	
	img = keras.preprocessing.image.load_img( file, target_size=image_size )
	
	img_array = keras.preprocessing.image.img_to_array(img)
	
	img_array = np.expand_dims(img_array, 0)  # Create batch axis
	
	predictions = model.predict(img_array)
	
	max_indx = 0
	max_num = 0
	predictions = predictions.squeeze()
	
	for indx in  range(len(predictions)):
	  if indx == 0:
		max_num=predictions[indx]
		max_indx=indx
	  if indx>0:
		if predictions[indx]>predictions[indx-1]:
		  max_num=predictions[indx]
		  max_indx=indx
	#print(max_indx,". no:",max_num)
	if max_indx == 0:
	  st.write("A hand with three lines (life-brain-heart) joined")
	elif max_indx == 1:
	  st.write("A hand with two lines (life-brain) joined")
	else:
	  st.write("A hand with all lines (life-brain-heart) seperated")


	
if __name__ == '__main__':
	main()

