import unittest
from graph_adjacency_list import *

class TestKahnTopologicalSort(unittest.TestCase):
    def setUp(self):
        # 创建一个新的图实例
        self.graph = Graph(6)
    
    def test_dag(self):
        # 创建一个有向无环图 (DAG)
        # 构建如下图
        #     5 → 2 → 3
        #     ↓      ↓
        #     4 → 1 → 0

        self.graph.add_edge(5, 2)
        self.graph.add_edge(5, 4)
        self.graph.add_edge(4, 1)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(3, 1)
        self.graph.add_edge(1, 0)

        # 执行拓扑排序
        topo_order = self.graph.kahn_topological_sort_dfs()

        # 拓扑排序的结果应该满足依赖关系
        # 将拓扑排序结果的索引存入字典，方便检查顺序关系
        topo_index = {node.id: idx for idx, node in enumerate(topo_order)}
        
        # 检查每个依赖关系是否满足拓扑排序
        # 5 -> 2, 5 -> 4, 4 -> 1, 2 -> 3, 3 -> 1, 1 -> 0
        self.assertLess(topo_index[5], topo_index[2])
        self.assertLess(topo_index[5], topo_index[4])
        self.assertLess(topo_index[4], topo_index[1])
        self.assertLess(topo_index[2], topo_index[3])
        self.assertLess(topo_index[3], topo_index[1])
        self.assertLess(topo_index[1], topo_index[0])

    def test_cycle_detection(self):
        # 创建一个有环的图
        # 构建如下图
        #     1 → 2
        #     ↑   ↓
        #     ← 3 ←

        self.graph.add_edge(1, 2)
        self.graph.add_edge(2, 3)
        self.graph.add_edge(3, 1)

        # 执行拓扑排序时应检测到环
        with self.assertRaises(ValueError):
            self.graph.kahn_topological_sort_dfs()

if __name__ == '__main__':
    unittest.main()