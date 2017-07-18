# -*- coding: utf-8 -*-
import matplotlib
matplotlib.use('TkAgg')
import nltk 
'''
☼ Produce a dispersion plot of the four main protagonists in
Sense and Sensibility: Elinor, Marianne, Edward, and Willoughby.
What can you observe about the different roles played by the males
and females in this novel?  Can you identify the couples?

'''
from nltk.book import text2
text2.dispersion_plot(["Elinor","Marianne","Edward","Willoughby"])
'''
Females appear more frequently compared to males.
Elinor-Edward, Marianne-Willoughby.
'''