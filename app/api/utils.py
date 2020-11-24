from app import app
from math import log2
from flask import request

@app.route('/get_bin', methods=['POST'])
def get_bin(num=None):
    if request.method == "POST":
        num = request.form.get("data")
        grid_size = request.form.get("grid_size")
        if grid_size:
            return find_bin(int(num), int(grid_size))
        return find_bin(num)
    return num

@app.context_processor
def calc_log():
    def inner(num):
        return log2(num)
    return dict(calc_log=inner)

@app.context_processor
def calc_bin():
    return dict(calc_bin=find_bin)


def find_bin (num, grid_size = None):
    if grid_size:
        bin_num = bin(num)[2:]
        return bin_num if len(bin_num) >= grid_size else '0' * (grid_size - len(bin_num)) + bin_num
    else:
        return ' '.join(format(i, 'b') for i in bytearray(num, encoding ='utf-8')) 

def bin2str(bin):
    return "".join(map(lambda x: chr(int(x,2)), bin.split()))