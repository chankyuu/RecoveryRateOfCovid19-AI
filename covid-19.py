%matplotlib notebook
# Author:- Anurag Gupta # email:- 999.anuraggupta@gmail.com
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep
#### ---- Step 1:- Download data
URL_DATASET = r'https://raw.githubusercontent.com/datasets/covid-19/master/data/countries-aggregated.csv'
df = pd.read_csv(URL_DATASET, usecols = ['Date', 'Country', 'Confirmed', 'Recovered', 'Deaths'])
#### ---- Step 2:- Create list of all dates
list_dates = df['Date'].unique()
#print(list_dates) # Uncomment to see the dates
#### --- Step 3:- Pick 5 countries. Also create ax object
fig, ax = plt.subplots(figsize=(15, 8))
# We will animate for these 5 countries only
list_countries = ['Japan', 'China', 'Vietnam', 'Mongolia','Malaysia']
# colors for the 5 horizontal bars
list_colors = ['black', 'red', 'green', 'blue', 'yellow']
### --- Step 4:- Write the call back function
# plot_bar() is the call back function used in FuncAnimation class object


def plot_bar(some_date):
 df2 = df[df['Date'].eq(some_date)]
 ax.clear()
 # 아시아 국가들에 대한 회복률(Recovered/Confiremd)을 구한다.
 df3 = df2[df2['Country'].isin(list_countries)] #df3은 'Japan', 'China', 'Vietnam', 'Mongolia','Malaysia' 대상으로 series 범위를 축소한다.
 recovered = df3['Recovered'] #recoverd는 Git에서 불러온 Recovered 데이터를 저장한다.
 confirmed = df3['Confirmed'] #confirmed는 Git에서 불러온 Confirmed 데이터를 저장한다.
 r = []
 c = []
 avg_rc = []
 for term in recovered : # recovered 변수에서 차례로 데이터 값을 r 리스트에 저장한다.
    r.append(term)
 for term in confirmed : # confirmed 변수에서 차례로 데이터 값을 c 리스트에 저장한다.
    c.append(term)   
 for i in range(len(r)) : # 데이터의 수만큼 회복률을 계산하여 avg_rc 리스트에 저장한다.
    if(c[i] == 0) :       # DivisionError일 때
        avg_rc.append(0)
    else :
        tmp = round((r[i] / c[i]), 4)
        avg_rc.append(tmp * 100)
 # print(df4) # Uncomment to see that dat is only for 5 countries
 sleep(0.2) # To slow down the animation
 # ax.barh() makes a horizontal bar plot.
 ax.set_xlabel("Recovery rate") # x축 label 셋팅
 return ax.barh(df3['Country'], avg_rc, color= list_colors)  # 아시아 국가들을 대상으로 회복률 데이터를 반환한다.
###----Step 5:- Create FuncAnimation object---------
my_anim = animation.FuncAnimation(fig = fig, func = plot_bar,
                                     frames= list_dates, blit=True,
                                     interval=30)
## ### --- Step 6:- Save the animation to an mp4

 # Place where to save the mp4. Give your file path instead
#plt.rcParmas는 ffmpeg가 저장된 장소
plt.rcParams['animation.ffmpeg_path'] = r'C:/bin/ffmpeg-4.3.1-2020-10-01-full_build/ffmpeg-4.3.1-2020-10-01-full_build/bin/ffmpeg.exe'
#path_mp4는 내가 mp4를 저장할 경로
path_mp4 = r"C:/Users/USER/Desktop/covid-19/recoveryrate_covid.mp4"
writervideo = animation.FFMpegWriter(extra_args= ['-vcodec', 'libx264', '-pix_fmt', 'yuv420p'], fps=30)
my_anim.save(filename = path_mp4, writer = writervideo, dpi=200)
plt.show()
