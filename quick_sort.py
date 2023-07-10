# 88200963


def quick_sort(array):
    def pivot_comparison(elem, pivot):
        (pivot_name, pivot_tasks_done, pivot_penalty) = pivot
        (elem_name, elem_tasks_done, elem_penalty) = elem
        return True \
            if (elem_tasks_done < pivot_tasks_done) \
               or (elem_tasks_done == pivot_tasks_done and elem_penalty > pivot_penalty) \
               or (elem_tasks_done == pivot_tasks_done and elem_penalty == pivot_penalty and elem_name > pivot_name) \
            else False



    def inner_quick_sort(left, right):
        def partition():
            pointer = left - 1
            for elem in range(left, right):
                if not pivot_comparison(array[elem], array[right]):
                    pointer = pointer + 1
                    (array[pointer], array[elem]) = (array[elem], array[pointer])
            (array[pointer + 1], array[right]) = (array[right], array[pointer + 1])
            return pointer + 1

        if left < right:
            pivot = partition()
            inner_quick_sort(left, pivot - 1)
            inner_quick_sort(pivot + 1, right)

    inner_quick_sort(0, len(array) - 1)

    return array


if __name__ == "__main__":
    participants = ['alla 4 100', 'gena 6 1000', 'gosha 2 90', 'rita 2 90', 'timofey 4 80']
    participants = [person.split(' ') for person in participants]
    participants = [[name, int(tasks), int(penalty)] for name, tasks, penalty in participants]

    #participants_count = int(input())
    #participants = [input() for _ in range(participants_count)]
    #participants = [participant.split(' ') for participant in participants]
    #participants = [[name, int(tasks), int(penalty)] for name, tasks, penalty in participants]

    participants = quick_sort(participants)
    print(*[name for name, tasks, penalty in participants], sep='\n')
