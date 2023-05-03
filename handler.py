import random
import time

from config import commandsCount, commandsCountMassive, commandsCountMassiveCoordinates, field, blockCount, start, c_n, sinking


def _handler():
    global field, commandsCountMassiveCoordinates, commandsCountMassive, start
    # print(commandsCount)
    for i in range(commandsCount):


        commandCoordinates = commandsCountMassiveCoordinates[i]

        # for coord in commandCoordinates:
        #     if random.choice([True, False]):
        #         field[coord[0]][coord[1]][3] += random.randint(1, 10)
        # for j in range(random.randint(0, len(commandCoordinates))):
        #     random_cell = random.choice(commandCoordinates)
        #     field[random_cell[0]][random_cell[1]][3] += random.randint(1, 10)

        command = commandsCountMassive[i]
        commandCoordinates = commandsCountMassiveCoordinates[i]
        # print(f'Индекс - {i} - Ячеек: {len(commandCoordinates)}\n'
        #       f'{commandCoordinates}')
        # print(commandsCountMassiveCoordinates[0])

        free_cell = []
        for coord in commandCoordinates:
            vrag = 0
            drug = 0
            # field[coord[0]][coord[1]][3] += random.randint(1, 10)
            # print(f'Ячейка - {field[coord[0]][coord[1]]}')
            # field[coord[0]][coord[1]][3] += random.randint(0, 15000)
            if coord[0] < blockCount - 1:
                if [field[coord[0] + 1][coord[1]][0], field[coord[0] + 1][coord[1]][1],
                    field[coord[0] + 1][coord[1]][2]] != command:
                    pass
                else:
                    drug += 1
            if coord[0] != 0:
                if [field[coord[0] - 1][coord[1]][0], field[coord[0] - 1][coord[1]][1],
                    field[coord[0] - 1][coord[1]][2]] != command:
                    pass
                else:
                    drug += 1
            if coord[1] != 0:
                if [field[coord[0]][coord[1] - 1][0], field[coord[0]][coord[1] - 1][1],
                    field[coord[0]][coord[1] - 1][2]] != command:
                    pass
                else:
                    drug += 1
            if coord[1] < blockCount - 1:
                if [field[coord[0]][coord[1] + 1][0], field[coord[0]][coord[1] + 1][1],
                    field[coord[0]][coord[1] + 1][2]] != command:
                    pass
                else:
                    drug += 1

            # if start2 is True:
            #     free_cell.append(coord)

            # if coord[0] < blockCount - 1:
            #     if coord[1] < blockCount - 1:
            #         if [field[coord[0] + 1][coord[1] + 1][0], field[coord[0] + 1][coord[1] + 1][1],
            #             field[coord[0] + 1][coord[1] + 1][2]] != command:
            #             pass
            #         else:
            #             drug += 1
            # if coord[0] < blockCount - 1:
            #     if coord[1] != 0:
            #         if [field[coord[0] + 1][coord[1] - 1][0], field[coord[0] + 1][coord[1] - 1][1],
            #             field[coord[0] + 1][coord[1] - 1][2]] != command:
            #             pass
            #         else:
            #             drug += 1
            # if coord[0] != 0:
            #     if coord[1] < blockCount - 1:
            #         if [field[coord[0] - 1][coord[1] + 1][0], field[coord[0] - 1][coord[1] + 1][1],
            #             field[coord[0] - 1][coord[1] + 1][2]] != command:
            #             pass
            #         else:
            #             drug += 1
            # if coord[0] != 0:
            #     if coord[1] != 0:
            #         if [field[coord[0] - 1][coord[1] - 1][0], field[coord[0] - 1][coord[1] - 1][1],
            #             field[coord[0] - 1][coord[1] - 1][2]] != command:
            #             pass
            #         else:
            #             drug += 1
            # print(drug)
            if drug >= 0:
                free_cell.append(coord)
            elif start != 0:
                free_cell.append(coord)

        if len(free_cell) != 0:
            catch_cell = random.choice(free_cell)
            power_cell_catch = field[catch_cell[0]][catch_cell[1]][3]
            attacking_cell = []
            if catch_cell[0] < blockCount - 1:
                if [field[catch_cell[0] + 1][catch_cell[1]][0], field[catch_cell[0] + 1][catch_cell[1]][1],
                    field[catch_cell[0] + 1][catch_cell[1]][2]] != command:
                    if field[catch_cell[0] + 1][catch_cell[1]] not in attacking_cell:
                        attacking_cell.append([catch_cell[0] + 1, catch_cell[1]])
            if catch_cell[0] != 0:
                if [field[catch_cell[0] - 1][catch_cell[1]][0], field[catch_cell[0] - 1][catch_cell[1]][1],
                    field[catch_cell[0] - 1][catch_cell[1]][2]] != command:
                    if field[catch_cell[0] - 1][catch_cell[1]] not in attacking_cell:
                        attacking_cell.append([catch_cell[0] - 1, catch_cell[1]])
            if catch_cell[1] != 0:
                if [field[catch_cell[0]][catch_cell[1] - 1][0], field[catch_cell[0]][catch_cell[1] - 1][1],
                    field[catch_cell[0]][catch_cell[1] - 1][2]] != command:
                    if field[catch_cell[0]][catch_cell[1] - 1] not in attacking_cell:
                        attacking_cell.append([catch_cell[0], catch_cell[1] - 1])
            if catch_cell[1] < blockCount - 1:
                if [field[catch_cell[0]][catch_cell[1] + 1][0], field[catch_cell[0]][catch_cell[1] + 1][1],
                    field[catch_cell[0]][catch_cell[1] + 1][2]] != command:
                    if field[catch_cell[0]][catch_cell[1] + 1] not in attacking_cell:
                        attacking_cell.append([catch_cell[0], catch_cell[1] + 1])
            # if catch_cell[0] < blockCount - 1:
            #     if catch_cell[1] < blockCount - 1:
            #         if field[catch_cell[0] + 1][catch_cell[1] + 1] != command and field[catch_cell[0] + 1][
            #             catch_cell[1] + 1] not in attacking_cell:
            #             attacking_cell.append([catch_cell[0] + 1, catch_cell[1] + 1])
            # if catch_cell[0] < blockCount - 1:
            #     if catch_cell[1] != 0:
            #         if field[catch_cell[0] + 1][catch_cell[1] - 1] != command and field[catch_cell[0] + 1][
            #             catch_cell[1] - 1] not in attacking_cell:
            #             attacking_cell.append([catch_cell[0] + 1, catch_cell[1] - 1])
            # if catch_cell[0] != 0:
            #     if catch_cell[1] < blockCount - 1:
            #         if field[catch_cell[0] - 1][catch_cell[1] + 1] != command and field[catch_cell[0] - 1][
            #             catch_cell[1] + 1] not in attacking_cell:
            #             attacking_cell.append([catch_cell[0] - 1, catch_cell[1] + 1])
            # if catch_cell[0] != 0:
            #     if catch_cell[1] != 0:
            #         if field[catch_cell[0] - 1][catch_cell[1 - 1]] != command and field[catch_cell[0] - 1][
            #             catch_cell[1 - 1]] not in attacking_cell:
            #             attacking_cell.append([catch_cell[0] - 1, catch_cell[1] - 1])
            if len(attacking_cell) != 0:
                end = False
                cikl = 0
                while end is False:
                    # print(1)
                    # print(f'{len(attacking_cell)} - {cikl}')
                    if len(attacking_cell) >= cikl:

                        # print(f'Vot - {attacking_cell}')
                        attacking_cell = random.choice(attacking_cell)
                        # print(attacking_cell)

                        try:
                            power_cell_attacking = field[attacking_cell[0]][attacking_cell[1]][3]
                        except Exception as exc:
                            break

                        # print(f'{catch_cell} - {attacking_cell}')
                        # print(f'{power_cell_catch} - {power_cell_attacking}')
                        # surprise = power_cell_catch // 100 * 200
                        if power_cell_catch >= power_cell_attacking:
                            # print(f'Атака - {attacking_cell}')

                            # remains_power = power_cell_catch - power_cell_attacking
                            # if random.choice([True, False]) is True:
                            #     remains_power *=10
                            # remains_power = int(remains_power)
                            # if remains_power > 1:
                            #     remains_power //= 2
                            # remains_power = 0
                            # remains_power_catch = int((remains_power / 100 * 30) + remains_power)

                            power_cell_catch+=random.randint(2,30)


                            if random.choice(c_n):
                                print(f'Выпала удача.')
                                power_cell_catch+=random.randint(4000,10000)
                            field[attacking_cell[0]][attacking_cell[1]] = [field[catch_cell[0]][catch_cell[1]][0],
                                                                           field[catch_cell[0]][catch_cell[1]][1],
                                                                           field[catch_cell[0]][catch_cell[1]][2],
                                                                           power_cell_catch]
                            field[catch_cell[0]][catch_cell[1]] = [field[catch_cell[0]][catch_cell[1]][0],
                                                                   field[catch_cell[0]][catch_cell[1]][1],
                                                                   field[catch_cell[0]][catch_cell[1]][2],
                                                                   power_cell_catch-1]

                            # new_massive = []
                            # for m in commandCoordinates:
                            #     new_massive.append(m)
                            # new_massive.append(attacking_cell)

                            for g in range(commandsCount):
                                if commandsCountMassiveCoordinates[g] != i:
                                    if attacking_cell in commandsCountMassiveCoordinates[g]:
                                        # print(commandsCountMassiveCoordinates[g])
                                        commandsCountMassiveCoordinates[g].remove(attacking_cell)
                                        # print(commandsCountMassiveCoordinates[g])
                                        # print('\n')
                                        # print('Удалено')
                                        # if len(commandsCountMassiveCoordinates[g]) == 0:
                                        # commandsCountMassiveCoordinates.remove(g)
                                        # commandsCountMassive.pop(g)

                            commandsCountMassiveCoordinates[i] += [attacking_cell]
                            end = True
                        cikl+=1
                    else:
                        end = True
