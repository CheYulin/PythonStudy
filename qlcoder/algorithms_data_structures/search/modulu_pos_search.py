#!/usr/bin/python
# coding:utf-8

import urllib2
import re
import modulo


def execute_answer():
    headers = {
        'Cookie': 'gr_user_id=3949c66a-56d6-49be-99e6-dc48710481cd; uuid=5811c0d121dd4; è¿é¢çç­æ¡æ¯oreo=eyJpdiI6Ik13RVwvTVlPd0pHMGFkWTJFdElndnhRPT0iLCJ2YWx1ZSI6ImJKUlMxaFA4a1lYV2J3b0NnN0ZUS1E9PSIsIm1hYyI6ImRjZTBjYjU4NDg5ZjNjYjk5OGNmZmE0MTk2MWU1NmIyMTA4NmViMmM2OWUxYTA3NjdhYjNiODdlOTNkMmFlNTYifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IndsTFlJekoreDNFcTltQjJvQWYwNVE9PSIsInZhbHVlIjoiYis4SnV6SjliMWRhRVc0VnJzOVNCZGd6THREVENtOVR2ejV5QUQwRVNLdElFa2taeCs3cWJteVBseVdhdXJ2ZEI3SWRPd3pmNnRXSHNaeERBcVdaRHc9PSIsIm1hYyI6IjBhODM4MjczODQ3MmU3MDgzNWQ2OThiMGVmYzdkMjEzNWNhOWRiNmMxMjgzNDlkYjI1ZjBlYjMxYWU0NjVhZjcifQ%3D%3D; laravel_session=eyJpdiI6IkpPWGlaWXBmSWkzYVwvdE5NYTdUbWR3PT0iLCJ2YWx1ZSI6IndxZXN4MUdFc0pQTkFLZENWM1ZxMmxuMkRzODh0R0dUQ2liVVlJYlZkTmpodUVnR3g0YzR2bnRMNVBiR1hkMkhMdHN1RXFyY3NJME12VGtTWUFYa0pnPT0iLCJtYWMiOiI1NjAxODE1MjM5YjNiYzYyMDE5NjBlZTRlNWNlOWYxNzllY2Y5NjQ1ZThlNjI3N2MwOWI1YmY1ZWFmNDgyZTdlIn0%3D; gr_session_id_80dfd8ec4495dedb=00c7f621-140a-44d1-b53c-d356c37de177; Hm_lvt_420590b976ac0a82d0b82a80985a3b8a=1477531541,1477533371,1477535066,1477558482; Hm_lpvt_420590b976ac0a82d0b82a80985a3b8a=1477566715'
    }

    request = urllib2.Request('http://www.qlcoder.com/train/automodu', headers=headers)

    response_stream = urllib2.urlopen(request, timeout=200)
    html_str = response_stream.read()
    my_list = html_str.split('\n')
    for ele in my_list:
        if re.match('.*level.*modu.*map.*\}', ele):
            json_str = ele[0:len(ele) - 4]
            print json_str


def get_piece_list(pieces_info):
    return [transform_piece_str_to_grid(ele) for ele in pieces_info]


def transform_piece_str_to_grid(piece_str):
    rows = piece_str.split(',')
    return [map(lambda info_ch: 1 if info_ch == 'X' else 0, row) for row in rows]


def transform_map_str_to_grid(map_str):
    return [map(lambda info_ch: ord(info_ch) - ord('0'), row) for row in map_str]


def sum_piece_arr(piece_arr):
    my_sum = 0
    for row in piece_arr:
        for col in row:
            my_sum += col
    return my_sum


if __name__ == '__main__':
    my_json_str = {"level": 3, "modu": "2", "map": ["100", "010", "011"], "pieces": ["XXX", "X", ".X,XX", "X,X,X"]}
    my_json_dict = dict(my_json_str)

    modulo_num = int(my_json_dict['modu'])
    map_arr = transform_map_str_to_grid(my_json_str['map'])
    map_row = len(map_arr)
    map_col = len(map_arr[0])

    pieces_info = my_json_dict['pieces']
    pieces_list = get_piece_list(pieces_info=pieces_info)
    piece_sum_list = map(lambda piece_arr_ele: sum_piece_arr(piece_arr_ele), pieces_list)

    print 'map_row:', map_row, ', map_col:', map_col, ', map_info:', map_arr, ', pieces:', pieces_list, ', pieces sum:', piece_sum_list
    left_cells = reduce(lambda x, y: x + y, piece_sum_list)
    print 'left cells:', left_cells
    path_list = list()
    print modulo.fixed_depth_search(0, left_cells, path_list, pieces_list, piece_sum_list, map_arr, modulo_num)
    print path_list
