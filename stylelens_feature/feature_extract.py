# coding: utf-8
"""
    stylelens-feature

    This is a API document for Object Detection on fashion items\"

    OpenAPI spec version: 0.0.1
    Contact: devops@bluehack.net
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import numpy as np
import os
import tensorflow as tf

class ExtractFeature(object):
  def __init__(self):
    try:
      MODEL = os.environ['CLASSIFY_GRAPH']
    except:
      print("!!! Need to define environment variable: CLASSIFY_GRAPH=/path/to/model.pb")


    print(MODEL)
    with tf.gfile.FastGFile(MODEL, 'rb') as f:
      graph_def = tf.GraphDef()
      graph_def.ParseFromString(f.read())
      _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as self.sess:
      self.pool3 = self.sess.graph.get_tensor_by_name('pool_3:0')

  def extract_feature(self, file):
    with tf.gfile.GFile(file, 'rb') as fid:
      image_data = fid.read()
      pool3_features = self.sess.run(self.pool3,{'DecodeJpeg/contents:0': image_data})
      feature = np.squeeze(pool3_features)
      print(feature)
      return feature


