from mazelib import Maze
from mazelib.generate.AldousBroder import AldousBroder
from mazelib.generate.BacktrackingGenerator import BacktrackingGenerator
from mazelib.generate.BinaryTree import BinaryTree
from mazelib.generate.CellularAutomaton import CellularAutomaton
from mazelib.generate.Division import Division
from mazelib.generate.DungeonRooms import DungeonRooms
from mazelib.generate.Ellers import Ellers
from mazelib.generate.GrowingTree import GrowingTree
from mazelib.generate.HuntAndKill import HuntAndKill
from mazelib.generate.Kruskal import Kruskal
from mazelib.generate.Prims import Prims
from mazelib.generate.Sidewinder import Sidewinder
from mazelib.generate.TrivialMaze import TrivialMaze
from mazelib.generate.Wilsons import Wilsons


class MazeGenerator:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def generate_map(self, algo=0):
        algos = {0: self.generate_using_aldous_broder(),
                 1: self.generate_using_wilson(),
                 2: self.generate_using_prim(),
                 3: self.generate_using_eller(),
                 4: self.generate_using_kruskal(),
                 5: self.generate_using_trivial(),
                 6: self.generate_using_sidewinder(),
                 7: self.generate_using_cellular_automation(),
                 8: self.generate_using_backtracking(),
                 9: self.generate_using_binary_tree(),
                 10: self.generate_using_dungeon_rooms(),
                 11: self.generate_using_growing_tree(),
                 12: self.generate_using_recursive_division(),
                 13: self.generate_using_hunt_n_kill()}

        temp = str(algos[algo])
        temp = temp.replace(" ", "-")
        iter1 = [x for x in temp.splitlines()]
        map = []
        for line in iter1:
            map.append(list(line))

        return map

    def generate_using_aldous_broder(self):
        m = Maze()
        m.generator = AldousBroder(self.height, self.width)
        m.generate()
        return m

    def generate_using_backtracking(self):
        m = Maze()
        m.generator = BacktrackingGenerator(self.height, self.width)
        m.generate()
        return m

    def generate_using_cellular_automation(self):
        m = Maze()
        m.generator = CellularAutomaton(self.height, self.width)
        m.generate()
        return m

    def generate_using_dungeon_rooms(self):
        m = Maze()
        m.generator = DungeonRooms(self.height, self.width)
        m.generate()
        return m

    def generate_using_eller(self):
        m = Maze()
        m.generator = Ellers(self.height, self.width)
        m.generate()
        return m

    def generate_using_growing_tree(self):
        m = Maze()
        m.generator = GrowingTree(self.height, self.width)
        m.generate()
        return m

    def generate_using_hunt_n_kill(self):
        m = Maze()
        m.generator = HuntAndKill(self.height, self.width)
        m.generate()
        return m

    def generate_using_kruskal(self):
        m = Maze()
        m.generator = Kruskal(self.height, self.width)
        m.generate()
        return m

    def generate_using_prim(self):
        m = Maze()
        m.generator = Prims(self.height, self.width)
        m.generate()
        return m

    def generate_using_recursive_division(self):
        m = Maze()
        m.generator = Division(self.height, self.width)
        m.generate()
        return m

    def generate_using_sidewinder(self):
        m = Maze()
        m.generator = Sidewinder(self.height, self.width)
        m.generate()
        return m

    def generate_using_wilson(self):
        m = Maze()
        m.generator = Wilsons(self.height, self.width)
        m.generate()
        return m

    def generate_using_binary_tree(self):
        m = Maze()
        m.generator = BinaryTree(self.height, self.width)
        m.generate()
        return m

    def generate_using_trivial(self):
        m = Maze()
        m.generator = TrivialMaze(self.height, self.width)
        m.generate()
        return m
