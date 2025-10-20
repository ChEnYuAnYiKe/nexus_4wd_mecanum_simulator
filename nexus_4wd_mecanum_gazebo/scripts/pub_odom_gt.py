#!/usr/bin/env python3
import rospy
from gazebo_msgs.msg import ModelStates
from nav_msgs.msg import Odometry

def main():
    rospy.init_node("gt_odom_mux")
    names = rospy.get_param("~model_names", ["ugv_0","ugv_1","ugv_2","ugv_3"])
    frame_id = rospy.get_param("~frame_id", "world")
    child_frame = rospy.get_param("~child_frame", "base_footprint")  # 你的车有 base_footprint

    pubs = {n: rospy.Publisher("/%s/odom_gt" % n, Odometry, queue_size=1) for n in names}

    def cb(ms: ModelStates):
        now = rospy.Time.now()
        idx = {n:i for i,n in enumerate(ms.name)}
        for n in names:
            i = idx.get(n)
            if i is None:
                continue
            od = Odometry()
            od.header.stamp = now
            od.header.frame_id = frame_id
            od.child_frame_id = "%s/%s" % (n, child_frame)  # 例：ugv_0/base_footprint
            od.pose.pose = ms.pose[i]
            od.twist.twist = ms.twist[i]
            pubs[n].publish(od)

    rospy.Subscriber("/gazebo/model_states", ModelStates, cb, queue_size=1)
    rospy.spin()

if __name__ == "__main__":
    main()
