# TAMIZH-assessment
Problem Statement

You are developing firmware for a wearable device with limited battery capacity.

The device must execute a sequence of tasks in a fixed order. Each task consumes battery power at a constant rate while running. Between tasks, the device may remain idle, allowing the battery to recharge at a constant rate.

Your goal is to determine the minimum total runtime (task execution time + charging time) required to complete all tasks while ensuring that the battery never violates its constraints.

Inputs
batteryCapacity

Maximum battery capacity in mAh.

initialBattery

Initial battery level in mAh.

tasks

A list of tasks where:

tasks[i] = [duration_i, drainRate_i]
duration_i → Execution time of the task (seconds)
drainRate_i → Battery consumption rate (mAh/second)
chargeRate

Battery recharge rate during idle periods (mAh/second).

Constraints
Tasks must be executed in the given order.
Tasks cannot be interrupted once started.
Idle (charging) periods may be inserted between tasks.
Idle duration can be any non-negative real number.
Battery level must never fall below 0.
Battery level must never exceed batteryCapacity.
Battery changes continuously over time.
Return -1 if completing all tasks is impossible.
Return the final answer rounded to one decimal place.
