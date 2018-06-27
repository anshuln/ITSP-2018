from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
import time

import numpy as np
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt
import get_contours
tic = time.time()
def load_graph(model_file):
    graph = tf.Graph()
    graph_def = tf.GraphDef()

    with open(model_file, "rb") as f:
        graph_def.ParseFromString(f.read())
    with graph.as_default():
        tf.import_graph_def(graph_def)
    return graph

def load_labels(label_file):
    label = []
    proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
    for l in proto_as_ascii_lines:
        label.append(l.rstrip())
    return label

def read_tensor_from_window(window, input_height=299, input_width=299,input_mean=0, input_std=255):
    float_caster = tf.cast(window, tf.float32)
    dims_expander = tf.expand_dims(float_caster, 0);
    resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
    normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
    sess = tf.Session()
    result = sess.run(normalized)
    return result

def create_windows(image):
    windows = []
    pos = []
    
    # image = cv2.imread(file_name)
    image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

    step=25  
    WINDOWX=100
    WINDOWY=100

    height = image.shape[0]
    width = image.shape[1]
    
    xmin=0
    xmax=WINDOWX            #These values may be hard-coded, or maybe ratios, but since final image will
    ymin=0                  #always be of same size, this does not matter
    ymax=WINDOWY

    while xmax<width:
        xmin+=step
        xmax+=step
        ymin=0
        ymax=WINDOWY
        while ymax<height:
            
            ymin=ymin+step
            ymax=ymax+step
            windows.append(image[xmin:xmax,ymin:ymax,0:3])
            pos.append([((xmax+xmin)/2.0),((ymax+ymin)/2.0)])
    print(len(windows))        
    return windows, pos

def main(path='Test1.jpg',name='digene'):    
    graph = load_graph(model_file)
    labels = load_labels(label_file)
    images,corners = get_contours.get_smaller_images(path)
    centroids=[]
    for i in range(0,len(images)):

        windows, pos = create_windows(images[i])
        xmin=corners[i][0]
        ymin=corners[i][1]
        app=[]
        #fig=plt.figure(figsize=(6,6))
        points=[]
        with tf.Session(graph=graph) as sess:
            for i in range(len(windows)):
                w = windows[i]
                
                input_name = "import/" + input_layer
                output_name = "import/" + output_layer
                input_operation = graph.get_operation_by_name(input_name);
                output_operation = graph.get_operation_by_name(output_name);
                tic=time.time()
                if(w.shape[0]):
                    t = read_tensor_from_window(w, input_height=input_height, input_width=input_width, input_mean=input_mean, input_std=input_std) 

                    results = sess.run(output_operation.outputs[0], {input_operation.outputs[0]: t})

                    results = np.squeeze(results)

                    top_k = results.argsort()[-5:][::-1]
                    k = top_k[0]                    
                    label=labels[k]
                    if(results[k]>0.85 and name==label):
                        points.append(pos[i])
                        print(pos[i][0],pos[i][1])
                        plt.imshow(w)
                        plt.title(label+' ('+str(results[k])+')')
                        plt.show()

            #print(labels[k], results[k], pos[i])
        if len(points):
            app.append(xmin+sum([x[0] for x in points] )/len(points))
            app.append(ymin+sum([x[1] for x in points] )/len(points))
            centroids.append(app)            
                
        
        #plt.show()
    return(centroids)

if __name__ == "__main__":
    #file_name = "tf_files/Test1.jpg"
    model_file = "G:/ITSP Codes/tensorflow-for-poets-2-master/tf_files/retrained_graph.pb"
    label_file = "G:/ITSP Codes/tensorflow-for-poets-2-master/tf_files/retrained_labels.txt"
    input_height = 224
    input_width = 224
    input_mean = 128
    input_std = 128
    input_layer = "input"
    output_layer = "final_result"
    c=main()
    print(c)


