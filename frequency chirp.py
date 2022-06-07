import math
import cmath
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
p=math.pi
axis_color='white'
sigma=5                              #variance for defining gaussian pulse
freq_ini=-5                          #initial frequency
freq_final=5                         #final frequency
freq_range=freq_final-freq_ini       #frequency range
factor=100                           #number of points per unit frequency range

def efield_freq(E,sigma,beta,t_0):
    y=[]
    freq_intensity=[]
    for i in range(freq_range*factor):
        add=E*np.exp(-0.5*(2*p*sigma*(freq_ini+i/factor))**2)*cmath.exp(complex(0,beta*(freq_ini+i/factor)**2+(freq_ini+i/factor)*t_0))
        y.append(add)
        freq_intensity.append(add**2)
    E_t=np.fft.fft(y)                     #electric field in time domain
    intensity=E_t**2
    return freq_intensity                 #can be changed to E_t or intensity if required

freq=np.linspace(freq_ini,freq_final,freq_range*factor)
time=np.fft.fftfreq(len(freq))

fig = plt.figure()
ax=fig.add_subplot(111)
fig.subplots_adjust(top=0.935,bottom=0.38,left=0.08,right=0.955)

E_0=1
sigma_0=0.5
beta_0=0
t_0_0=2

[line]=ax.plot(freq,efield_freq(E_0,sigma_0,beta_0,t_0_0),linewidth=1)

E_slider_ax  = fig.add_axes([0.25, 0.15, 0.65, 0.03], facecolor=axis_color)
E_slider=Slider(E_slider_ax,'E (Amplitude)',0,1,valinit=E_0)

sigma_slider_ax=fig.add_axes([0.25, 0.20, 0.65, 0.03], facecolor=axis_color)
sigma_slider=Slider(sigma_slider_ax,'Variance for gaussian',0,1,valinit=sigma_0)

beta_slider_ax=fig.add_axes([0.25, 0.25, 0.65, 0.03], facecolor=axis_color)
beta_slider=Slider(beta_slider_ax,'Beta (chirp factor)',-10,50,valinit=beta_0)

t_0_slider_ax=fig.add_axes([0.25, 0.30, 0.65, 0.03], facecolor=axis_color)
t_0_slider=Slider(t_0_slider_ax,'Inital time',-50,50,valinit=t_0_0)

def slider_on_changed(val):
    line.set_ydata(efield_freq(E_slider.val,sigma_slider.val,beta_slider.val,t_0_slider.val))
    fig.canvas.draw_idle()

E_slider.on_changed(slider_on_changed)
sigma_slider.on_changed(slider_on_changed)
beta_slider.on_changed(slider_on_changed)
t_0_slider.on_changed(slider_on_changed)

#plt.ylim((-1,1))
plt.show()
