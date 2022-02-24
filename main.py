# Idea source:
# https://www.youtube.com/watch?v=pvimAM_SLic

import matplotlib.pyplot as plt
import numpy as np


def main(n):
    res, dots = calculate_pi(n)
    plots(res, dots[0], dots[1], n)


def calculate_pi(n):
    points_in = 0
    points_total = 0
    # Creating array which contains numbers between 0 and 1
    # with shape 1 row and "n" columns
    x_arr = np.random.uniform(0, 1, (1, n))
    y_arr = np.random.uniform(0, 1, (1, n))
    x_in, y_in = [], []
    x_off, y_off = [], []
    for x, y in zip(x_arr[0], y_arr[0]):
        r = np.sqrt(x ** 2 + y ** 2)
        if r <= 1:
            points_in += 1
            x_in.append(x)
            y_in.append(y)
        else:
            x_off.append(x)
            y_off.append(y)
        points_total += 1
    dots_in = np.array([[x_in], [y_in]])
    dots_off = np.array([[x_off], [y_off]])
    
    return (4 * (points_in / points_total), (dots_in, dots_off))


def plots(res, inside, outside, num):
    plt.style.use('grayscale')
    plt.rcParams.update({'font.family': 'Arial'})
    fig, ax = plt.subplots(figsize=(10, 10), dpi=80, facecolor='#161616')
    circle = plt.Circle((0, 0), 1.0, color='c', fill=False, lw=2)
    
    ax.set_facecolor('#1F1F1F')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['top'].set_color('white')
    ax.tick_params(axis='both', colors='white', labelsize=15)
    ax.set_aspect(1)
    ax.add_patch(circle)
    
    ax.set_title(f'With n = {num}\nπ = {res}',
                fontsize=20, 
                fontname='Cambria',
                fontstyle='italic',
                color='white', 
                pad=20
    )
   
    # Dots in the circle 
    ax.scatter(inside[0], inside[1], c='#ee9b00', s=2)
    
    # Dots off the circle 
    ax.scatter(outside[0], outside[1], c='#7209b7', s=2)
    
    plt.xlim([-1.0, 1.0])
    plt.ylim([-1.0, 1.0])
    plt.grid(color='#adb5bd')
    plt.show()
    

if __name__ == '__main__':
    main(100000)