FROM tensorflow/serving:2.7.0

COPY ./location-classifier /models/location-classifier/1 
ENV MODEL_NAME="location-classifier"