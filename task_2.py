#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    for ww in range(2):
        move_right()
        move_down()
    fill_cell()
    for q in range(1):
        move_right(2)
        move_down()


if __name__ == '__main__':
    run_tasks()
