from os import listdir, rename
import re
import time
import matplotlib.pyplot as plt
import pandas as pd

def get_cycle(f):
    df=pd.read_excel(f)[1:]
        
    if not 'Potential' in df.columns[0]:
        print('You should copy datas to A1')

    df.columns=['potential','current']
    x_scale=[ min(df['potential']), max(df['potential']) ]

    moving = 1 # 1,2 : ->, 3,4 : <-
    cycle=[]
    cycle_number=0

    for i,row in df.iterrows():
        if moving==1 and x_scale[1]*0.985<row[0]: # -> entered max area
            moving=2
        elif moving==2 and x_scale[1]*0.985>row[0]: # -> passed max area
            moving=3
        elif moving==3 and row[0]*0.985<x_scale[0]: # -> entered min area
            moving=4
        elif moving==4 and row[0]*0.985>x_scale[0]: # -> passed min area
            moving=1
            cycle.append(i-1)

    if moving==4:
        cycle.append(len(df)-1)
    cycle_number=len(cycle)
    print('cycle number : %d'%cycle_number)

    return df,cycle,cycle_number

doing=True
while doing:
    files = [f for f in listdir('.') if re.match('py(.*)+\.xlsx',f)]
    # print(files)

    if len(files)==0:
        print('There aren\'t any target files. Put \'py\' infront of the name of target files')
        time.sleep(2)
        break

    else:
        flag=True if len(files)==1 else False

        plots=[]
        for f in files:
            df,cycle,cycle_number = get_cycle(f)

            start=0
            for i,x in enumerate(cycle):
                if flag:
                    plt.plot(df['potential'][start:x],df['current'][start:x])

                min_current_idx=df['current'][start:x].idxmin()
                min_current=min(df['current'][start:x])

                max_current_idx=df['current'][start:x].idxmax()
                max_current=max(df['current'][start:x])
                
                print('Cycle #%d'%(i+1))
                print('ia/ic : %.4f'%(abs(max_current/min_current))) #max/min

                max_potential = df['potential'].iloc[max_current_idx]
                min_potential = df['potential'].iloc[min_current_idx]
                print('delta E : %.4f'%(max_potential-min_potential))
                print('')

                start=x
            
            print(cycle)
            # print(cycle_number)
            print('##### File : %s finished. #####\n\n'%f[2:])
            
            # labeling method
            try:
                label=f[2:-5].split('(')[1].split(')')[0]
            except:
                label=f[2:-5].split('-')[0].split(' ')[0]
            
            # tmplot : last cycle's data
            tmplot, = plt.plot(df['potential'][cycle[cycle_number-2]:cycle[cycle_number-1]], df['current'][cycle[cycle_number-2]:cycle[cycle_number-1]],label=label)
            plots.append(tmplot)
            
            rename(f,f[2:])

        # drawing graph of all 'py*.xlsx' files
        
        if flag:
            plt.title('CV of %d cycles'%cycle_number)
            plt.show()
        else:
            plt.title('CV of last cycle')
            plt.legend(handles=plots)
            plt.show()

        doit=input('press enter to exit, \'r\' to calc again')
        if doit!='r':
            break
