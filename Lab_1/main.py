from lab_1 import WorkerController

if __name__ == '__main__':

    c=WorkerController()
    name = 'true'
    while c.active:
        c.print_task_list()
        task_number = input("Введите номер команды: ")

        match task_number:
            case '1':
                c.create()
            case '2':
                c.delete()
            case '3':
                c.update()
            case '4':
                c.selectAll()
            case '5':
                c.selectByQuery()
            case '6':
                c.plotBar()
            case '7':
                c.plotCircle()
            case '8':
                c.exit()
            case _:
                print(f"Неизвестный номер команды: {task_number}")
