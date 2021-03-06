from crpyto_tool.libs.extended_euclidean import ExtendedGcdEuclidean


def gcd_euclidean(lhs, rhs):
    if rhs == 0:
        return lhs
    else:
        return gcd_euclidean(rhs, lhs % rhs)


def test_extended_gcd_euclidean(modulo_num, another_num):
    extend_euclidean_algo = ExtendedGcdEuclidean(modulo_num=modulo_num, another_num=another_num)
    for i in range(0, len(extend_euclidean_algo.iter_list) - 1):
        print 'iter:' + str(extend_euclidean_algo.iter_list[i]) + '\t\tr:' + \
              str(extend_euclidean_algo.r_list[i]) + '\t\tq:' + \
              str(extend_euclidean_algo.q_list[i]) + '\t\tx:' + \
              str(extend_euclidean_algo.x_list[i]) + '\t\ty:' + \
              str(extend_euclidean_algo.y_list[i])

    i = len(extend_euclidean_algo.iter_list) - 1
    print 'iter:' + str(extend_euclidean_algo.iter_list[i]) + '\t\tr:' + \
          str(extend_euclidean_algo.r_list[i]) + '\t\tq:' + \
          str(extend_euclidean_algo.q_list[i])
    print


if __name__ == '__main__':
    print 'Demo gcd of 24 and 36 is:' + str(gcd_euclidean(24, 36)) + '\n'

    test_extended_gcd_euclidean(1759, 550)
    test_extended_gcd_euclidean(1137, 29)
    test_extended_gcd_euclidean(37, 49)
    test_extended_gcd_euclidean(49, 37)
    extend_euclidean_algo = ExtendedGcdEuclidean(modulo_num=37, another_num=49)
    print 'multiplicative inverse of 49 modulo 37 is:', extend_euclidean_algo.get_result()
