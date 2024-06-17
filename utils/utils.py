import os
import sys

import pandas as pd


class Utils:
    @staticmethod
    def get_resource_path(relative_path):
        """Get the absolute path to the resource, works for dev and for PyInstaller"""
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    @staticmethod
    def get_app_favicon():
        return Utils.get_resource_path("assets/minero-pro.svg")

    @staticmethod
    def get_github_icon():
        return Utils.get_resource_path("assets/github-icon.svg")

    @staticmethod
    def get_minero_pro_image():
        return Utils.get_resource_path("assets/minero-pro.svg")

    @staticmethod
    def read_coordinates(filename):
        df = pd.read_csv(
            filename, header=None, names=["X", "Y", "Z", "Tonelaje", "Metal", "Metal2"]
        )
        return df
