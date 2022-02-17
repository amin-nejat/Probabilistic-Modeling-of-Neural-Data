# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 18:35:46 2022

@author: Amin
"""

import matplotlib.pyplot as plt
import numpy as np
import logging

logging.getLogger('matplotlib.font_manager').disabled = True

# %%
def plot_signals(x,z=None,titlestr='',fontsize=12,linewidth=2,save=False,file=None):
    """Plot multivariate signals and their corresponding states
    """
    plt.figure(figsize=(10,3))
    
    offset = np.append(0.0, np.nanmax(x[:,0:-1,],0)-np.nanmin(x[:,0:-1],0))
    s = (x-np.nanmin(x,0)[None,:]+np.cumsum(offset)[None,:])
    
    plt.plot(s,linewidth=linewidth)
    
    if z is not None:
        colors = plt.cm.hsv(np.linspace(0,1,max(z)+2)[0:-1])[:,0:3]
        t = np.arange(len(z))
        for z_ in range(max(z)+1):
            plt.vlines(x=t[z==z_], ymin=(s.min()-1), ymax=(s.max()+1), 
                       color=colors[z_], alpha=.1, lw=1)

    plt.yticks(s[0,:],[str(signal_idx) for signal_idx in range(s.shape[1])])
        
    if save:
        plt.savefig(file+'.png',format='png')
        plt.savefig(file+'.pdf',format='pdf')
        plt.close('all')
    else:
        plt.show()

# %%
def plot_grad_norms(gradient_norms):
    """Norms of the gradients of SVI variables
    """
    plt.figure(figsize=(10,4), dpi=100).set_facecolor('white')
    for name, grad_norms in gradient_norms.items():
        plt.plot(grad_norms, label=name)

    plt.xlabel('iters')
    plt.ylabel('gradient norm')
    plt.yscale('log')
    plt.legend(loc='best')
    plt.title('Gradient norms during SVI');

    plt.show()
    
# %%
def plot_loss(losses):
    """Plot losses as a function of iterations
    """
    plt.figure(figsize=(10,3), dpi=100).set_facecolor('white')
    plt.plot(losses)
    plt.xlabel('iters')
    plt.ylabel('loss')
#     plt.yscale('log')
    plt.title('Convergence of SVI')
    plt.show()

# %%
def plot_gmm_2d(data,mu,pi,z,weights=None,locs=None):
    """Plot Gaussian Mixture Model (GMM) true and inferred variables
    """
    colors = plt.cm.hsv(np.linspace(0,1,max(z)+2)[0:-1])[:,0:3]

    plt.scatter(data[:,0],data[:,1],s=.5,c=colors[z])
    plt.scatter(mu[:,0],mu[:,1],s=pi*1000,c=(0,0,0,0),marker='o',edgecolors='r')
    
    if locs is not None:
        plt.scatter(locs[:,0],locs[:,1],s=weights*1000,c='w',marker='o',edgecolors='k')

    plt.axis('equal')
    plt.show()
    
# %%
def plot_transition(mat,titles):
    """Plot ture and inferred transition matrix
    """
    for i in range(len(mat)):
        plt.subplot(1,len(mat),i+1)
        plt.imshow(mat[i])
        plt.title(titles[i])
        plt.axis('off')
    
    plt.show()