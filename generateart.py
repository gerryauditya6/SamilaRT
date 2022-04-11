""" Credit : https://github.com/gerryauditya6 
             https://instagram.com/gerryaudityaa
             https://twitter.com/particleverse"""
   

from samila import *
import uuid
import random
import math
import streamlit as st
import matplotlib.pyplot as plt

def main():
    filename = str(uuid.uuid4())
    l = [Projection.RECTILINEAR , Projection.POLAR , Projection.AITOFF , Projection.HAMMER , Projection.LAMBERT , Projection.MOLLWEIDE]
    gradient = ['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'turbo', 'turbo_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']

    def f1(x, y):
        result = random.uniform(-1, 1) * y * x + math.cos(x ** 2) + random.gauss(0, 1)
        return result
    def f2(x, y):
        result = random.uniform(-1, 1) * y * x + math.cos(x ** 2) + random.gauss(0, 1) + math.sin(x * y) + 2** random.gauss(0, 5)
        return result
    def f3(x, y):
        result = random.uniform(-1, 1) * y * x + math.cos(x ** 2) + random.gauss(0, 1)
        return result
    def f4(x, y):
        result = random.uniform(-1, 1) * y * x + math.cos(x ** 2) + random.gauss(0, 1) + math.sin(x * y) + 2** random.gauss(0, 5)
        return result

    g1 = GenerativeImage(f1,f2)
    g2 = GenerativeImage(f3,f4)
    g1.generate(seed=random)
    g2.generate(seed=random)
    g1.plot(bgcolor="black", projection=random.choice(l))
    fig1 = g1.fig
    ax = fig1.get_axes()[0]
    ax.scatter(
        g1.data2,
        g1.data1,
        alpha=0.06,
        cmap=random.choice(gradient),
        c=g1.data2,
        s=0.06,)
    ax.scatter(
        g2.data2,
        g2.data1,
        alpha=0.06,
        cmap=random.choice(gradient),
        c=g2.data2,
        s=0.06)

    g1.save_data(file_adr=filename + "." + "json")
    g1.save_image(file_adr=filename, depth=2)

main()
