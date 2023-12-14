#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import numpy as np
from std_msgs.msg import Float64MultiArray
import time
import pickle
import pandas as pd
pos=0
joint=0
matriz=np.zeros((60,140), dtype=object)
def guardar_valor(joints,posis):
    global matriz
    x,y=[posis[0]*100,posis[1]*100]
    if (x%1.0<0.4) and (y%1.0<0.4):
        if type(matriz[int(x),int(y)])==int:
          matriz[int(x),int(y)]=[int(x),int(y),joints[0],joints[2],joints[4]]
          print(matriz[int(x),int(y)])

          with open('matriz_IK.pkl', 'wb') as archivo:
              pickle.dump(matriz, archivo)
          # Ruta del archivo CSV donde se guardará el DataFrame
          ruta_archivo_csv = 'matriz_guardada.csv'

          df = pd.DataFrame(matriz)

          # Guardar el DataFrame en el archivo CSV sin incluir índices y encabezados
          df.to_csv(ruta_archivo_csv, index=False, header=False)      
def callback(data):
    global pos
    pos=data.data
    guardar_valor(joint,pos)

def joint_states_callback(msg):
    # Accede a las posiciones de las articulaciones desde el mensaje
    global joint
    joint = msg.position
    #print("Joint Positions:", joint)

def listener():
    rospy.init_node('joint_states_listener', anonymous=True)
    rate = rospy.Rate(10)  # Publicar a una tasa de 1 Hz
    rospy.Subscriber("joint_states", JointState, joint_states_callback)
    rospy.Subscriber('/position_topic', Float64MultiArray, callback)
    rate.sleep()
    
    rospy.spin()



    

    

    
    
  
    
       
    
    
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass

