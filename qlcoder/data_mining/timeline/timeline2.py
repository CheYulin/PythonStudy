import random
import sys
import hashlib
import numpy
import string

global_digest_list = list()
limit = 10000000
vertex_list = numpy.ndarray(limit + 1)
my_primes = list()


def init_things():
    if sys.version_info[0] == 3:
        print ("Welcome to qlcoder!")
        print ("We find your Python version is python3.X")
        print ("But this script needs to be executed with Python2.X\n")
        exit()

    global vertex_list
    random.seed(10)
    vertex_list = map(lambda ele: [], vertex_list)

    global my_primes
    with open("primes.txt") as fs:
        my_primes = fs.readlines()
    my_primes = set(map(lambda e: int(e), my_primes))

    print len(my_primes)


def compute_md5(str_list):
    res_str = '-'.join(str_list)
    return hashlib.md5(res_str).hexdigest()


def verbose_time_line(vertex_index):
    if len(vertex_list[vertex_index]) == 0:
        global_digest_list.append(hashlib.md5("").hexdigest())
    else:
        vertex_list[vertex_index].reverse()
        if len(vertex_list[vertex_index]) == 1:
            global_digest_list.append(hashlib.md5(vertex_list[vertex_index][0]).hexdigest())
        else:
            global_digest_list.append(compute_md5(vertex_list[vertex_index]))
        vertex_list[vertex_index] = list()


def notify_message(vertex_index, message_str):
    if my_primes.__contains__(vertex_index):
        for listeners_index in range(1, vertex_index):
            vertex_list[listeners_index].append(message_str)
    times_count = 2
    notified_vertex_index = times_count * vertex_index
    while notified_vertex_index < limit + 1:
        vertex_list[notified_vertex_index].append(message_str)
        times_count += 1
        notified_vertex_index = times_count * vertex_index


if __name__ == '__main__':
    init_things()
    for i in range(limit):
        r = random.randint(1, limit)
        if i % 3 == 0:
            my_message_str = ''.join(random.sample(string.ascii_letters, 4))
            notify_message(r, my_message_str)
        else:
            verbose_time_line(r)
        if i == 99 or i == 299 or i == 999 or i == 23030 or i == 49999 or i == 66665 or i == 100000 - 1:
            print str(i) + ':' + compute_md5(global_digest_list)
        if i % 100000 == 0:
            print i

    print compute_md5(global_digest_list)
