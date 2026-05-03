"""
Download DDR dataset from Roboflow.
API key taken from the original train.ipynb.
"""
import subprocess
import sys

# Pastikan roboflow terinstall
subprocess.check_call([sys.executable, "-m", "pip", "install", "roboflow", "-q"])

from roboflow import Roboflow

rf = Roboflow(api_key="Q1flzyg1J8Z2OMweLXf3")
project = rf.workspace("weapon-mpr3p").project("ddr-dataset-yyvzp")
version = project.version(1)
dataset = version.download("folder")

print(f"\nDataset downloaded to: {dataset.location}")
