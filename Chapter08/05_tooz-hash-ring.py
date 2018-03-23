# -*- encoding: utf-8 -*-
from tooz import hashring


NUMBER_OF_NODES = 16

# Step #1 16개의 노드로 해시 링 생성
hr = hashring.HashRing(["node%d" % i for i in range(NUMBER_OF_NODES)])
nodes = hr.get_nodes(b"some data")
print(nodes)
nodes = hr.get_nodes(b"some data", replicas=2)
print(nodes)
nodes = hr.get_nodes(b"some other data", replicas=3)
print(nodes)
nodes = hr.get_nodes(b"some other of my data", replicas=2)
print(nodes)

# Step #2 노드 하나를 제거
print("Removing node8")
hr.remove_node("node8")
nodes = hr.get_nodes(b"some data")
print(nodes)
nodes = hr.get_nodes(b"some data", replicas=2)
print(nodes)
nodes = hr.get_nodes(b"some other data", replicas=3)
print(nodes)
nodes = hr.get_nodes(b"some other of my data", replicas=2)
print(nodes)

# Step #3 새 노드 추가
print("Adding node17")
hr.add_node("node17")
nodes = hr.get_nodes(b"some data")
print(nodes)
nodes = hr.get_nodes(b"some data", replicas=2)
print(nodes)
nodes = hr.get_nodes(b"some other data", replicas=3)
print(nodes)
nodes = hr.get_nodes(b"some other of my data", replicas=2)
print(nodes)
nodes = hr.get_nodes(b"some data that should end on node17", replicas=2)
print(nodes)

# Step #4 제거한 노드를, 더 높은 가중치로 다시 추가한다.
print("Adding back node8 with weight")
hr.add_node("node8", weight=100)
nodes = hr.get_nodes(b"some data")
print(nodes)
nodes = hr.get_nodes(b"some data", replicas=2)
print(nodes)
nodes = hr.get_nodes(b"some other data", replicas=3)
print(nodes)
nodes = hr.get_nodes(b"some other of my data", replicas=2)
print(nodes)