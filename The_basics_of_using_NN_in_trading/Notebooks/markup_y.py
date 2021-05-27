import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr 
import matplotlib.pyplot as plt


#=======================SELL==============================

def SELL(data, counter_lvl):
    
    plt.figure(figsize=(22, 8))
    
    signals = pd.DataFrame() # dataframe для записи сигналов

    #df['High'].plot(label='high')
    data['Close'].plot(label='close')
        
    pivots =[]
    dates = []
    counter = 0
    lastPivot = 0
    Range = [0,0,0,0,0,0,0,0,0,0]
    daterange = [0,0,0,0,0,0,0,0,0,0]
        
    for i in data.index:
        currentMax = max(Range , default=0)
        #value=round(df["High"][i],2)
        value=round(data['Close'][i], 2)
            
        Range=Range[1:9]
        Range.append(value)
        daterange=daterange[1:9]
        daterange.append(i)
            
        if currentMax == max(Range , default=0):
            counter+=1
        else:
            counter = 0
        if counter ==  counter_lvl:
            lastPivot = currentMax
            dateloc = Range.index(lastPivot)
            lastDate = daterange[dateloc]
            pivots.append(lastPivot)
            dates.append(lastDate)
    print()
    timeD = dt.timedelta(days=500)
    
        
    for index in range(1, len(pivots)):
        #print(str(pivots[index]) + " :" + str(dates[index]))
        line = pd.DataFrame({'Date':[dates[index]], 'price':[pivots[index]], 'Signal':[-1]})
        signals = signals.append(line, ignore_index=True)
        
        #plt.plot_date([dates[index], dates[index] + timeD],
        #    [pivots[index], pivots[index]] , linestyle='solid' , linewidth=1, marker=',', color='red')
            
        plt.plot_date([dates[index], dates[index]],
            [pivots[index], pivots[index]], marker='v', color='red')
    
    plt.grid()
    plt.show()

    return signals




#=======================BUY==============================

def BUY(data, counter_lvl):
    
    plt.figure(figsize=(22, 8))
    
    signals = pd.DataFrame() # dataframe для записи сигналов

    #df['Low'].plot(label='low')
    data['Close'].plot(label='close')
        
    pivots =[]
    dates = []
    counter = 0
    lastPivot = 0
    Range = [0,0,0,0,0,0,0,0,0,0]
    daterange = [0,0,0,0,0,0,0,0,0,0]
        
    for i in data.index:
        currentMax = min(Range , default=0)
        #value=round(df["Low"][i], 2)
        value=round(data['Close'][i], 2)
        
            
        Range=Range[1:9]
        Range.append(value)
        daterange=daterange[1:9]
        daterange.append(i)
            
        if currentMax == min(Range , default=0):
            counter+=1
        else:
            counter = 0
        if counter ==  counter_lvl:
            lastPivot=currentMax
            dateloc =Range.index(lastPivot)
            lastDate = daterange[dateloc]
            pivots.append(lastPivot)
            dates.append(lastDate)
    print()
    timeD = dt.timedelta(days=500)
        
        
    for index in range(1, len(pivots)):
        #print(str(pivots[index]) + " :" + str(dates[index]))
        line = pd.DataFrame({'Date':[dates[index]], 'price':[pivots[index]], 'Signal':[1]})
        signals = signals.append(line, ignore_index=True)
            
        #plt.plot_date([dates[index], dates[index] + timeD],
        #    [pivots[index], pivots[index]] , linestyle='solid' , linewidth=1, marker=',', color='red')
            
        plt.plot_date([dates[index], dates[index]],
            [pivots[index], pivots[index]], marker='^', color='green')
    
    plt.grid()
    plt.show()
    return signals
