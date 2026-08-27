import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import pandas as pd
#libraries

df = pd.read_csv('Depth Data.csv')
df = df.replace("#VALUE!", np.nan)
#loading the given csv file and replacing the missing values with NaN
s = pd.to_numeric(df["Depth (m)"])

s1=[]
for i in range(len(s)):
    low=max(0,i-7)
    high=min(i+7,len(s))
    s1.append(np.nanmedian(s[low:high]))
t=np.arange(1,len(s)+1,1)
#The given data points were erratic, this loop smooths out the data points while ignoring nan.
#If nan was not ignored then around the value 97

fig, ax = plt.subplots()
ax.grid()
ax.set_xlabel("Time (s)")
ax.set_ylabel("Depth (m)")
ax.set_title("Ship Depth Over Time")
ax.set_xlim(t[0], t[-1])
ax.set_ylim(np.nanmin(s1), np.nanmax(s1)*0.9)
#np.nanmax(s1) has been scaled down as all the values are negative.
#To give more negative space above the graph the max has to be scaled down

line, = ax.plot([], [])
dots, = ax.plot([], [], marker='o', markersize=2.5, linestyle='none', color='red', alpha=0.2)

def update(frame):
    line.set_data(t[:frame+1], s1[:frame+1])
    dots.set_data(t[:frame + 1], s1[:frame + 1])
    return line, dots,
#The update function, this creates new data points and lines as and when the function is called during ani therevy creating an animation

ani = anim.FuncAnimation(fig, update, frames=len(t), interval=100)
#frames dictates how many times to call the function update
plt.show()