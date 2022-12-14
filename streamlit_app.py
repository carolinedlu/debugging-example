import streamlit as st
import tensorflow as tf
import tensorflow_hub as hub

@st.experimental_singleton
def get_model():
  model = hub.KerasLayer("https://tfhub.dev/google/universal-sentence-encoder-large/5", trainable=False)
  return model

if __name__ == "__main__":
  model = get_model()
  text = st.text_area("Enter some text")
  result = model(tf.convert_to_tensor(text))
