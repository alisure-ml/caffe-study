import sys
import caffe

model_file = "../net/lenet.prototxt"
pre_trained = "../model/mnist_iter_60000.caffemodel"
image_file = "../data/mnist/image/image_0.bmp"

input_image = caffe.io.load_image(image_file, color=False)
net = caffe.Classifier(model_file, pre_trained)

prediction = net.predict([input_image], oversample=False)
caffe.set_mode_gpu()

print(prediction[0].argmax())
