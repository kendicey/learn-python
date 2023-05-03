def hanoi(disks, source, helper, destination):
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(
            disks, source, destination))
        return
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(
        disks, source, destination))
    hanoi(disks - 1, helper, source, destination)


disks = int(input('Number of disks to be displaced: '))
hanoi(disks, 'A', 'B', 'C')
