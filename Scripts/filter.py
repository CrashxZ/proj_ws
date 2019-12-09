import numpy as np
import json
import importlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def loadJSON():
    _pathArray = []
    with open("coordinates.json", "r") as file:
        for lines in file.readlines():
            _pathArray.append(json.loads(lines))
    return _pathArray


def filter(_pathData, _nIterations):
    _delta = ""
    _errorL = 0.2
    _errorH = 2
    _iteration = 0
    while _iteration < _nIterations:
        _counter = 1
        while _counter < len(_pathData):

            _delta = {
                'x': _pathData[_counter]['x'] - _pathData[_counter - 1]['x'],
                'y': _pathData[_counter]['y'] - _pathData[_counter - 1]['y'],
                'z': _pathData[_counter]['z'] - _pathData[_counter - 1]['z']
            }

            if (abs(_delta['x']) < _errorL or abs(_delta['y']) < _errorL or abs(_delta['z']) < _errorL
                    or abs(_delta['x']) > _errorH or abs(_delta['y']) > _errorH or abs(_delta['z']) > _errorH):
                _pathData.pop(_counter)

            _counter += 1
        _iteration += 1
        print _counter
    _filteredPath = _pathData
    return _filteredPath


def plotter(_pathGraph):
    _pointCounter = 0
    fig = plt.figure()
    ax = plt.axes(projection="3d")

    while _pointCounter < len(_pathGraph):
        _x = [_pathGraph[_pointCounter]['x']]
        _y = [_pathGraph[_pointCounter]['y']]
        _z = [_pathGraph[_pointCounter]['z']]
        ax.scatter(_x, _y, _z, c='b', marker='.', linewidths=0.01)
        _pointCounter += 1
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.title('Flight Data')
    plt.grid(True)
    plt.show()

def write_to_file(_filtered_Path):
    with open("filtered_path.json", "w") as file:
        if (_filtered_Path != ""):
            for _points in _filtered_Path:
                json.dump(_points, file)
                file.write('\n')


if __name__ == "__main__":
    _filterIterations = input("Enter the number of filter iterations: ")
    _data = loadJSON()
    _finalPath = filter(_data, _filterIterations)
    plotter(_finalPath)
    write_to_file(_finalPath)
