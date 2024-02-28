import os


for i in range(8):
    os.mkdir(f"TPC{i+1}")
    open(f"TPC{i+1}/.gitkeep", "w")

os.mkdir("Projeto")
open(f"Projeto/.gitkeep", "w")

os.m("Teste")
open(f"Teste/.gitkeep", "w")