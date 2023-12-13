
class not2DError(Exception):
    # Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'


class unevenListError(Exception):
    # Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'


class improperMatrixError(Exception):
    # Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1, arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum += arr1[i]*arr2[i]
    return sum


class list_D2(list):
    def __init__(self, arr):

        # is a valid matrix
        is_2d = False
        is_even = False

        if all(isinstance(sublist, list) for sublist in arr) == False:
            raise not2DError()
        else:
            is_2d = True

        if all(len(sublist) == len(arr[0]) for sublist in arr) == False:
            raise unevenListError()
        else:
            is_even = True

        if is_2d and is_even:
            self.arr = arr

        ######

        self.extend(arr)

    def __str__(self):

        # of cols and rows in string type
        cols = str(len(self.arr))
        rows = str(len(self.arr[0]))

        # return the shape of list_2d
        return 'list_2D: '+cols+'*'+rows

    def transpose(self):

        # calculates the transposed matrix
        transposed_arr = [[self.arr[j][i] for j in range(
            len(self.arr))] for i in range(len(self.arr[0]))]

        return list_D2(transposed_arr)

    def __matmul__(self, others):

        # raise an error if it isn't a proper matmul

        if (len(self.arr[0]) != len(others.arr)):
            raise improperMatrixError()

        else:
            result = []
            for i in range(len(self.arr)):
                row = []
                for j in range(len(others.arr[0])):
                    element_sum = 0
                    for k in range(len(self.arr[0])):
                        element_sum += self.arr[i][k] * others.arr[k][j]
                    row.append(element_sum)
                result.append(row)

        return list_D2(result)

    def avg(self):

        # calculates the sum of element in matrix
        total = 0

        # the total elements in matrix
        num_element = len(self.arr) * len(self.arr[0])

        for i in range(len(self.arr)):
            for j in range(len(self.arr[0])):
                total += self.arr[i][j]

        # calculates the average
        average = total / num_element

        return average
