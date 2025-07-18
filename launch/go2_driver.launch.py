# Copyright (c) 2024 Intelligent Robotics Lab (URJC)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch_ros.actions import ComposableNodeContainer, Node
from launch_ros.descriptions import ComposableNode


def generate_launch_description():

    composable_nodes = []

    composable_node = ComposableNode(
        package='go2_driver',
        plugin='go2_driver::Go2Driver',
        name='go2_driver',
        namespace='',

    )
    composable_nodes.append(composable_node)

    container = ComposableNodeContainer(
        name='go2_container',
        namespace='',
        package='rclcpp_components',
        executable='component_container',
        composable_node_descriptions=composable_nodes,
        output='screen',
    )

    ld = LaunchDescription()
    ld.add_action(container)

    return ld
