import numpy
import numpy as np
import random
from random import choice


class Game2048(object):

    def __init__(self,dimension = 4):
        self.dimension = dimension  #维数，决定要构建几维的矩阵 
        self.matrix = np.zeros((dimension,dimension)) #创建一个全是0的n(n = dimension)维矩阵

    def judge_gameover(self):#判断是否游戏结束，如果游戏结束返回True，未结束则返回False
        '''如果水平方向上任意两个相邻的数字有相等的或者有为0的那么游戏未结束'''
        for a in range(0,self.dimension):
            for b in range(0,self.dimension-1):
                if self.matrix[a][b] == self.matrix[a][b+1] or self.matrix[a][b] == 0 or self.matrix[a][b+1] == 0:
                    return False
        '''如果垂直方向上任意两个相邻的数字有相等的或者有为0的那么游戏未结束'''
        self.matrix = np.transpose(self.matrix)#先转置垂直方向变作水平方向 eg:[[1,2],[3,4]]>>[[1,3],[2,4]]
        for a in range(0,self.dimension):
            for b in range(0,self.dimension-1):
                if self.matrix[a][b] == self.matrix[a][b+1] or self.matrix[a][b] == 0 or self.matrix[a][b+1] == 0:
                    return False
        return True
                    
    def generate_num(self):#在随机的空白(为0)的位置替换为1个随机的2或者4
        '''在随机的空白(为0)的位置替换为1个随机的2或者4'''
        
        #判断矩阵内为零的数的位置,并将索引放入到list_0中
        list_0 = []
        for a in range(0,self.dimension):
            for b in range(0,self.dimension):
                if self.matrix[a,b] == 0 :
                    list_0.append([a,b])
                    
        #判断矩阵内为0的数的个数，如果为0,那么就不再生成新的数字
        if len(list_0) != 0:
            x = random.sample(list_0,1)[0]#注意random.sample()函数返回值类型为列表
            self.matrix[x[0]][x[1]] = random.randrange(2, 5, 2)
    
    def left_2048(self):#向左平移合并
        '''数字向左平移'''
        for i in range(0,self.dimension):
            list_i = list(self.matrix[i])
            while 0 in list_i:
                list_i.remove(0)
            while len(list_i) != self.dimension:
                list_i.append(0)
            self.matrix[i] = list_i
            
        '''水平向左合并'''
        for a in range(0,self.dimension):
            for b in range(0,self.dimension-1):
                if self.matrix[a][b] != 0 and self.matrix[a][b] == self.matrix[a][b+1]:
                    self.matrix[a][b] = 2 * self.matrix[a][b]
                    self.matrix[a][b+1] = 0
                else:
                    pass
                    
        '''数字向左平移'''
        for i in range(0,self.dimension):
            list_i = list(self.matrix[i])
            while 0 in list_i:
                list_i.remove(0)
            while len(list_i) != self.dimension:
                list_i.append(0)
            self.matrix[i] = list_i
            
    def right_2048(self):#向右平移合并
        for i in range(0,self.dimension):#将矩阵水平方向反转 eg：[[1,2],[3,4]]>>[[2,1],[4,3]]
            self.matrix[i] = self.matrix[i][::-1]
        self.left_2048()#注意在类中内置函数互相调用前面要加self.，也注意不要循环调用
        for i in range(0,self.dimension):#再将矩阵水平方向反转回来
            self.matrix[i] = self.matrix[i][::-1]

    def down_2048(self):#向下平移合并
        self.matrix = self.matrix[::-1]#先上下反转 eg:[[1,2],[3,4]]>>[[3,4],[1,2]]
        self.up_2048()
        self.matrix = self.matrix[::-1]#再上下反转回来eg:[[3,4],[1,2]]>>[[1,2],[3,4]]
    
    def up_2048(self):#向上平移合并
        self.matrix = np.transpose(self.matrix)#先转置 eg:[[1,2],[3,4]]>>[[1,3],[2,4]]
        self.left_2048()
        self.matrix = np.transpose(self.matrix)#再转置回来 eg:[[1,3],[2,4]]>>[[1,2],[3,4]]
        
    def print_2048(self):#显示
        for i in self.matrix:
            print(i)
        
    def input_2048(self):#输入
        while True:
            s = input("w(↑) a(←) s(↓) d(右)：")
            if s == "w":
                self.up_2048()
                break
            elif s == "a":
                self.left_2048()
                break
            elif s == "s":
                self.down_2048()
                break
            elif s == "d":
                self.right_2048()
                break
            else:
                print("输入有误请重新输入")
                continue
                

if __name__ == '__main__':#主程序
    g1 = Game2048()
    g1.generate_num()
    g1.generate_num()
    g1.generate_num()
    g1.print_2048()
    while True:
        g1.input_2048()
        g1.generate_num()
        g1.print_2048()
        if g1.judge_gameover() == True:
            print("Game over")
            brea
    '''2048游戏的类'''
    '''
        属性:
            self.dimension
            self.matrix
        方法：
            judge_gameover(self)
            generate_num(self)
            left_2048(self)
            right_2048(self)
            down_2048(self)
            up_2048(self)
            print_(self)
            input_(self)
    '''