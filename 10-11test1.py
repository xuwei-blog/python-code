                      #       迪克斯特拉算法
# (e表格)(坐标权重关系图的实现)
graph = {}                 
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2


#print(graph)                #{'start': {'a': 6, 'b': 2}}
#print(graph["start"])       #{'a': 6, 'b': 2}
#print(graph["start"]["a"])  #6



graph["a"] = {}
graph["a"]["fin"] = 1


graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}           #终点没有邻居

#汇总的坐标信息
#print(graph)



#开销表(算法图解中的名称)    aka(我理解的叫法)(dis表,估计值表)(用来记录最短路径)
#定义无穷大
infinity = float("inf")

#创建开销表  记录最小权重之和
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity


#储存父节点的散列表

parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None


#避免重复处理
processed = []

#定义函数(查找costs中最小的值)
def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost< lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node



#代码的实现
node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbours = graph[node]
    
    for n in neighbours.keys():
        new_cost = cost + neighbours[n]
        if costs[n] > new_cost:
            costs[n]  = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)


#最短路径        
print(costs)
print(parents)




