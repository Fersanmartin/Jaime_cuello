#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import numpy as np
from std_msgs.msg import Float64MultiArray
import time
import pickle

pos=0
def callback(data):
    global pos
    pos=data.data
    
def publish_joint_states():

    primero=0.7
    segundo=0.7
    tercero=1.5

    rospy.init_node('joint_state_publisher', anonymous=True)
    rate = rospy.Rate(1000000)  # Publicar a una tasa de 1 Hz

    joint_states_pub = rospy.Publisher('/joint_states', JointState, queue_size=10)

    joint_state_msg = JointState()
    joint_state_msg.header = Header()

    # Ejemplo: Publicar valores constantes de las 5 articulaciones
    joint_state_msg.name = ['primero', 'segundo', 'tercero', 'cuarto', 'quinto']
    # joint_state_msg.position = [np.random.uniform(0.5, 0.5) for _ in range(5)]
    joint_state_msg.position = [0,0,0,0,0,0]

    
    list_positions = []

    n=20
    for i in range(n+1):
        angulo_1 =(float(i)/n)*primero
        for j in range(n+1):
            angulo_2 =(float(j)/n)*segundo
            for k in range(n+1):
                angulo_3 =(float(k)/n)*tercero
                list_positions.append([angulo_1,angulo_1,angulo_2,angulo_2,angulo_3])
    # Obtén el tiempo actual
    tiempo_inicial = time.time()

    # Duración deseada en segundos
    duracion = 0.1
    # while not rospy.is_shutdown():
    matriz=[]
    for position in list_positions:
        rospy.Subscriber('/position_topic', Float64MultiArray, callback)
        while (time.time() - tiempo_inicial) < duracion:
            
            joint_state_msg.header.stamp = rospy.Time.now()
            joint_state_msg.position = position
            rate.sleep()
            joint_states_pub.publish(joint_state_msg)
        
        #matriz.append(pos.extend(position))
        xy=[pos[0],pos[1]]
        position=[position[0],position[2],position[4]]
        xy.extend(position)
        matriz.append(xy)
        tiempo_inicial = time.time()
    
    with open('matriz_IK.pkl', 'wb') as archivo:
        pickle.dump(matriz, archivo)

if __name__ == '__main__':
    try:
        publish_joint_states()
    except rospy.ROSInterruptException:
        pass




