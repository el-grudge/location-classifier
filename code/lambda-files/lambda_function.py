import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

preprocessor = create_preprocessor("xception", target_size=(150, 150))

model_name = 'ResNet_lr_0.10000000149011612_size_NA_dropout_0.5_01_0.953.tflite'
interpreter = tflite.Interpreter(model_path=model_name)
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]


# get classes
classes = [
    'cairo',
    'moscow',
    'paris'
]


def predict(url):
    X = preprocessor.from_url(url)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    float_preds = preds[0].tolist()
    class_pred_dict = dict(zip(classes, float_preds))

    return max(class_pred_dict, key=class_pred_dict.get)


def lambda_handler(event, context):
    url = event["url"]
    result = predict(url)
    return result
