from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg
import pandas

app = QtGui.QApplication([])
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')
win = pg.GraphicsWindow(title="Basic plotting examples")
win.resize(640,480)
win.setWindowTitle('pyqtgraph example: Plotting')

# Enable antialiasing for prettier plots
pg.setConfigOptions(antialias=True)


p6 = win.addPlot(title="Temperature Plot")
#curve = p6.plot(pen='w')
#global data
##def data_1():
##    data = np.random.normal(size=(10,1000))
##    print(data)
##    return data
##data=[]
##new=[]
##def data_1():
##    global data,new
##    
##    with open("myfaisal.txt","r") as f:
##            text=f.read()
##    x=text.split()
##    for y in x:
##            data.append(y[0])
##    for m in data:
##        new.append(int(m))
##    print(new)
##    return new


ptr = 0
#data = np.random.normal(size=(10,100000))
#data=np.int(data)
#def data():
#data=[1,2,3,4,6,7,8,9,10,11,12,13,14,15,16,17]
#print(data)
def data_2():
    df=pandas.read_csv('1.csv')
    return (df['Temperature'])
def data_3():
    df=pandas.read_csv('1.csv')
    return (df['Time'])

def data_1():
        with open("myfaisal.txt","r") as f:
                text=f.readlines()
                return text
def now_1():
    q=[0,0]
    x=0
    data=[]
    new=[]
    now=[]
    woo=[]
    while True:
        m_1=data_1()
        q.append(m_1)
        x=x+1
        if q[x]!=q[x+1]:
            for line in m_1:
                w=line.split()
                now.append(float(w[0]))
            return now
def now_2():
        q=[[0],[0]]
        q_1=[[0],[0]]

        l_1=[[0],[0]]
        t=0
        n=0
        #print(list(data_1()))
        ##for x in range(0,10):
        while True:
              m_1=list(data_2())
              m_2=list(data_3())
              q.append(m_1)
              q_1.append(m_2)
              #l_1.append(q)
              t=t+1
              n=n+1
              #print(q)
              #break
              if (q[t]!=q[t+1]):
                  #print(q)
                  return(q[-1])
              #if (q_1[n]!=q_1[n+1]):
                  #print(q)
                  #print(q_1[-1])
def now_3():
        q=[[0],[0]]
        q_1=[[0],[0]]

        l_1=[[0],[0]]
        t=0
        n=0
        #print(list(data_1()))
        ##for x in range(0,10):
        while True:
              m_1=list(data_2())
              m_2=list(data_3())
              q.append(m_1)
              q_1.append(m_2)
              #l_1.append(q)
              t=t+1
              n=n+1
              #print(q)
              #break
##              if (q[t]!=q[t+1]):
##                  #print(q)
##                  print(q[-1])
              if (q_1[n]!=q_1[n+1]):
                  #print(q)
                  return(q_1[-1])
def update():

    global curve,data,new,now,q,woo, ptr, p6
    time=QtCore.QTime.currentTime().toString()
    print(time)
    
    curve=p6.plot(now_3(),now_2(),pen=pg.mkPen('r',width=1))
    curve=p6.plot(now_3(),now_2(),pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')
    #p6.enableAutoRange('xy', False)        
##    
##    #curve.setData(data[ptr%10])
##    
    #curve.setData(data_1())
    #curve = p6.plot(data_1(),pen='r')
    #curve.setData()
##    if ptr == 0:
##        p6.enableAutoRange('xy', False)  ## stop auto-scaling after the first data set is plotted
##    ptr += 1
##    time=QtCore.QTime.currentTime().toString()
##    print(time)
    
timer = QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)
#print(timer)


#win.nextRow()
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
