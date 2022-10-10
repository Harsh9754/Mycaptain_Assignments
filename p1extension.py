#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 17:17:43 2022

@author: harshmanishpatidar
"""

fn= input("Enter Filename: ")

f = fn.split(".")

print ("Extension of the file is : " + f[-1])