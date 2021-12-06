 #1.每个节点随机初始化聚类中心点、拉格朗日乘数（初始化有什么规律吗）、u>0
 #2.在每个节点上，数据点分配给他最近的中心点。
 #3.给每个节点根据广播自己的中心点，以及给下一个邻居（节点编号加一的邻居）发送拉格朗日乘数。
 #4.每个节点更新中心点。
 #5.每个节点更新拉格朗日乘数。
 # 重复2-5 直到达到收敛（最大迭代次数）

from mpi4py import MPI
import numpy as np
maxIte=10  #最大迭代次数
def InitClusterCenter(data,k):#初始化中心点
    center=np.zeros([len(data),k])
    return center
def Init():
    comm=MPI.COMM_WORLD
    rank=comm.Get_rank()
    size=comm.Get_size()
    data=np.loadtxt('dataset/seeds/seeds%d',rank)

def PSDKM():
    comm=MPI.COMM_WORLD
    rank=comm.Get_rank()
    size=comm.Get_size()
    
if __name__=="__main__":
    for i in range(maxIte):
        PSDKM()