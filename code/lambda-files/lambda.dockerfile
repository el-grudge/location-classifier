FROM public.ecr.aws/lambda/python:3.10

RUN pip install keras-image-helper
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.14.0-cp310-cp310-linux_x86_64.whl

COPY ResNet_lr_0.10000000149011612_size_NA_dropout_0.5_01_0.953.tflite .
COPY lambda_function.py .

CMD ["lambda_function.lambda_handler"]