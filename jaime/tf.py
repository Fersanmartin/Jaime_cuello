#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
from std_msgs.msg import Float64MultiArray

def tf_listener():
    rospy.init_node('tf_listener_node')

    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    rate = rospy.Rate(1000)  # Escucha a una tasa de 1 Hz

    # Crea un publicador para las posiciones x y z
    position_publisher = rospy.Publisher('/position_topic', Float64MultiArray, queue_size=10)

    while not rospy.is_shutdown():
        try:
            # Intenta obtener la transformación entre dos frames
            transform = tf_buffer.lookup_transform('base_link', 'Tablet', rospy.Time())

            # Extrae las posiciones x y z
            x_position = transform.transform.translation.x
            z_position = transform.transform.translation.z

            # Crea un mensaje Float64MultiArray y establece las posiciones x y z
            position_msg = Float64MultiArray(data=[x_position, z_position])

            # Publica las posiciones en el tópico
            position_publisher.publish(position_msg)

        except tf2_ros.LookupException as e:
            rospy.logwarn("Excepción al buscar la transformación: {}".format(e))
        except tf2_ros.ExtrapolationException as e:
            rospy.logwarn("Excepción de extrapolación: {}".format(e))
        except tf2_ros.ConnectivityException as e:
            rospy.logwarn("Excepción de conectividad: {}".format(e))
        
        rate.sleep()

if __name__ == '__main__':
    try:
        tf_listener()
    except rospy.ROSInterruptException:
        pass
