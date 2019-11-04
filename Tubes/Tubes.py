with open('in.txt', 'r') as fin:
    third_tube_final = int(fin.readline())
    first_tube_start = int(fin.readline())
    second_tube_start = int(fin.readline())
    third_tube_start = 100 - (first_tube_start + second_tube_start)
    divisions = tuple(int(div) for div in fin.readline().split())


new_conditions = [(first_tube_start, second_tube_start, third_tube_start, 0)]
conditions_set = {(first_tube_start, second_tube_start, third_tube_start)}
final_steps = 0


def _start_transfusions():
    global new_conditions
    global conditions_set
    global final_steps

    for condition in new_conditions:

        first_tube = condition[0]
        second_tube = condition[1]
        third_tube = condition[2]
        steps = condition[3]

        # all transfusions from and to first tube
        transfusions_from_first = []
        transfusions_to_first = []

        for div in divisions:
            if div < first_tube:
                transfusions_from_first.append(first_tube - div)
            if div > first_tube:
                transfusions_to_first.append(div - first_tube)

        # transfuse from first tube
        for transfusion in transfusions_from_first:
            if transfusion + second_tube <= 100:
                new_condition = (first_tube - transfusion, second_tube + transfusion, third_tube)
                if conditions_set.isdisjoint({new_condition}):
                    new_conditions.append((*new_condition, steps + 1))
                    conditions_set.add(new_condition)
            if transfusion + third_tube <= 100:
                new_condition = (first_tube - transfusion, second_tube, third_tube + transfusion)
                if conditions_set.isdisjoint({new_condition}):
                    if new_condition[2] == third_tube_final:
                        final_steps = steps + 1
                        return
                    new_conditions.append((*new_condition, steps + 1))
                    conditions_set.add(new_condition)

        # transfuse to first tube
        for transfusion in transfusions_to_first:
            if transfusion <= second_tube:
                new_condition = (first_tube + transfusion, second_tube - transfusion, third_tube)
                if conditions_set.isdisjoint({new_condition}):
                    new_conditions.append((*new_condition, steps + 1))
                    conditions_set.add(new_condition)
            if transfusion <= third_tube:
                new_condition = (first_tube + transfusion, second_tube, third_tube - transfusion)
                if conditions_set.isdisjoint({new_condition}):
                    if new_condition[2] == third_tube_final:
                        final_steps = steps + 1
                        return
                    conditions_set.add(new_condition)
                    new_conditions.append((*new_condition, steps + 1))

        # all transfusions from and to second tube
        transfusions_from_second = []
        transfusions_to_second = []
        for div in divisions:
            if div < second_tube:
                transfusions_from_second.append(second_tube - div)
            if div > second_tube:
                transfusions_to_second.append(div - second_tube)


        # transfuse from second tube
        for transfusion in transfusions_from_second:
            if transfusion + first_tube <= 100:
                new_condition = (first_tube + transfusion, second_tube - transfusion, third_tube)
                if conditions_set.isdisjoint({new_condition}):
                    new_conditions.append((*new_condition, steps + 1))
                    conditions_set.add(new_condition)
            if transfusion + third_tube <= 100:
                new_condition = (first_tube, second_tube - transfusion, third_tube + transfusion)
                if conditions_set.isdisjoint({new_condition}):
                    if new_condition[2] == third_tube_final:
                        final_steps = steps + 1
                        return
                    new_conditions.append((*new_condition, steps + 1))
                    conditions_set.add(new_condition)

        # transfuse to second tube
        for transfusion in transfusions_to_second:
            if transfusion <= first_tube:
                new_condition = (first_tube - transfusion, second_tube + transfusion, third_tube)
                if conditions_set.isdisjoint({new_condition}):
                    new_conditions.append((*new_condition, steps + 1))
                    conditions_set.add(new_condition)
            if transfusion <= third_tube:
                new_condition = (first_tube, second_tube + transfusion, third_tube - transfusion)
                if conditions_set.isdisjoint({new_condition}):
                    if new_condition[2] == third_tube_final:
                        final_steps = steps + 1
                        return
                    new_conditions.append((*new_condition, steps + 1))
                    conditions_set.add(new_condition)

        # make third tube empty
        if first_tube + third_tube <= 100:
            new_condition = (first_tube + third_tube, second_tube, 0)
            if conditions_set.isdisjoint({new_condition}):
                if new_condition[2] == third_tube_final:
                    final_steps = steps + 1
                    return
                new_conditions.append((*new_condition, steps + 1))
                conditions_set.add(new_condition)
        if second_tube + third_tube <= 100:
            new_condition = (first_tube, second_tube + third_tube, 0)
            if conditions_set.isdisjoint({new_condition}):
                if new_condition[2] == third_tube_final:
                    final_steps = steps + 1
                    return
                new_conditions.append((*new_condition, steps + 1))
                conditions_set.add(new_condition)


_start_transfusions()

with open('out.txt', 'w') as fout:
    if third_tube_start == third_tube_final:
        final_steps = 0
        fout.write(str(final_steps))
    elif final_steps:
            fout.write(str(final_steps))
    else:
        fout.write('No solution')
